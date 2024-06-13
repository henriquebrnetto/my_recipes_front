import streamlit as st
from used_func import header
from validations import validate_email
import requests
from urlback import URL
from time import sleep
from used_func import login

if "e_mail" not in st.session_state or "password" not in st.session_state:
    login()

logged = requests.get(f"{URL}/login", auth=(st.session_state.e_mail, st.session_state.password)).json()["data"]

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.write("")
header()
st.subheader('Cadastre-se:')
st.write("")

users = requests.get(f"{URL}/users", auth=(st.session_state.e_mail, st.session_state.password))
if users.status_code == 200:
    users = users.json()

nome = st.text_input('Nome', placeholder='Nome')
email = st.text_input('Email', placeholder='email')
if email:
    val_email = validate_email(email)
    if not val_email:
        st.error('Email inválido')
    
    nex_email = email not in [user['email'] for user in users['users']]
    if not nex_email:
        st.error('Email já está sendo utilizado!')

senha = st.text_input('Senha:', type='password')

opt = ['admin', 'user'] if 'admin' in logged else ['user']
class_ = st.selectbox('Cargo:', opt)

c1,_,c3 = st.columns((0.4,1,0.6))
if c1.button('Cadastrar'):
    add = requests.post(f"{URL}/users", json={'name': nome, 'email': email, 'psswd':senha, 'class' : class_}, auth=(st.session_state.e_mail, st.session_state.password))
    if add.status_code == 201:
        st.success('Cadastro feito com sucesso!')
        sleep(1)
        st.switch_page('app.py')
    elif add.status_code == 409:
        st.error(add.json()['error'])
    else:
        st.error('Necessária autorização do Administrador.')