import pandas as pd
import numpy as np
from scipy import stats


class Profiler:
    """Performs data profiling, summary stats, and outlier detection."""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary(self) -> pd.DataFrame:
        return self.df.describe().T

    def missing_report(self) -> pd.DataFrame:
        missing = self.df.isna().sum()
        pct_missing = (missing / len(self.df)) * 100
        report = pd.DataFrame({"missing_count": missing, "missing_pct": pct_missing})
        return report[report["missing_pct"] > 0].sort_values(
            "missing_pct", ascending=False
        )

    def detect_outliers(self, columns: list):
        z_scores = np.abs(stats.zscore(self.df[columns], nan_policy="omit"))
        mask = (z_scores > 3).any(axis=1)
        return z_scores, mask
