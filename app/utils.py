import pandas as pd
import streamlit as st

@st.cache_data  # This speeds up the app by keeping data in memory
def load_data():
    countries = ["ethiopia", "kenya", "sudan", "tanzania", "nigeria"]
    all_data = []
    for country in countries:
        df = pd.read_csv(f"data/{country}_clean.csv")
        df['country'] = country.capitalize()
        all_data.append(df)
    return pd.concat(all_data)