import streamlit as st
import pandas as pd

st.set_page_config(page_title="Multi Page App")

st.title("Hello Worlds")
st.sidebar.success("Select a page above")
path = r"G:\Shared drives\FLORS QUANT\Benchmarks and Diagnostics\Skills Diagnostic\2023 Participation\Audit Skills\News Corp\Report Generation\News Corp\Completed.xlsx"
df1=pd.read_excel(path)
st.dataframe(data=df1)