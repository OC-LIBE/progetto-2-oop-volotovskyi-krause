import streamlit as st
import json
import os
from time import sleep
from login import existing_data

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


st.title("Welcome to BlackJack")

st.write("Please sign up to continue (username `test`, password `test`).")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Create account", type="primary"):
    dic = {username: password}
    diclist.update(dic.copy())
    st.session_state.logged_in = True
    st.success("Account successfully created!")
    sleep(0.3)
    st.switch_page("login.py")

with open(json_file, "w") as outfile:
    json.dump(diclist, outfile)
outfile.close()