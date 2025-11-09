import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from app import load_country_data, compare_metrics, summarize_kpis  # use from app

# ----------------------------
# Page Setup
# ----------------------------
st.set_page_config(
    page_title="Solar Data Dashboard",
    page_icon="🌞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Header / Title Section
# ----------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.2rem;
        color: #f39c12;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<div class='main-title'>🌞 Solar Energy Metrics Dashboard</div>",
            unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Interactive exploration of GHI, DNI, and DHI across multiple countries</div>", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.header("⚙️ Dashboard Settings")

data_dir = Path("../data")
available_countries = [f.stem.replace(
    "_clean", "").capitalize() for f in data_dir.glob("*_clean.csv")]

selected_countries = st.sidebar.multiselect(
    "Select Countries to Compare",
    available_countries,
    default=available_countries
)

metric = st.sidebar.selectbox("Select Solar Metric", ["GHI", "DNI", "DHI"])

st.sidebar.markdown("---")
st.sidebar.markdown("**Visualization Options**")
chart_type = st.sidebar.radio(
    "Select Chart Type",
    ["Boxplot", "Bar Chart"],
    index=0
)

# ----------------------------
# Load and Combine Data
# ----------------------------
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

# ----------------------------
# KPI Section
# ----------------------------
st.markdown("### Key Performance Indicators")
summary_df = compare_metrics(combined_df, ["GHI", "DNI", "DHI"])
kpi_df = summarize_kpis(summary_df)

col1, col2, col3 = st.columns(3)
col1.metric("Top Country (Avg GHI)",
            kpi_df["Top Country"], f"{kpi_df['Max GHI']:.2f}")
col2.metric("Lowest Avg GHI",
            kpi_df["Lowest Country"], f"{kpi_df['Min GHI']:.2f}")
col3.metric("Overall Mean GHI", None, f"{kpi_df['Mean GHI']:.2f}")

# ----------------------------
# Visualization Section
# ----------------------------
st.markdown(f"### {metric} Comparison")

if chart_type == "Boxplot":
    fig = px.box(
        combined_df, x="Country", y=metric, color="Country",
        title=f"{metric} Distribution by Country", template="plotly_white"
    )
else:
    grouped = combined_df.groupby("Country")[metric].mean().reset_index()
    fig = px.bar(
        grouped, x="Country", y=metric, color="Country",
        text_auto=".2f", template="plotly_white",
        title=f"Average {metric} by Country"
    )

st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Summary Table
# ----------------------------
st.markdown("### Summary Statistics")
st.dataframe(summary_df.style.highlight_max(axis=0), use_container_width=True)

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; font-size:0.9rem; color:#666;'>
        © 2025 Solar Insights Dashboard 
    </div>
    """,
    unsafe_allow_html=True
)
