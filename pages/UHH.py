#Library
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu

excel_file = 'UHH.xlsx'
sheet_name = 'DATA'
df = pd.read_excel(excel_file,sheet_name = sheet_name,engine="openpyxl",usecols='A:D')
st.dataframe(df)

st.sidebar.header("Filter: ")
tahun = st.sidebar.selectbox(
"Pilih tahun: ",
["2020", "2021", "2022"]
)

if(tahun=="2020"):
    st.bar_chart(df, x="Kabupaten/Kota", y="2020")

elif(tahun=="2021"):
    st.bar_chart(df, x="Kabupaten/Kota", y="2021")

elif(tahun=="2022"):
    st.bar_chart(df, x="Kabupaten/Kota", y="2022")