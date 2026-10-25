
import streamlit as st
import pandas as pd

st.title("Student Data Analytics")

# Upload a CSV file
file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    data = pd.read_csv(file)

    # Display the data and total students
    st.write(data)
    st.metric("Students", len(data))

    # Select a subject for analysis
    subject = st.selectbox("Select Subject", data.columns[1:])

    # Display chart if the selected column is numeric
    if pd.api.types.is_numeric_dtype(data[subject]):
        st.bar_chart(data[subject])
    else:
        st.warning("Please select a numeric subject column.")
else:
    st.info("Please upload a CSV file.")
