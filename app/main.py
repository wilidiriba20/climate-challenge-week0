import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="EthioClimate Analytics", layout="wide")

st.title("COP32 Climate Trend Analysis")
st.markdown("Exploratory Data Analysis for African Climate Vulnerability")

# 1. Sidebar Widgets
st.sidebar.header("Filters")
df = load_data()

# Country Selector
selected_countries = st.sidebar.multiselect(
    "Select Countries", 
    options=df['country'].unique(), 
    default=df['country'].unique()
)

# Year Slider
min_year, max_year = int(df['YEAR'].min()), int(df['YEAR'].max())
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Filtered Data
filtered_df = df[
    (df['country'].isin(selected_countries)) & 
    (df['YEAR'].between(year_range[0], year_range[1]))
]

# 2. Main Visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Temperature Trends (T2M)")
    fig_temp = px.line(filtered_df, x='YEAR', y='T2M', color='country', title="Mean Temperature Over Time")
    st.plotly_chart(fig_temp, use_container_width=True)

with col2:
    st.subheader("Precipitation Distribution")
    fig_precip = px.box(filtered_df, x='country', y='PRECTOTCORR', color='country', title="Rainfall Variability")
    st.plotly_chart(fig_precip, use_container_width=True)