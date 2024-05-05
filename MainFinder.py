import streamlit as st
import pandas as pd



st.set_page_config(layout="wide", page_title="Disc Finder")

st.markdown('''<h1 style='text-align: center; font-size: 30pt; margin-top: -20px;'>Welcome To The Disc Finder</h1>''', unsafe_allow_html=True)
st.markdown("***")

col1, col2, col3 = st.columns([.5, 1, .5])

with col2:
st.markdown('''<p style='text-align: left; font-size: 15pt;'>Welcome to Disc Finder! Currently in development, this app may not function as intended. The concept driving this app is simple: major corporations such as Amazon, Disney, Netflix, and Apple heavily promote subscription services. Yet, why subscribe when you can create your own media server, ensuring perpetual access to your content? The only hurdle is locating the physical discs to build your collection, a challenging task given the scarcity of physical media on platforms like Amazon. This is where Disc Finder steps in. Our app aims to scour prominent websites such as Amazon, Blu-ray.com, and eBay to locate the precise discs you seek.</p>''', unsafe_allow_html=True)

with st.sidebar:

    st.text_input("Please Enter Series Title Here:")

    st.radio("Please Select Media Type:", ["Movie", "TV Series"])

    st.multiselect("Please Select Which Media Format's Are Acceptable:", ["DVD", "Blu Ray", "Ultra 4K"])