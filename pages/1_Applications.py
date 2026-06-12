import streamlit as st
import pandas as pd
import os

st.title("Applications")

if os.path.exists("applications.csv"):
    applications = pd.read_csv("applications.csv")
    edited_applications = st.data_editor(
        applications,
        use_container_width=True,
        hide_index=True
    )
    if st.button("Save Changes"):
        edited_applications.to_csv("applications.csv", index=False)
        st.success("Changes saved successfully.")
else:
    st.info("No applications have been saved yet.")