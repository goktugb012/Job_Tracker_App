import streamlit as st
import pandas as pd
import os

st.title("Applications")

if os.path.exists("applications.csv"):
    applications = pd.read_csv("applications.csv")

    status_options = ["All"] + sorted(
        applications["Status"].dropna().unique().tolist()
    )

    selected_status = st.selectbox("Filter by Status", status_options, index=0)

    filtered_applications = applications.copy()

    if selected_status != "All":
        filtered_applications = applications[
            applications["Status"] == selected_status
        ].copy()
    if selected_status == "All":
        edited_applications = st.data_editor(
            filtered_applications,
            use_container_width=True,
            hide_index=True,
            num_rows="dynamic"
        )
    else:
        st.dataframe(filtered_applications,
                     width="stretch", hide_index=True)
        
                
    if st.button("Save Changes"):
        edited_applications.to_csv("applications.csv", index=False)
        st.success("Changes saved successfully.")
    
else:
    st.info("No applications have been saved yet.")