import plotly.express as px
import pandas as pd


def plot_box(df: pd.DataFrame, metric: str):
    """
    Create a boxplot comparing metric distributions across countries.
    """
    fig = px.box(
        df,
        x="Country",
        y=metric,
        color="Country",
        title=f"{metric} Distribution by Country",
        template="plotly_white",
    )
    return fig


def plot_bar(summary_df: pd.DataFrame):
    """
    Create bar chart ranking countries by average GHI.
    """
    fig = px.bar(
        summary_df,
        x="Country",
        y="mean_GHI",
        color="Country",
        text_auto=".2f",
        title="Average GHI by Country",
        template="plotly_white",
    )
    return fig


def kpi_summary(kpi: dict):
    """
    Return Streamlit metrics layout for KPIs.
    """
    import streamlit as st

    col1, col2, col3 = st.columns(3)
    col1.metric("Top Country by Avg GHI", kpi["Top Country"], f"{kpi['Max GHI']:.2f}")
    col2.metric("Lowest Avg GHI", kpi["Lowest Country"], f"{kpi['Min GHI']:.2f}")
    col3.metric("Average GHI (All)", f"{kpi['Mean GHI']:.2f}")
