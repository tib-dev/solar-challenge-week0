import pandas as pd
from scipy import stats


def compare_metrics(df: pd.DataFrame, metrics: list[str]) -> pd.DataFrame:
    """
    Compute mean, median, and standard deviation of given metrics per country.
    """
    summary = (
        df.groupby("Country")[metrics]
        .agg(["mean", "median", "std"])
        .round(2)
        .reset_index()
    )
    summary.columns = ["_".join(c).strip("_") for c in summary.columns.values]
    return summary


def summarize_kpis(summary_df: pd.DataFrame) -> dict:
    """
    Extract high-level KPI statistics from summary DataFrame.
    """
    top_row = summary_df.loc[summary_df["mean_GHI"].idxmax()]
    low_row = summary_df.loc[summary_df["mean_GHI"].idxmin()]
    mean_val = summary_df["mean_GHI"].mean()

    return {
        "Top Country": top_row["Country"],
        "Max GHI": top_row["mean_GHI"],
        "Lowest Country": low_row["Country"],
        "Min GHI": low_row["mean_GHI"],
        "Mean GHI": mean_val,
    }


def run_anova(df: pd.DataFrame, metric: str) -> float:
    """
    Run one-way ANOVA to test for differences in a metric between countries.
    Returns the p-value.
    """
    grouped = [group[metric].dropna() for _, group in df.groupby("Country")]
    stat, p = stats.f_oneway(*grouped)
    return p
