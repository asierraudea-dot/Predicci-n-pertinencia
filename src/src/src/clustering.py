from sklearn.cluster import KMeans


class TerritorialCluster:

    def train(self, X):

        model = KMeans(
            n_clusters=4,
            random_state=42
        )

        model.fit(X)

        return model
