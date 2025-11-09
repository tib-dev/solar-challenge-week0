"""
Core package for Solar Challenge project.

Provides reusable utilities for:
- Data loading
- Profiling & statistics
- Cleaning & preprocessing
- EDA visualizations
- Automated pipeline
"""

from .data_loader import DataLoader
from .preprocessing import Preprocessor
from .profiling import Profiler
from .eda import EDA
from .visualization import Visualizer
from .pipeline import SolarPipeline

__all__ = [
    "DataLoader",
    "Preprocessor",
    "Profiler",
    "EDA",
    "Visualizer",
    "SolarPipeline",
]
