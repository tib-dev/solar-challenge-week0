import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
# your existing functions
from app import load_country_data, compare_metrics, summarize_kpis

# ------------------------------------------------------------
# Utility: Normalize Summary Columns
# ------------------------------------------------------------


def normalize_summary_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert columns like 'GHI_mean' → 'mean_GHI' to keep consistent naming
    for summarize_kpis and visualization.
    """
    new_cols = []
    for c in df.columns:
        parts = c.split("_")
        if len(parts) == 2 and parts[1].lower() in {"mean", "median", "std"}:
            metric, agg = parts[0], parts[1].lower()
            new_cols.append(f"{agg}_{metric}")
        else:
            new_cols.append(c)
    df.columns = new_cols
    return df


# ------------------------------------------------------------
# Page Setup
# ------------------------------------------------------------
st.set_page_config(
    page_title="Solar Data Dashboard",
    page_icon="🌞",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------
# Header / Title
# ------------------------------------------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.3rem;
        color: #f39c12;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.05rem;
        color: #aaa;
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='main-title'>🌞 Solar Energy Metrics Dashboard</div>",
            unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Interactive analysis of GHI, DNI, and DHI across multiple countries</div>",
            unsafe_allow_html=True)

# ------------------------------------------------------------
# Sidebar Controls
# ------------------------------------------------------------
st.sidebar.header("⚙️ Dashboard Settings")

# Always find data folder relative to this file
data_dir = Path(__file__).resolve().parents[1] / "data" / "processed"

if not data_dir.exists():
    st.error(f"❌ Data directory not found: {data_dir}")
    st.stop()

# Auto-detect available CSVs
available_countries = sorted([f.stem.replace(
    "_clean", "").capitalize() for f in data_dir.glob("*_clean.csv")])

if not available_countries:
    st.warning(
        "⚠️ No cleaned CSV files found in data/processed/. Please add *_clean.csv files.")
    st.stop()

selected_countries = st.sidebar.multiselect(
    "Select Countries to Compare",
    available_countries,
    default=available_countries
)

metric = st.sidebar.selectbox("Select Solar Metric", ["GHI", "DNI", "DHI"])

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Visualization Options")
chart_type = st.sidebar.radio(
    "Select Chart Type", ["Boxplot", "Bar Chart"], index=0)

st.sidebar.markdown("---")
st.sidebar.caption(f"📂 Data path: `{data_dir}`")

# ------------------------------------------------------------
# Load and Combine Data
# ------------------------------------------------------------
dfs = []
for country in selected_countries:
    file_path = data_dir / f"{country.lower()}_clean.csv"
    if file_path.exists():
        df = load_country_data(file_path, country)
        dfs.append(df)
    else:
        st.warning(f"⚠️ Missing file for {country}")

if not dfs:
    st.warning("Please select at least one valid country.")
    st.stop()

combined_df = pd.concat(dfs, ignore_index=True)

# ------------------------------------------------------------
# KPI Section
# ------------------------------------------------------------
st.markdown("### Key Performance Indicators")

summary_df = compare_metrics(combined_df, ["GHI", "DNI", "DHI"])
summary_df = normalize_summary_columns(summary_df)

try:
    kpi_df = summarize_kpis(summary_df)
except KeyError as e:
    st.error(f"Error calculating KPIs: {e}")
    st.dataframe(summary_df)
    st.stop()

col1, col2, col3 = st.columns(3)
col1.metric("Top Country (Avg GHI)",
            kpi_df["Top Country"], f"{kpi_df['Max GHI']:.2f}")
col2.metric("Lowest Avg GHI",
            kpi_df["Lowest Country"], f"{kpi_df['Min GHI']:.2f}")
col3.metric("Overall Mean GHI", None, f"{kpi_df['Mean GHI']:.2f}")

# ------------------------------------------------------------
# Visualization Section
# ------------------------------------------------------------
st.markdown(f"### {metric} Comparison")

if chart_type == "Boxplot":
    fig = px.box(
        combined_df,
        x="Country",
        y=metric,
        color="Country",
        title=f"{metric} Distribution by Country",
        template="plotly_white",
    )
else:
    grouped = combined_df.groupby("Country")[metric].mean().reset_index()
    fig = px.bar(
        grouped,
        x="Country",
        y=metric,
        color="Country",
        text_auto=".2f",
        template="plotly_white",
        title=f"Average {metric} by Country",
    )

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------
# Summary Table
# ------------------------------------------------------------
st.markdown("### Summary Statistics")
st.dataframe(summary_df.style.highlight_max(axis=0), use_container_width=True)

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; font-size:0.9rem; color:#888;'>
        © 2025 Solar Insights Dashboard | Built with using Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
