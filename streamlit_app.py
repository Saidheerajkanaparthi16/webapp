#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport

# Web App Title
st.markdown('''
# **The EDA App**

This is the **EDA App** created in Streamlit using the **ydata_profiling** library.

**Credit:** App built in `Python` + `Streamlit`By Dheeraj
---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file])
""")

# Function to load data
def load_data(uploaded_file):
    csv = pd.read_csv(uploaded_file)
    return csv

# Function to generate profile report
def generate_profile_report(df):
    pr = ProfileReport(df, explorative=True)
    return pr.to_html()

# Displaying the Uploaded CSV and Profile Report
if uploaded_file is not None:
    df = load_data(uploaded_file)
    report_html = generate_profile_report(df)
    
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st.markdown(report_html, unsafe_allow_html=True)

else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        df = pd.DataFrame(np.random.rand(100, 5), columns=['a', 'b', 'c', 'd', 'e'])
        report_html = generate_profile_report(df)
        
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st.markdown(report_html, unsafe_allow_html=True)
