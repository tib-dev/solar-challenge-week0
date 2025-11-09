# core/pipeline.py
from .data_loader import DataLoader
from .preprocessing import Preprocessor
from .eda import EDA


class SolarPipeline:
    def __init__(self, data_path):
        self.loader = DataLoader(data_path)
        self.preprocessor = Preprocessor()
        self.eda = EDA()

    def run(self):
        df = self.loader.load()
        df_clean = self.preprocessor.clean(df)
        self.eda.summarize(df_clean)
