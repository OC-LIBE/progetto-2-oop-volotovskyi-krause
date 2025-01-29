import streamlit as st
import base64
from modules.card import Card
from modules.deck import Deck
from app import Player
from app import Dealer
from app import Game

deck = Deck(1)
player = Player()
dealer = Dealer()

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



#Game Buttons
#if 'stand' not in st.session_state:
    #if st.button("Hit"):
        #player.handf.append(deck.cards[0])
        #player.hand_ap()
        #st.write(player.handf)
    
#if st.button('Stand'):
    #if 'stand' not in st.session_state:
       # st.session_state.stand = True
        #dealer.take_card()