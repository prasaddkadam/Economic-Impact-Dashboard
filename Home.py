import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Economic Impact"
)

st.title('Economic Impact')

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('data/bg_image4.jpg')  

st.markdown(
    """
    #### In this captivating fusion of art and analytics, discover the hidden gems of knowledge that lie within the data. Gain evidence-backed insights into the ripple effects of economic decisions, identify emerging opportunities, and unravel the threads that connect industries and regions.
    """)

st.markdown(
    """#### Economic impact refers to thethe results and implications that different variables have on the general economic performance of a nation, sector, or particular event. It covers a wide variety of topics, including as population, CO2 Emissions, Child Mortality, and Life Expectancy. We can learn a lot about how certain events, policies, or trends effect the economy at various sizes by visualising economic impact data. Making educated judgements, comprehending the interdependence of economic variables, and seeing chances for development and progress are all made possible as a result. Our information visualisation dashboard seeks to provide customers the tools they need to study and analyse economic trends, spot patterns, and make well-informed decisions by using interactive and aesthetically pleasing data visualisations."""
)
