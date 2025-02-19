import streamlit as st
import json
import os
from navigation import make_sidebar
from time import sleep

st.set_page_config(
   layout="wide",
)

json_file = "accounts.json"

if os.path.exists(json_file):
    with open(json_file, "r") as infile:
        try:
            existing_data = json.load(infile)
        except json.JSONDecodeError:
            existing_data = {} 
else:
    existing_data = {}
if "dicl" not in st.session_state:
     st.session_state.dicl = existing_data
diclist = st.session_state.dicl


make_sidebar()


st.title("Welcome to BlackJack")

st.write("Please log in to continue (username `test`, password `test`).")

username = st.text_input("Username")
password = st.text_input("Password", type="password")


if st.button("Log in", type="primary"):
    for key, value in diclist.items():
            if username == key and password == value:
                st.session_state.logged_in = True
                st.session_state.username = username
                username = st.session_state.username
                st.success("Logged in successfully!")
                sleep(0.5)
                st.switch_page("pages/app.py")
    else:
        st.error("Incorrect username or password")

st.write('')
st.markdown("Don't have an account? Sign up!")
if st.button('Sign up'):
    sleep(0.5)
    st.switch_page("pages/sign_up.py")






        
        
    
        




