import streamlit as st
import base64
from modules.card import Card
from modules.deck import Deck
import json


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(jpg_file):
    bin_str = get_base64(jpg_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('./images/tab.jpg')

dic = {}

with st.popover('Sign in'):
    login = st.text_input('Login')
    password = st.text_input('Password')
    
        
with st.popover('New Account'):
    new_login = st.text_input('','Login1')
    new_password = st.text_input('','Password2')
    if st.button('Register'):
        dic.update({new_login: new_password})
        json = json.dumps(dic)
        f = open("accounts.json","w")
        f.write(json)
        f.close()
        st.success('You Cretaed an Account')



st.write(dic)
