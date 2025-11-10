import pandas as pd


def load_country_data(file_path, country_name):
    """Load and prepare individual country dataset."""
    df = pd.read_csv(file_path)
    df["Country"] = country_name
    return df


def compare_metrics(df, metrics):
    """Compute summary statistics (mean, median, std) for selected metrics."""
    summary = []
    for country, group in df.groupby("Country"):
        stats = {"Country": country}
        for m in metrics:
            stats[f"mean_{m}"] = group[m].mean()
            stats[f"median_{m}"] = group[m].median()
            stats[f"std_{m}"] = group[m].std()
        summary.append(stats)
    return pd.DataFrame(summary)


def summarize_kpis(summary_df):
    """Extract top-performing countries and KPIs."""
    top_country = summary_df.loc[summary_df["mean_GHI"].idxmax(), "Country"]
    lowest_country = summary_df.loc[summary_df["mean_GHI"].idxmin(), "Country"]
    return {
        "Top Country": top_country,
        "Max GHI": summary_df["mean_GHI"].max(),
        "Lowest Country": lowest_country,
        "Min GHI": summary_df["mean_GHI"].min(),
        "Mean GHI": summary_df["mean_GHI"].mean(),
    }
