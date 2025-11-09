import pandas as pd
from pathlib import Path


def load_country_data(file_path: Path, country_name: str) -> pd.DataFrame:
    """
    Load a cleaned CSV for a given country and add metadata.

    Parameters
    ----------
    file_path : Path
        Path to the country's cleaned CSV file.
    country_name : str
        Name of the country to label data.

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame with a 'Country' column added.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    df = pd.read_csv(file_path)
    df["Country"] = country_name.capitalize()
    return df
