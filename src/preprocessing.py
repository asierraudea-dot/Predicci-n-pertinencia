import pandas as pd


class DataPreprocessor:

    def __init__(self, eva_path, sena_path):
        self.eva_path = eva_path
        self.sena_path = sena_path

    def load_data(self):

        eva = pd.read_csv(self.eva_path)

        sena = pd.read_excel(self.sena_path)

        return eva, sena

    def clean(self, df):

        df = df.drop_duplicates()

        df = df.fillna(0)

        return df
