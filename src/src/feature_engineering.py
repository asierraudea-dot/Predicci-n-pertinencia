import pandas as pd


class FeatureEngineering:

    def create_features(self, df):

        df["Produccion_Hectarea"] = (
            df["Produccion"] /
            df["Area"]
        )

        df["Indice_Productivo"] = (
            df["Produccion_Hectarea"] *
            df["Area"]
        )

        return df
