"""
Responsible for reading all temperature CSV files from a folder
and returning one combined DataFrame with numeric month columns.
"""

from pathlib import Path
import pandas as pd
from config import MONTHS

def load_all_files(folder_name: str = "temperatures"):
    """
    Load all CSV files in the given folder and combine them into one DataFrame.

    Some files may be tab separated. If a file loads with only 1 column,
    we retry reading using tab separator.
    Month columns are converted to numeric. Invalid values become NaN.

    Args:
        folder_name: Folder containing CSV files.

    Returns:
        Combined pandas DataFrame containing all rows from all files.

    Raises:
        FileNotFoundError: If the folder doesn't exist or contains no CSV files.
    """
    folder = Path(folder_name)

    # Check folder exists
    if not folder.exists():
        raise FileNotFoundError(f"{folder_name} folder not found")

    files = list(folder.glob("*.csv"))

    # Ensure there are CSV files to read
    if not files:
        raise FileNotFoundError(f"No CSV files found in {folder_name} folder")

    data_frames: list[pd.DataFrame] = []

    print("Loading temperature files:")

    for file in files:
        try:
            # Try normal CSV read
            df = pd.read_csv(file)

            # If it looks like a tab-separated file, re-read it properly
            if len(df.columns) == 1:
                df = pd.read_csv(file, sep="\t")

            data_frames.append(df)
            print(f"- {file.name} loaded")
        except Exception:
            print(f"- {file.name} could not be loaded")

    # Merge all files into a single DataFrame
    all_data = pd.concat(data_frames, ignore_index=True)

    # Convert month columns to numeric (invalid values -> NaN)
    for month in MONTHS:
        all_data[month] = pd.to_numeric(all_data[month], errors="coerce")

    print(f"Total files loaded: {len(data_frames)}")

    return all_data