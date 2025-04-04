import streamlit as st
from time import sleep

def logout():
    del st.session_state['username']
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("login.py")

logo = ("images/icon.png")

def make_sidebar():
    with st.sidebar:
        st.title("BlackJack")
        st.write("")
        st.write("")

        
        st.logo(logo, size='large')

        if 'username' in st.session_state:
            
            st.write("")
            st.write("")

            if st.button("Log out"):
                    logout()
        
    


