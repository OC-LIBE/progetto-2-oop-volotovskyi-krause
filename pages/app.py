import streamlit as st
from modules.card import Card
from modules.deck import Deck
import base64
import json
import os
from navigation import make_sidebar

if "username" not in st.session_state:
    st.switch_page("login.py")
    
make_sidebar()

try:
    st.set_page_config(
    layout="wide",
    )
except st.errors.StreamlitSetPageConfigMustBeFirstCommandError:
    st.write('')


json_balance = "balance.json"
if os.path.exists(json_balance):
    with open(json_balance, "r") as infile_b:
        try:
            existing_data_b = json.load(infile_b)
        except json.JSONDecodeError:
            existing_data_b = {} 

if "dicb" not in st.session_state:
     st.session_state.dicb = existing_data_b
diclist_b = st.session_state.dicb

if 'username' in st.session_state:
    field_key = st.session_state.username

balance = diclist_b.get(field_key, 0)


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





with st.popover("Bet"):
    bet = st.selectbox("Choose your bet",(0,25,50,100,200,500,1000))
    if st.button('Confirm'):
        if 'bet' not in st.session_state:
            st.session_state.bet = bet
        st.success('Success')
if "bet" in st.session_state:
    if bet != st.session_state.bet:
        st.session_state.bet = bet
    st.write(f"Your current bet: {st.session_state.bet}")
    

try:
    option = st.session_state.bet
except AttributeError:
    option = 0

   


class User():
    def __init__(self):
        self.balance = balance
        if "username" in st.session_state:
            self.name = st.session_state.username

       
            
    
    
    def l_money(self):
        self.balance -= option
        return self.balance
        
    
    def w_money(self):
        self.balance += option
        return self.balance

user = User()

st.header(f'Hello, **{user.name}** 👋')
st.header(f'Balance: {user.balance}$')


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
                user.w_money()

        elif dlscore>plscore:
            st.error('You lost')
            if 'winlose' not in st.session_state:
                st.session_state.winlose = True
                user.l_money()

        elif plscore == dlscore:
            st.info('Draw')
            if 'winlose' not in st.session_state:
                st.session_state.winlose = True
                

game = Game()




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
        user.w_money()


if plscore > 21 or dlscore == 21:
    st.error('You lost')
    if 'winlose' not in st.session_state:
        st.session_state.winlose = True
        user.l_money()


if 'stand' in st.session_state and 'winlose' not in st.session_state:
    game.result()

col1, col2, col3 = st.columns(3)
with col2:
    st.image([card.image for card in dealer.handf], width=card_width)
    st.markdown(f'Dealer score: {dlscore}')
with col1:
    st.image([card.image for card in player.handf], width=card_width)     
    st.markdown(f'Your score: {plscore}')



balance_backup = st.session_state.get('balance', user.balance)
username_backup = st.session_state.get('username', user.name)
try:
    bet_backup = st.session_state.bet
except AttributeError:
    bet_backup = 0



if 'winlose' in st.session_state:

    diclist_b[field_key] = user.balance
    with open(json_balance, "w") as outfile_b:
        json.dump(diclist_b, outfile_b, indent=4)
    outfile_b.close()
    
   



    if st.button('New Game'):
        keys_to_keep = ['balance','username',"bet"]
        for key in list(st.session_state.keys()):
            if key not in keys_to_keep:
                del st.session_state[key]

        st.session_state.balance = balance_backup
        st.session_state.username = username_backup
        st.session_state.bet = bet_backup

        st.rerun()
        


