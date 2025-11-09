import pandas as pd
import numpy as np


class Preprocessor:
    """Handles missing value imputation and outlier removal."""

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def fill_missing(self, columns: list, method: str = "median") -> pd.DataFrame:
        for col in columns:
            if col in self.df.columns:
                if method == "median":
                    self.df[col].fillna(self.df[col].median(), inplace=True)
                elif method == "mean":
                    self.df[col].fillna(self.df[col].mean(), inplace=True)
                else:
                    self.df[col].fillna(0, inplace=True)
        return self.df

    def drop_outliers(self, mask: pd.Series) -> pd.DataFrame:
        if mask is not None:
            self.df = self.df[~mask]
        return self.df

    def drop_null_rows(self, threshold=0.5) -> pd.DataFrame:
        """Drop rows where >50% of values are missing."""
        limit = int(self.df.shape[1] * threshold)
        self.df.dropna(thresh=limit, inplace=True)
        return self.df
