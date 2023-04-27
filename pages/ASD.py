import streamlit as st
import pandas as pd

st.title("ASD Welcomes you")

uploadedFile = st.file_uploader("Upload", type=['csv','xlsx'],accept_multiple_files=False,key="fileUploader")

if uploadedFile is not None:
    df1=pd.read_excel(uploadedFile)
    st.dataframe(data=df1)