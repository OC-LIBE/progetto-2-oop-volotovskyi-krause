import streamlit as st
import json
import os
from time import sleep
from login import existing_data
from navigation import make_sidebar

make_sidebar()

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


json_balance = "balance.json"
if os.path.exists(json_balance):
    with open(json_balance, "r") as infile_b:
        try:
            existing_data_b = json.load(infile_b)
        except json.JSONDecodeError:
            existing_data_b = {} 
else:
    existing_data_b = {}

if "dicb" not in st.session_state:
     st.session_state.dicb = existing_data_b
diclist_b = st.session_state.dicb

st.title("Welcome to BlackJack")

st.write("Create your account.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Create account", type="primary"):
    dic = {username: password}
    diclist.update(dic.copy())
    dic_balance = {username: 2000}
    diclist_b.update(dic_balance.copy())
    st.session_state.logged_in = True
    st.success("Account successfully created!")
    sleep(0.3)
    st.switch_page("login.py")

with open(json_file, "w") as outfile:
    json.dump(diclist, outfile)
outfile.close()

with open(json_balance, "w") as outfile_b:
    json.dump(diclist_b, outfile_b)
outfile_b.close()