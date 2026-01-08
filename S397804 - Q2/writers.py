import pandas as pd


def write_average_file(averages: dict[str, float], filename: str = "average_temp.txt"):
    """
    Write seasonal averages into a text file.

    Args:
        Dict of season.
        Output file name.
    """
    with open(filename, "w") as file:
        for season in ["Summer", "Autumn", "Winter", "Spring"]:
            file.write(f"{season}: {averages[season]:.1f}°C\n")

def write_range_file(ranges: pd.DataFrame, filename: str = "largest_temp_range_station.txt"):
    """
    Write station(s) with the largest temperature range to a text file.

    If multiple stations tie for the largest range, all are written.

    Args:
        DataFrame with columns min, max, range (indexed by station).
        Output file name.
    """
    max_range = ranges["range"].max()
    winners = ranges[ranges["range"] == max_range]

    with open(filename, "w") as file:
        for name, row in winners.iterrows():
            file.write(
                f"{name}: Range {row['range']:.1f}°C "
                f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
            )

def write_stability_file(std_dev: pd.Series, filename: str = "temperature_stability_stations.txt"):
    """
    Write the most stable and most variable stations based on std deviation.

    Args:
        Series indexed by station name with std dev values.
        Output file name.
    """
    min_std = std_dev.min()
    max_std = std_dev.max()

    with open(filename, "w") as file:
        for name, value in std_dev[std_dev == min_std].items():
            file.write(f"Most Stable: {name}: StdDev {value:.1f}°C\n")

        for name, value in std_dev[std_dev == max_std].items():
            file.write(f"Most Variable: {name}: StdDev {value:.1f}°C\n")