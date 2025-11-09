import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from .visualization import Visualizer


class EDA:
    """Handles time series, correlation, and scatter plots for EDA."""

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.viz = Visualizer()

    def plot_time_series(self, cols):
        for col in cols:
            if col in self.df.columns:
                plt.figure(figsize=(10, 4))
                sns.lineplot(data=self.df, x="Timestamp", y=col)
                plt.title(f"{col} vs Time")
                plt.show()

    def correlation_heatmap(self, cols):
        cols = [c for c in cols if c in self.df.columns]
        corr = self.df[cols].corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.show()

    def scatter(self, x, y):
        if x in self.df.columns and y in self.df.columns:
            plt.figure(figsize=(7, 5))
            sns.scatterplot(data=self.df, x=x, y=y, alpha=0.6)
            plt.title(f"{y} vs {x}")
            plt.show()
