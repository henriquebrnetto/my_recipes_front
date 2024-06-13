import streamlit as st
import streamlit_antd_components as sac
import requests
from urlback import URL


def pagina_login(profile= True):
    _,c2,_ = st.columns((0.3, 1, 0.3))

    c2.write("")
    #c2.image('images\JJ.png', width=400)
    sac.divider(align='center', color='green', key='key')

def header(profile=True):
    c5,_,c2,_,c4 = st.columns((0.2,0.8,3,0.8,0.2))

    c2.write("")
    sac.divider(align='center', color='grey', key='key')

    if profile:
        icon = '🏃‍♂️'
        pgn = 'pages/login.py'

        c5.write("")
        profile = c5.button(icon)
        if (profile):
            st.switch_page(pgn)


def clear_session_state(ignored=None):
    keys = list(st.session_state.keys())
    if len(ignored):
        for strt in ignored:
            keys.remove(strt)
    for key in keys:
        del st.session_state[key]

@st.experimental_dialog("Fazer Login")
def login():

    st.write("")
    st.subheader('Login:')
    st.session_state.e_mail = st.text_input('email:', key='email')
    st.session_state.password = st.text_input('Senha: ', type='password', key='senha')
    st.write("")

    col1, col2 = st.columns([1, 0.2])
    with col1:
        if st.button('cadastre-se', key='cadastre-se'):
            st.switch_page('pages/add_users.py')

    incorrect = False
    with col2:
        if st.button('Entrar', key='entrar'):
            if not requests.get(f"{URL}/login", auth=(st.session_state.e_mail, st.session_state.password)).json()["data"]:
                incorrect = True
            else:
                st.rerun()

    if incorrect:
        st.error('Username or password incorrect.')

    st.write("")

    _,c,_ = st.columns((1.3,1,1.3))

    if c.button("Esqueci minha senha"):
        st.switch_page("pages/rec_senha.py")

def split_strip(txt, sep=','):
    return [t.strip().lower() for t in txt.split(sep)]