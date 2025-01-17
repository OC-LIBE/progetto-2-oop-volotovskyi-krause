import streamlit as st
from modules.card import Card
from modules.deck import Deck


st.set_page_config(
   layout="wide",
)
card_width=95



deck = Deck(1)
shuffled = False 


#st.markdown(f"## Deck created with {number_of_decks} deck/s")

#st.image([card.image for card in deck.cards], width=card_width)

#st.markdown("## Shuffling deck")
 

if st.button("Shuffle Deck"):
    if shuffled == False:
        deck.shuffle()
        shuffled = True
        st.success("Deck shuffled!")
    else:
        st.write("ok")

st.write(shuffled)





class Player:
    def __init__(self):
        self.score = 0
        self.handlist = []

    def hand(self):
        
        st.image([card.image for card in deck.cards], width=card_width)
        self.handlist = []
        length = 2
        for i in range(length):
            self.handlist.append(deck.cards[i])
        del deck.cards[:2]
        #st.image([card.image for card in self.hand], width=card_width)
        return self.handlist
    
    
    def calc_score(self):
        for i in self.handlist:
            obj = i
            a=(getattr(obj, 'rank'))
            self.score = self.score + a
        return self.score

class Dealer:
    def __init__(self):
        self.score = 0
        self.handlist = []




player = Player()
hand = player.hand()






#if st.button("button"):
    #hand = Player(2).hand()
    #st.image([card.image for card in hand], width=card_width)
    #st.write(hand)
    
   # for i in hand:
       # obj = i
        #st.write(getattr(obj, 'rank'))

    #for i in hand:
        
#taking card
if st.button("take card"):
    player.handlist.append(deck.cards[0])
    del deck.cards[:1]
    st.write(player.handlist)
    

st.image([card.image for card in player.handlist], width=card_width)

#score
plscore = player.calc_score()
st.markdown(f'Your score: {plscore} Dealer Score: ')
if plscore > 21:
    st.error('You lost')

#columns
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = st.columns(11, gap="small")
def col_insert(col_num):
    try:
        st.image(hand[col_num-1].image,width=card_width)
    except TypeError:
        print('')
    except IndexError:
        print('')

with col1:
    col_insert(1)
with col2:
    col_insert(2)
with col3:
    col_insert(3)
