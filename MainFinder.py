import streamlit as st
import pandas as pd



st.set_page_config(layout="wide", page_title="Disc Finder")

st.markdown('''<h1 style='text-align: center; font-size: 30pt; margin-top: -20px;'>Welcome To The Disc Finder</h1>''', unsafe_allow_html=True)

with st.sidebar:

    st.text_input("Please Enter Series Title Here:")

    st.radio("Please Select Media Type:", ["Movie", "TV Series"])

    st.multiselect("Please Select Which Media Format's Are Acceptable:", ["DVD", "Blu Ray", "Ultra 4K"])