import streamlit as st
from used_func import header
from validations import validate_email
import requests
from urlback import URL
from time import sleep
from used_func import login, split_strip
from consts import recipes_json

if "e_mail" not in st.session_state or "password" not in st.session_state:
    login()

logged = requests.get(f"{URL}/login", auth=(st.session_state.e_mail, st.session_state.password)).json()["data"]

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.write("")
header()
st.subheader('Cadastre a Receita:')
st.write("")

recipes = requests.get(f"{URL}/recipes", auth=(st.session_state.e_mail, st.session_state.password))
if recipes.status_code == 200:
    recipes = recipes.json()

recipes_json['receita'] = st.text_input('Receita', placeholder='receita')

categorias = requests.get(f"{URL}/recipes/categorias", auth=(st.session_state.e_mail, st.session_state.password))
recipes_json['categorias'] = st.multiselect('Categorias', options=categorias.json()['data']+['Outros'], placeholder='Categorias')
if 'Outros' in recipes_json['categorias']:
    recipes_json['categorias'] += split_strip(st.text_input('Outras categorias: (se for mais de uma divida-as por vígula (","))'))

recipes_json

c1,_,c3 = st.columns((0.4,1,0.6))
if c1.button('Cadastrar'):
    add = requests.post(f"{URL}/recipes", json=recipes_json, auth=(st.session_state.e_mail, st.session_state.password))
    add.status_code
    if add.status_code == 201:
        st.success('Cadastro feito com sucesso!')
        sleep(1)
        st.switch_page('app.py')
    elif add.status_code == 409:
        st.error(add.json()['message'])
    else:
        st.error('Necessária autorização do Administrador.')