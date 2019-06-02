import numpy as np
import random
# --------------------------
class Card:
    """ CARD OBJECT FOR POKER SIMULATION"""
    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    suits_symbols = [
                '♣',
                '♦', 
                '♥', 
                '♠'
                ]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]
    suit_l1st = ["C", "D", "H", "S"]
    
    rank_l1st = [None, "A-", "2-", "3-", "4-", "5-", "6-", "7-", 
              "8-", "9-", "10", "J-", "Q-", "K-"]
    rank_l2st = [None, "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def title(self):
        title =  str(Card.rank_names[self.rank]) + ' of ' + str(Card.suit_names[self.suit])
        return title

    def __split2rows__(self):
        pass
        suit = str(Card.suits_symbols[self.suit])
        rank = str(Card.rank_l2st[self.rank])
        # ten 10 rank is irregular thus below is req'd
        margin = ''
        if rank != '10':
            margin = ' '
    # briefly store building blocks under variables
        # t1tle =  str(Card.rank_names[self.rank]) + ' of ' + str(Card.suit_names[self.suit])
        top =         '┌───┐'
        rank_left =   '│{}{} │'.format(rank, margin)  
        suit_center = '│ {} │'.format(suit)
        frame_lower = '│ {}{}│'.format(margin, rank)
        bottom =      '└───┘'
    # like a lego of strings
        str_list = [
            # t1tle, 
            # margin_top, 
            top,
            rank_left, 
            suit_center,
            frame_lower, 
            bottom
        ]

        return str_list  

    def __str__(self):
        pass
        suit = str(Card.suits_symbols[self.suit])
        rank = str(Card.rank_l2st[self.rank])
        # ten 10 rank is irregular thus below is req'd
        margin = ''
        if rank != '10':
            margin = ' '
    # briefly store building blocks under variables
        # t1tle =  str(Card.rank_names[self.rank]) + ' of ' + str(Card.suit_names[self.suit])
        top =         '┌───┐'
        rank_left =   '│{}{} │'.format(rank, margin)  
        suit_center = '│ {} │'.format(suit)
        frame_lower = '│ {}{}│'.format(margin, rank)
        bottom =      '└───┘'
    # like a lego of strings
        str_list = [
            # t1tle, 
            # margin_top, 
            top,
            rank_left, 
            suit_center,
            frame_lower, 
            bottom
        ]
# iterate through each element of the above list with new line as seperator
        return '\n'.join(str_list)

    def __lt__(self,other):
        """FIRST APPROACH: CHK THE SUITS; IF SAME:CHECK RANKS///SECOND APPROACH: TUPLES
        ///HOWEVER COMPARING CARDS INDVLY MAY NOT BE SO USEFUL IN POKER """
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False
        return self.rank < other.rank
        # self_tuple = self.suit, self.rank
        # other_tuple = other.suit, other.rank
        # return self_tuple < other_tuple

# ----------TEST-----------------
def cardTester():
    pass    
    first_card = Card(3, 3)
    print(first_card)
    second_card = Card(3,2)
    print(second_card)
    print(second_card.__lt__(first_card))
    print(first_card.rank_names)
    print(first_card.suit_names)
    return None
# -------------------------------------------------------------
# --------------------------- DECK  ---------------------------
# -------------------------------------------------------------
class Deck():
    """ GENERATES FIFTY-TW0 CARDS RANDOM-UNIQUE """
    def __init__(self):
        self.cards = [
            Card(suit,rank) for suit in range(len(Card.suit_l1st)) for rank in range(1,len(Card.rank_l1st))
            ]

    def __str__(self):
        return '\n'.join([
        str(card) for card in self.cards
        ])

    def to_l1st(self):
        get4_list = [ card
            for card in self.cards
        ]
        return get4_list

    def __de4l__(self):
        pass
        t3st_card = Card()    
        # create a string obj
        ind3x = np.arange(len(self.to_l1st()))
        np.random.shuffle(ind3x)
        print(ind3x)
        index = np.arange(len(self.to_l1st()))
        dict4now = dict(zip(ind3x, self.to_l1st()))
        out = ''
        start = 0
        br3ak = 5
        s3lf = self.to_l1st()
        np.random.shuffle(s3lf)
        while br3ak < len(s3lf):
            pass
            for n in range(len(t3st_card.__split2rows__())):
                for kart in s3lf[start:br3ak]:
                    out += kart.__split2rows__()[n]
                out += '\n'
            start = br3ak
            br3ak +=5
        print(out) 
        return out            

# ----------------------
# cardTester()
test_card = Card(3,1)
# print(test_card.__str__())
d3ste = Deck()
d3ste.__de4l__()