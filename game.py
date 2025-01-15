import streamlit as st
from modules.card import Card
from modules.deck import Deck

st.set_page_config(
   layout="wide",
)
card_width=95


number_of_decks = 1
deck = Deck(number_of_decks)


shuffle_button = st.button("Shuffle")
if shuffle_button:
    deck.shuffle()
st.image([card.image for card in deck.cards()], width=card_width)



class Player:
    def __init__(self, cards, score):
        self.cards = deck.cards[0]
        self.score = Card.rank(cards[0]) + Card.rank(cards[1])

# class dealer:

