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
            existing_data = {}  # If the file is empty or corrupted, start fresh
else:
    existing_data = {}




make_sidebar()


st.title("Welcome to BlackJack")

st.write("Please log in to continue (username `test`, password `test`).")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "test" and password == "test":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/app.py")
    else:
        st.error("Incorrect username or password")


# if "dicl" not in st.session_state:
#     st.session_state.dicl = existing_data
# diclist = st.session_state.dicl

# with st.popover('Sign in'):
#     login = st.text_input('Login')
#     password = st.text_input('Password')
#     if st.button('Sign in'):
#         for key, value in diclist.items():
#             if login == key and password == value:
#                 st.success('You successfully logined!')
#                 st.switch_page("app.py")
#             else:
#                 st.error('Wrong Login/Password')
        
# with st.popover('New Account'):
#     new_login = st.text_input('','Login1')
#     new_password = st.text_input('','Password2')
    
#     if st.button('Register'):
#         dic = {new_login: new_password}
#         diclist.update(dic.copy())
#         st.success('You Cretaed an Account')


# with open(json_file, "w") as outfile:
#     json.dump(diclist, outfile)
# outfile.close()

#st.write(diclist)
