import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (you must combine your CSVs into one file OR load multiple)
ethiopia = pd.read_csv("data/ethiopia_clean.csv")
kenya = pd.read_csv("data/kenya_clean.csv")
sudan = pd.read_csv("data/sudan_clean.csv")
tanzania = pd.read_csv("data/tanzania_clean.csv")    
nigeria = pd.read_csv("data/nigeria_clean.csv")  


df = pd.concat([ethiopia, kenya, sudan, tanzania, nigeria])

st.title("Climate Dashboard")

#  COUNTRY SELECTOR
countries = st.multiselect(
    "Select Country",
    df["Country"].unique(),
    default=df["Country"].unique()
)

# YEAR FILTER 
year_range = st.slider(
    "Select Year Range",
    int(df["YEAR"].min()),
    int(df["YEAR"].max()),
    (2015, 2026)
)

# VARIABLE SELECTOR 
variable = st.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)

# FILTER DATA 
filtered = df[
    (df["Country"].isin(countries)) &
    (df["YEAR"] >= year_range[0]) &
    (df["YEAR"] <= year_range[1])
]

# TEMPERATURE TREND 
st.subheader("Temperature Trend")

temp = filtered.groupby(["YEAR", "Country"])["T2M"].mean().unstack()
st.line_chart(temp)

# PRECIPITATION BOXPLOT 
st.subheader("Precipitation Distribution")

fig, ax = plt.subplots()
sns.boxplot(x="Country", y="PRECTOTCORR", data=filtered, ax=ax)
st.pyplot(fig)