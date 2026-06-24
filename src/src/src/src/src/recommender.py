from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity


class Recommender:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def recommend(
            self,
            municipality,
            catalog
    ):

        emb = self.model.encode(
            municipality
        )

        cat = self.model.encode(
            catalog
        )

        similarity = cosine_similarity(
            [emb],
            cat
        )

        return similarity
