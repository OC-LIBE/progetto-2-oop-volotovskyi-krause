import streamlit as st
from modules.card import Card
from modules.deck import Deck

st.set_page_config(
   layout="wide",
)
card_width=95


number_of_decks = st.number_input("Number of decks", min_value=1, max_value=10, value=1)

deck = Deck(number_of_decks)


st.markdown(f"## Deck created with {number_of_decks} deck/s")

st.image([card.image for card in deck.cards], width=card_width)

st.markdown("## Shuffling deck")
shuffle_button = st.button("Shuffle")
if shuffle_button:
    deck.shuffle()
st.image([card.image for card in deck.cards], width=card_width)


class Player:
    def __init__(self, score):
        self.score = score
    

    def hand(self):
        self.hand1 = []
        length = 2
        for i in range(length):
            self.hand1.append(deck.cards[i])
        st.image([card.image for card in self.hand1], width=card_width)    
        return self.hand1


if st.button("button"):
    hand = Player(2).hand()
    st.write(hand)