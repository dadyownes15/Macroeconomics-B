from pathlib import Path

import pandas as pd
import requests


FRED_API_KEY = "9fb7818ec505ebe0f36e58efc607471c"
FRED_API_URL = "https://api.stlouisfed.org/fred/series/observations"


SERIES_IDS = {
    "price_index": "QDKN628BIS",
    "cost_index": "OPCNRE01DKQ661N",
    "permits_index": "DNKPERMITQISMEI",
}

CACHE_FILENAME = "denmark_housing_q_fred_cache.csv"


def _to_quarter_index(date_values):
    return pd.PeriodIndex(pd.to_datetime(date_values), freq="Q")


def fetch_fred_series(series_id, api_key=FRED_API_KEY, session=None):
    session = session or requests.Session()
    response = session.get(
        FRED_API_URL,
        params={
            "series_id": series_id,
            "api_key": api_key,
            "file_type": "json",
            "sort_order": "asc",
        },
        timeout=30,
    )
    response.raise_for_status()

    payload = response.json()
    observations = pd.DataFrame(payload["observations"])
    observations = observations.loc[observations["value"] != ".", ["date", "value"]].copy()
    observations["value"] = pd.to_numeric(observations["value"], errors="coerce")
    observations["quarter"] = _to_quarter_index(observations["date"])

    series = observations.set_index("quarter")["value"].sort_index()
    series.name = series_id
    return series


def _build_dataset(raw_df):
    # Start from the raw merged quarterly data, sort it by time,
    # drop any rows where one of the series is missing,
    # and make a copy so we can safely modify it.
    df = raw_df.sort_index().dropna().copy()

    # Create a Boolean mask that is True for all observations in 2015.
    # We will use 2015 as the base year for normalization.
    base_mask = df.index.year == 2015

    # Compute the average level in 2015 for the three underlying series.
    # These averages define "2015 = 100" for each series.
    base = df.loc[base_mask, ["price_index", "cost_index", "permits_index"]].mean()

    # Rebase the house price index so that its 2015 average equals 100.
    # Example: if price_index equals its 2015 average, this becomes 100.
    df["price_rebased"] = 100 * df["price_index"] / base["price_index"]

    # Rebase the construction cost index in the same way, with 2015 = 100.
    df["cost_rebased"] = 100 * df["cost_index"] / base["cost_index"]

    # Construct normalized housing q as the ratio of the rebased price index
    # to the rebased construction cost index.
    # If both move equally relative to 2015, q stays around 1.
    df["housing_q"] = df["price_rebased"] / df["cost_rebased"]

    # Rebase the building permits series so that its 2015 average also equals 100.
    df["permits_rebased"] = 100 * df["permits_index"] / base["permits_index"]

    # Smooth the permits series with a 4-quarter moving average.
    # min_periods=1 means the first few quarters are still kept,
    # even before four observations are available.
    df["permits_4q_ma"] = df["permits_rebased"].rolling(4, min_periods=1).mean()

    # Return the final dataset with the original and newly constructed columns.
    return df


def _cache_to_frame(cache_path):
    cached = pd.read_csv(cache_path)
    cached["quarter"] = pd.PeriodIndex(cached["quarter"], freq="Q")
    return cached.set_index("quarter").sort_index()


def _frame_to_cache(df, cache_path):
    output = df.reset_index(names="quarter").copy()
    output["quarter"] = output["quarter"].astype(str)
    output.to_csv(cache_path, index=False)


def load_or_fetch_denmark_housing_q(api_key=FRED_API_KEY, cache_path=None):
    cache_path = Path(cache_path or Path(__file__).with_name(CACHE_FILENAME))

    try:
        session = requests.Session()
        raw_df = pd.concat(
            {
                name: fetch_fred_series(series_id, api_key=api_key, session=session)
                for name, series_id in SERIES_IDS.items()
            },
            axis=1,
        )
        dataset = _build_dataset(raw_df)
        _frame_to_cache(dataset, cache_path)
        return dataset, "live FRED"
    except Exception:
        if cache_path.exists():
            return _cache_to_frame(cache_path), "local cache"
        raise
