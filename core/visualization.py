import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


class Visualizer:
    """Handles advanced visualizations: wind rose, histograms, bubble charts."""

    @staticmethod
    def wind_rose(df: pd.DataFrame):
        if "WD" not in df.columns or "WS" not in df.columns:
            print("⚠️ Skipping wind rose — missing WD or WS column.")
            return

        bins = np.arange(0, 361, 30)
        labels = (bins[:-1] + 15).tolist()
        df["WD_bin"] = pd.cut(df["WD"] % 360, bins=bins, right=False, labels=labels)
        wind_summary = df.groupby("WD_bin")["WS"].mean().reindex(labels)
        theta = np.deg2rad([float(x) for x in wind_summary.index])
        radii = wind_summary.values

        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, polar=True)
        ax.bar(theta, radii, width=np.deg2rad(30), bottom=0.0, alpha=0.7)
        ax.set_title("Wind Rose — Mean WS by Direction")
        plt.show()

    @staticmethod
    def histograms(df, cols):
        for c in cols:
            if c in df.columns:
                plt.figure(figsize=(8, 4))
                sns.histplot(df[c].dropna(), bins=40, kde=True)
                plt.title(f"{c} Distribution")
                plt.show()

    @staticmethod
    def bubble_chart(df, x, y, size_col, title=None):
        if not all(col in df.columns for col in [x, y, size_col]):
            print(f"⚠️ Missing one of the required columns: {x}, {y}, {size_col}")
            return

        sample = df.sample(n=min(2000, len(df)))
        plt.figure(figsize=(8, 6))
        plt.scatter(
            sample[x],
            sample[y],
            s=(sample[size_col] - sample[size_col].min() + 1) * 2,
            alpha=0.5,
        )
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(title or f"{y} vs {x} (size = {size_col})")
        plt.show()
