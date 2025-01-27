import streamlit as st
from modules.card import Card
from modules.deck import Deck


st.set_page_config(
   layout="wide",
)
card_width=95

if 'deck' not in st.session_state:
    st.session_state.deck = Deck(1)
    st.session_state.deck.shuffle()
deck = st.session_state.deck




#st.markdown(f"## Deck created with {number_of_decks} deck/s")

#st.image([card.image for card in deck.cards], width=card_width)

#st.markdown("## Shuffling deck")


class Game():
    def __init__(self):
        self.deck = deck
        


st.image([card.image for card in deck.cards], width=card_width)


class Player:
    def __init__(self):
        self.score = 0
        self.handlist = []
        if 'handlist' not in st.session_state:
            st.session_state.handlist = self.handlist
            self.hand_ap()
            self.hand_ap()
        self.handf = st.session_state.handlist
    

    def hand_ap(self):
        drawn_card = deck.draw()
        self.handlist.append(drawn_card)
        return self.handlist
    
    
    def calc_score(self):
        for i in self.handf:
            obj = i
            a=(getattr(obj, 'rank'))
            self.score = self.score + a
        return self.score

player = Player()


class HumanPlayer(Player):
    def __init__(self):
        self.name = "Player1"


#class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        self.handlist = []
        if 'handlist1' not in st.session_state:
            st.session_state.handlist = self.handlist
            self.hand_ap()
            self.hand_ap()
        self.hand1 = st.session_state.handlist



#dealer = Dealer()
#st.write(dealer.hand1)
#st.image([card.image for card in dealer.hand1], width=card_width)


if st.button("Hit"):
    player.handf.append(deck.cards[0])
    player.hand_ap()
    st.write(player.handf)
    

st.image([card.image for card in player.handf], width=card_width)

#score
plscore = player.calc_score()
st.markdown(f'Your score: {plscore} Dealer Score: ')
if plscore > 21:
    st.error('You lost')

#columns
#col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = st.columns(11, gap="small")
#def col_insert(col_num):
 #   try:
  #      st.image(player.handf[col_num-1].image,width=card_width)
 #   except TypeError:
  #      print('')
  #  except IndexError:
  #      print('')

#with col1:
  #  col_insert(1)
#with col2:
   # col_insert(2)
#with col3:
  #  col_insert(3)
#with col4:
   # col_insert(4)
#with col5:
   # col_insert(5)
#with col6:
   # col_insert(6)