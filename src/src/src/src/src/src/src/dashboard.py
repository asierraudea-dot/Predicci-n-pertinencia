import streamlit as st


class Dashboard:

    def run(self):

        st.title(
            "Sistema Inteligente de Planeación Territorial"
        )

        st.sidebar.title("Menú")

        page = st.sidebar.selectbox(

            "Seleccione",

            [

                "Inicio",

                "EDA",

                "Clusters",

                "Predicción",

                "Recomendaciones",

                "SHAP"

            ]

        )

        st.write(page)
