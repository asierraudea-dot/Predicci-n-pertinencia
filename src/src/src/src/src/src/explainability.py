import shap


class ExplainModel:

    def explain(self, model, X):

        explainer = shap.Explainer(model)

        values = explainer(X)

        return values
