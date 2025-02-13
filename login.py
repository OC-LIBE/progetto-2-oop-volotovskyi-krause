import streamlit as st
import json
import os


json_file = "accounts.json"

if os.path.exists(json_file):
    with open(json_file, "r") as infile:
        try:
            existing_data = json.load(infile)
        except json.JSONDecodeError:
            existing_data = {}  # If the file is empty or corrupted, start fresh
else:
    existing_data = {}


if "dicl" not in st.session_state:
    st.session_state.dicl = existing_data
diclist = st.session_state.dicl

with st.popover('Sign in'):
    login = st.text_input('Login')
    password = st.text_input('Password')
    if st.button('Sign in'):
        for key, value in diclist.items():
            if login == key and password == value:
                st.success('You successfully logined!')
                st.switch_page("app.py")
            else:
                st.error('Wrong Login/Password')
        
with st.popover('New Account'):
    new_login = st.text_input('','Login1')
    new_password = st.text_input('','Password2')
    
    if st.button('Register'):
        dic = {new_login: new_password}
        diclist.update(dic.copy())
        st.success('You Cretaed an Account')


with open(json_file, "w") as outfile:
    json.dump(diclist, outfile)
outfile.close()

st.write(diclist)
