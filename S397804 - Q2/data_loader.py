"""
Responsible for reading all temperature CSV files from a folder
and returning one combined DataFrame with numeric month columns.
"""

from pathlib import Path
import pandas as pd
from config import MONTHS