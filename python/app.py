import streamlit as st
st.markdown("<h1 style='color:#00c2ff;'>Workforce Planning Dashboard</h1>", unsafe_allow_html=True)
st.write("Hello, this is my first Streamlit app.")
import pandas as pd

df = pd.read_csv("workforce_clean.csv")
st.subheader("Workforce Data")
st.dataframe(df)
st.subheader("Monte Carlo Simulation")
st.image("montecarlo_chart.png")

st.subheader("Workload Ratio by Department")
st.image("workload_chart.png")
st.subheader("Try a Headcount Scenario")

dept = st.selectbox("Select Department", df["Department"].unique())
target_headcount = st.slider("Target Headcount", min_value=0, max_value=200, value=50)

st.write(f"You selected **{dept}** with a target headcount of **{target_headcount}**.")