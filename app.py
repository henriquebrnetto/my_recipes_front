import streamlit as st
from used_func import header, login, clear_session_state
import requests
from urlback import URL
import streamlit_antd_components as sac


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

if "e_mail" not in st.session_state or "password" not in st.session_state:
    logged = False
else:
    logged = requests.get(f"{URL}/login", auth=(st.session_state.e_mail, st.session_state.password)).json()["data"]

c5,_,c2,_,c4 = st.columns((0.2,0.8,3,0.8,0.4))

c2.write("")
#c2.image('images\JJ.png', width=400)
sac.divider(align='center', color='grey', key='key')

if logged in ["user", "admin"]:

    icon = '🏃‍♂️'
    pgn = 'pages/login.py'

    c5.write("")
    c4.write("")

    if c5.button(icon):
        login()
    
    if logged == "admin":

        tab1, tab2, tab3, tab4 = st.tabs(['Sortear', 'Receitas', 'Usuários', 'Buscar'])

else:
    login()
