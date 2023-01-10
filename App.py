#Library
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
import subprocess
import sys

# Create Localhost to host website
st.set_page_config(page_title='Aplikasi IPM Sumbar',
                   page_icon=":bar_chart:",
                   layout='wide')

st.title("IPM Sumatera Barat 2022")
st.sidebar.success("Select a page above")

# selected = option_menu(
#     menu_title=None,
#     options=["UHH", "HLS", "RLS", "Perkapita"],
#     icons=['house', 'gear', 'book', 'envelope'],
#     menu_icon="cast",
#     default_index=0,
#     orientation='horizontal',
# )

# if selected == "UHH":
#     st.write("ini UHH")
#     subprocess.run(["python", f"{sys.executable}", "uhh.py"])








