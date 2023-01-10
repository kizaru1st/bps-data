#Library
import pandas as pd
import streamlit as st
import plotly.express as px 
from streamlit_option_menu import option_menu

# Create Localhost to host website
st.set_page_config(page_title='Aplikasi IPM Sumbar', 
                   page_icon=":bar_chart",
                   layout="wide")

st.header('Aplikasi Visualisasi Data IPM Provinsi Sumbar 2022')

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["UHH", "HLS", "RLS", "Perkapita"],
        icons=['house', 'gear', 'book', 'envelope'],
        menu_icon="cast",
        default_index=0
    )
    
if selected == "UHH":
    st.title(f"Pilih {selected}")
    excel_file = 'UHH.xlsx'
    sheet_name = 'DATA'

    df = pd.read_excel(excel_file, sheet_name = sheet_name, header = 1, usecols='A:D')
    st.dataframe(df)

    pie_chart = px.pie(df, title='UHH pada tahun 2020', values='2020', names='Kabupaten/Kota')
    st.plotly_chart(pie_chart)

    pie_chart = px.pie(df, title='UHH pada tahun 2021', values='2021', names='Kabupaten/Kota')
    st.plotly_chart(pie_chart)

    pie_chart = px.pie(df, title='UHH pada tahun 2022', values='2022', names='Kabupaten/Kota')
    st.plotly_chart(pie_chart)

