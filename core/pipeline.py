from .data_loader import DataLoader
from .profiling import Profiler
from .preprocessing import Preprocessor
from .eda import EDA


class SolarPipeline:
    """Runs the full EDA pipeline for a country dataset."""

    def __init__(self, country):
        self.country = country
        self.loader = DataLoader()
        self.df = None

    def run(self):
        self.df = self.loader.load_csv(f"{self.country}.csv")

        profiler = Profiler(self.df)
        print("Summary:")
        print(profiler.summary().head())

        z_cols = ["GHI", "DNI", "DHI", "ModA", "ModB", "WS", "WSgust"]
        z_cols = [c for c in z_cols if c in self.df.columns]
        _, mask = profiler.detect_outliers(z_cols)

        cleaner = Preprocessor(self.df)
        df_clean = cleaner.fill_missing(z_cols)
        df_clean = cleaner.drop_outliers(mask)

        print(
            f"✅ Cleaned {self.country} dataset. Rows remaining: {len(df_clean)}")

        eda = EDA(df_clean)
        eda.plot_time_series(["GHI", "DNI", "DHI", "Tamb"])
        eda.correlation_heatmap(["GHI", "DNI", "DHI", "Tamb"])
