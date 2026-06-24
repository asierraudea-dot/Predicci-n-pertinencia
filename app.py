import streamlit as st

from src.dashboard import Dashboard

st.set_page_config(
    page_title="SENA AI Territorial",
    layout="wide"
)

dashboard = Dashboard()

dashboard.run()
