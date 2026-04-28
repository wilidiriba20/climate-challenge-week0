import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/all_countries.csv")

st.title("Climate Dashboard")

countries = st.multiselect("Select Countries", df["Country"].unique())

filtered = df[df["Country"].isin(countries)]

st.line_chart(filtered.groupby(["YEAR", "Country"])["T2M"].mean().unstack())

sns.boxplot(x="Country", y="PRECTOTCORR", data=filtered)
st.pyplot(plt)