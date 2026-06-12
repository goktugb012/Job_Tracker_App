import streamlit as st
import pandas as pd
import os

st.title("Applications")

if os.path.exists("applications.csv"):
    applications = pd.read_csv("applications.csv")
    st.dataframe(applications, use_container_width=True)
else:
    st.info("No applications have been saved yet.")