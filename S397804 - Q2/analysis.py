"""
 Seasonal averages
 Station temperature range (min/max/range)
 Station stability (standard deviation)
"""

import pandas as pd
from config import MONTHS, SEASONS

def seasonal_averages(df: pd.DataFrame):
    """
    Calculate average temperature for each season across all stations and months.

    The function flattens all values in the season's months, ignores NaNs,
    and computes the mean.

    Args:
        DataFrame containing month columns.

    Returns:
        Dictionary mapping season name average temperature.
    """
    results: dict[str, float] = {}

    for season, months in SEASONS.items():
        # Flatten values to one list-like array
        values = df[months].values.flatten()

        # Drop missing values and compute average
        avg = pd.Series(values).dropna().mean()
        results[season] = avg

    return results

def station_ranges(df: pd.DataFrame):
    """
    Compute min, max and range of temperatures per station.

    Convert wide month columns into long format using melt
    Group by station name and compute min/max
    Add range = max - min

    Args:
        DataFrame with station info and month columns.

    Returns:
        DataFrame indexed by station name with columns: min, max, range
    """
    long_df = df.melt(
        id_vars=["STATION_NAME", "STN_ID"],
        value_vars=MONTHS,
        var_name="Month",
        value_name="Temperature"
    ).dropna()

    grouped = long_df.groupby("STATION_NAME")["Temperature"]
    stats = grouped.agg(["min", "max"])
    stats["range"] = stats["max"] - stats["min"]

    return stats

def station_stability(df: pd.DataFrame):
    """
    Calculate temperature stability per station using population std deviation.

    Args:
        DataFrame with station info and month columns.

    Returns:
        pandas Series indexed by station name with std deviation values.
    """
    long_df = df.melt(
        id_vars=["STATION_NAME", "STN_ID"],
        value_vars=MONTHS,
        var_name="Month",
        value_name="Temperature"
    ).dropna()

    # ddof=0 means population standard deviation
    std_dev = long_df.groupby("STATION_NAME")["Temperature"].std(ddof=0)
    return std_dev
