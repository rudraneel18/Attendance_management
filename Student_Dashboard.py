from imports import *
import streamlit as st 
import hydralit as hy
from streamlit_option_menu import option_menu


def Home_page():
    title = st.markdown("<h1 style='text-align: center; color: #ffa31a;'>Student Dashboard</h1>", unsafe_allow_html=True)
    


def Edit_Details_page():
    pass


def Records_page():
    pass
navbar=option_menu(menu_title="Navbar",options=['Home','Edit Details','Records'],
                   menu_icon='cast',icons=['house','book','envelope'],default_index=0,orientation='horizontal')
if navbar=='Home':
    Home_page()
if navbar=='Edit Details':
    st.success('Edit Details')
if navbar=='Records':
    st.success('Attendance Records')
