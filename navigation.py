import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

st.session_state.logged_in = False
def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        st.title("BlackJack")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", True):
            
            st.write("")
            st.write("")

            if st.button("Log out"):
                    logout()
        
        if st.session_state.get("logged_in", False):
            if get_current_page_name() == "app":
                st.switch_page("login.py")


def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("login.py")