from xgboost import XGBRegressor


class PertinencePredictor:

    def train(self, X, y):

        model = XGBRegressor(

            n_estimators=300,

            learning_rate=0.05,

            max_depth=6,

            random_state=42

        )

        model.fit(X, y)

        return model
