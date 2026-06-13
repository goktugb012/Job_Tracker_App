import streamlit as st
import pandas as pd
import os
from datetime import date

def clear_form():
    st.session_state["company"] = ""
    st.session_state["position"] = ""
    st.session_state["salary"] = ""
    st.session_state["home_office"] = None
    st.session_state["status"] = None
    st.session_state["notes"] = ""
    st.session_state["application_date"] = date.today()



st.title("Job Application Tracker")

title_colunm, button_column = st.columns([4,1])

with  title_colunm:
    st.subheader("Application Details")
with button_column:
    st.button("Clear All", on_click=clear_form)


with st.form("application_form", clear_on_submit=True):
    company = st.text_input("Company Name", key="company")
    position = st.text_input("Position", key="position")
    salary = st.text_input("Salary", key="salary")
    home_office = st.selectbox(
        "Home Office", ["Yes", "No", "?"], index=None, placeholder="Select", key = "home_office")
    application_date = st.date_input("Application Date", key="application_date")
    notes = st.text_area("Notes",key="notes")
    status = st.selectbox(
        "Application Status", ["Applied", "Interview", "Rejected", "Offer"], key="status")
    submitted = st.form_submit_button("Submit Application")

if submitted:

    if not company.strip():
        st.warning("Company Name required")
    elif not position.strip():
        st.warning("Position Name required")
    elif status is None:
        st.warning("Status required")
    else:
        new_application = pd.DataFrame([{
            "Company": company,
            "Position": position,
            "Salary": salary,
            "Home Office": home_office,
            "Status": status,
            "Application Date": application_date,
            "Notes": notes
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