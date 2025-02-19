import streamlit as st
from modules.card import Card
from modules.deck import Deck
import base64
from login import username

try:
    st.set_page_config(
    layout="wide",
    )
except st.errors.StreamlitSetPageConfigMustBeFirstCommandError:
    st.write('')


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




card_width=95
card0 = Card(0,'Clubs')



class User():
    def __init__(self):
        self.name = username
        self.money = 2000

user = User()

st.header(f'Hello, {username}')
st.header(f'Balance: {user.money}$')

with st.popover("Bet"):
    option = st.selectbox("Choose your bet",(25,50,100,200,500,1000))
    if st.button('Confirm'):
        st.success('Success')



if 'deck' not in st.session_state:
    st.session_state.deck = Deck(1)
    st.session_state.deck.shuffle()
deck = st.session_state.deck

plscore = 0
dlscore = 0

class Game():
    def __init__(self):
        self.deck = deck

    
    def result(self):
        if plscore > dlscore:
            st.success('You won')
            if 'winlose' not in st.session_state:
                st.session_state.winlose = True
                user.money = user.money + option

        elif dlscore>plscore:
            st.error('You lost')
            if 'winlose' not in st.session_state:
                st.session_state.winlose = True
                user.money = user.money - option

        elif plscore == dlscore:
            st.info('Draw')
            if 'winlose' not in st.session_state:
                st.session_state.winlose = True
                

game = Game()

#st.image([card.image for card in deck.cards], width=card_width)


class Player:
    def __init__(self):
        self.score = 0
        self.handlist = []
        if 'handlist' not in st.session_state:
            st.session_state.handlist = self.handlist
            self.hand_ap()
            self.hand_ap()
            #st.write('player')
        self.handf = st.session_state.handlist
    

    

    def hand_ap(self):
        drawn_card = deck.draw()
        self.handlist.append(drawn_card)
        return self.handlist
    
    
    def calc_score(self):  
        self.score = sum(getattr(card, 'rank') for card in self.handf)
        
        return self.score


player = Player()


class Dealer(Player):
    def __init__(self):
        self.score = 0
        self.handlist = []
        self.exlist = []
        if 'exlist' not in st.session_state:
            st.session_state.exlist = self.exlist
            self.exlist.append(deck.cards[1])
        self.stexlist = st.session_state.exlist
        if 'handlist1' not in st.session_state:
            st.session_state.handlist1 = self.handlist
            self.hand_ap()
            self.hand_ap()
        self.handf = st.session_state.handlist1
        try:
            if 'stand' not in st.session_state:
                del self.handf[1]
        except IndexError:
            st.write('')

        if 'stand' not in st.session_state:
            self.handf.append(card0)


    def back_card(self):
        if 'stand' in st.session_state:
            self.handf.append(self.stexlist[0])
            self.handf.remove(card0)
        
    

    def take_card(self):
        try:
            if 'stand'in st.session_state:
                self.calc_score()
                while self.score <= 16:
                    self.handf.append(deck.cards[0])
                    self.hand_ap()
                    self.calc_score()
                if self.score >= 19:
                    st.write('')
        except IndexError:
            st.write('')
                



dealer = Dealer()





#Game Buttons
if 'stand' not in st.session_state:
    if 'winlose' not in st.session_state:
        if st.button("Hit"):
            player.handf.append(deck.cards[0])
            player.hand_ap()
            #st.write(player.handf)


if 'winlose' not in st.session_state:   
    if st.button('Stand'):
        if 'stand' not in st.session_state:
            st.session_state.stand = True
            dealer.back_card()
            dealer.take_card()

    
#Immediate score counter
dlscore = dealer.calc_score()
plscore = player.calc_score()

if dlscore > 21 or plscore == 21:
    st.success('You won')
    if 'winlose' not in st.session_state:
        st.session_state.winlose = True
        user.money = user.money + option


if plscore > 21 or dlscore == 21:
    st.error('You lost')
    if 'winlose' not in st.session_state:
        st.session_state.winlose = True
        user.money = user.money - option


if 'stand' in st.session_state and 'winlose' not in st.session_state:
    game.result()


st.image([card.image for card in dealer.handf], width=card_width)
st.markdown(f'Dealer score: {dlscore}')
st.image([card.image for card in player.handf], width=card_width)     
st.markdown(f'Your score: {plscore}')



if 'winlose' in st.session_state:
    if st.button('New Game'):
        st.session_state.clear()
        st.rerun()
        


