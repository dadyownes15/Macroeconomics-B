"""Utility functions for the Lecture 5 Phillips curve notebook."""

import time

import numpy as np
import pandas as pd
import requests


EUROSTAT_BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"


def fetch_eurostat(dataset, retries=4, sleep=4, **filters):
    """Download a Eurostat series and return it as a monthly pandas Series."""
    params = dict(filters)
    params["format"] = "JSON"

    last_error = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(
                f"{EUROSTAT_BASE}/{dataset}",
                params=params,
                timeout=30,
            )
            response.raise_for_status()
            data = response.json()
            break
        except requests.RequestException as exc:
            last_error = exc
            if attempt == retries:
                raise
            print(
                f"Eurostat request for {dataset} failed on attempt "
                f"{attempt}/{retries}: {exc}. Retrying..."
            )
            time.sleep(sleep)
    else:
        raise RuntimeError(f"Eurostat request failed: {last_error}")

    time_dim = data["dimension"]["time"]["category"]["index"]
    obs = data.get("value", {})
    values = []
    dates = []
    for label, pos in sorted(time_dim.items(), key=lambda kv: kv[1]):
        value = obs.get(str(pos))
        if value is None:
            continue
        dates.append(pd.Period(label, freq="M").to_timestamp())
        values.append(float(value))

    return pd.Series(values, index=pd.DatetimeIndex(dates), name=dataset).sort_index()


def simulate_as(par, regime):
    """Simulate inflation under a one-off supply shock and an expectation regime."""
    T = par["T"]
    pi = np.empty(T)
    pi_e = np.empty(T)

    pi_e[0] = par["pi_star"]
    for t in range(T):
        shock_t = par["shock"] if t == 0 else 0.0
        pi[t] = pi_e[t] + par["gamma"] * par["y_gap"] + shock_t

        if t + 1 < T:
            if regime == "static":
                pi_e[t + 1] = pi[t]
            elif regime == "anchored":
                pi_e[t + 1] = par["pi_star"]
            else:
                raise ValueError("regime must be 'static' or 'anchored'")

    return pi
