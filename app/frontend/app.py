import streamlit as st
import requests

st.set_page_config(page_title="AI ML Prediction Models")
st.write("# Welcome to AI Apps Home Page! 👋")

st.markdown(
    """
    Here are some collection of Machine Learning and Data Science projects.

    **👈 Select a project from the menu on the left** """
)

iris_page = st.Page("iris_app.py", title="Iris Prediction")
depression_page = st.Page("depression_app.py", title="Patient Depression Prediction")
pg = st.navigation([iris_page, depression_page])
pg.run()