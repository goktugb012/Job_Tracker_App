import streamlit as st

st.title("Job Application Tracker")
st.write("Tracker")

st.subheader("Applications")

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
    st.success(f"{company} şirketindeki {position} pozisyonu eklendi.")