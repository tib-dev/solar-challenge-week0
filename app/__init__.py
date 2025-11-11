"""
App package initialization.

This package contains the Streamlit dashboard and supporting utilities for
data loading, analysis, and visualization of the Solar Challenge Week 0 project.
"""

from utils.data_utils import load_country_data
from utils.eda_utils import compare_metrics, summarize_kpis
from utils.dashboard_utils import plot_box, plot_bar, kpi_summary

__all__ = [
    "load_country_data",
    "compare_metrics",
    "summarize_kpis",
    "plot_box",
    "plot_bar",
    "kpi_summary",
]
