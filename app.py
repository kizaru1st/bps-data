#Library
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu

# Create Localhost to host website
st.set_page_config(page_title='Aplikasi IPM Sumbar',
                   page_icon=":bar_chart:",
                   layout='wide')

st.header('IPM Provinsi Sumbar 2022')


selected = option_menu(
    menu_title=None,
    options=["UHH", "HLS", "RLS", "Perkapita"],
    icons=['house', 'gear', 'book', 'envelope'],
    menu_icon="cast",
    default_index=0,
    orientation='horizontal',
)

if selected == "UHH":
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








