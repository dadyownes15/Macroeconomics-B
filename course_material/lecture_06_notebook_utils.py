import numpy as np
import pandas as pd
import requests


FRED_BASE_URL = "https://api.stlouisfed.org/fred/series/observations"


def fetch_fred_series(series_id, fred_api_key, start="2018-01-01", frequency=None, fallback=None):
    params = {
        "series_id": series_id,
        "api_key": fred_api_key,
        "file_type": "json",
        "observation_start": start,
    }
    if frequency is not None:
        params["frequency"] = frequency

    try:
        response = requests.get(FRED_BASE_URL, params=params, timeout=20)
        response.raise_for_status()
        observations = response.json()["observations"]
        values = []
        dates = []
        for obs in observations:
            value = obs["value"]
            if value == ".":
                continue
            dates.append(pd.to_datetime(obs["date"]))
            values.append(float(value))
        series = pd.Series(values, index=pd.DatetimeIndex(dates), name=series_id)
        if series.empty:
            raise ValueError(f"No observations returned for {series_id}.")
        return series
    except Exception:
        if fallback is None:
            raise
        return fallback.copy()


def annual_percentage_change(series):
    return 100 * (series / series.shift(12) - 1)


def simulate_as_ad(T, a, gamma, s_path=None, z_path=None, pi0=0.0):
    s = np.zeros(T)
    z = np.zeros(T)
    if s_path is not None:
        s[: min(T, len(s_path))] = s_path[: min(T, len(s_path))]
    if z_path is not None:
        z[: min(T, len(z_path))] = z_path[: min(T, len(z_path))]

    beta = 1 / (1 + a * gamma)
    pi_gap = np.empty(T)
    y_gap = np.empty(T)

    prev_pi = pi0
    for t in range(T):
        pi_gap[t] = beta * prev_pi + gamma * beta * z[t] + beta * s[t]
        y_gap[t] = z[t] - a * pi_gap[t]
        prev_pi = pi_gap[t]

    return pd.DataFrame(
        {
            "period": np.arange(1, T + 1),
            "output_gap": y_gap,
            "inflation_gap": pi_gap,
            "supply_shock": s,
            "demand_shock": z,
        }
    )


def policy_table(a_values, gamma, s1, T):
    rows = []
    s_path = np.zeros(T)
    s_path[0] = s1
    for a in a_values:
        beta = 1 / (1 + a * gamma)
        sim = simulate_as_ad(T=T, a=a, gamma=gamma, s_path=s_path)
        rows.append(
            {
                "a": a,
                "beta": beta,
                "impact_output_gap": sim.loc[0, "output_gap"],
                "impact_inflation_gap": sim.loc[0, "inflation_gap"],
                "inflation_gap_period_4": sim.loc[3, "inflation_gap"],
            }
        )
    return pd.DataFrame(rows)


def fallback_monthly_series(values, start, name):
    index = pd.date_range(start=start, periods=len(values), freq="MS")
    return pd.Series(values, index=index, name=name)
