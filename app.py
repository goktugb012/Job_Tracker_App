import streamlit as st
import pandas as pd
import os





st.title("Job Application Tracker")

st.subheader("Application Details")

company = st.text_input("Company Name")
position = st.text_input("Position")
salary = st.text_input("Salary")
home_office = st.selectbox(
    "Home Office", ["Yes", "No", "?"], index=None, placeholder="Select")
application_date = st.date_input("Application Date")
notes = st.text_area("Notes")

status = st.selectbox(
    "Application Status", ["Applied", "Interview", "Rejected", "Offer"])

if st.button("Submit Application"):

    new_application = pd.DataFrame([{
        "Company": company,
        "Position": position,
        "Salary": salary,
        "Home Office": home_office,
        "Status": status
    }])

    if os.path.exists("applications.csv"):
        new_application.to_csv(
            "applications.csv",
            mode="a",
            header=False,
            index=False
        )

    else:
        new_application.to_csv(
            "applications.csv",
            index=False
        )

    st.success("Application saved.")

st.subheader("Saved Applications")
if st.button("View Applications"):
    st.switch_page("pages/1_Applications.py")