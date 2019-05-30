class Card:
    """ CARD OBJECT FOR POKER SIMULATION"""
    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank
    
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]
    suit_l1st = ["C", "D", "H", "S"]
    
    rank_l1st = [None, "A-", "2-", "3-", "4-", "5-", "6-", "7-", 
              "8-", "9-", "10", "J-", "Q-", "K-"]
    rank_l2st = [None, "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
       
    def __str__(self):
        top = str(Card.rank_l1st[self.rank]) + '-'*6 + str(Card.rank_l2st[self.rank])
        mid_full = '|' + '/'*7 +'|'
        mid = '|' *1
        margin_suit = '/'*2
        suit_row = mid + str(margin_suit) + '<' + str(Card.suit_l1st[self.suit]) + '>' + margin_suit + mid
        bottom = '| \n' *1 + '|'
        return top +'\n'+ mid_full + '\n' + suit_row

    def __lt__(self,other):
        """FIRST APPROACH: CHK THE SUITS; IF SAME:CHECK RANKS///SECOND APPROACH: TUPLES
        ///HOWEVER COMPARING CARDS INDVLY MAY NOT BE SO USEFUL IN POKER """
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False
        return self.rank < other.rank
        # self_tuple = self.suit, self.rank
        # other_tuple = other.suit, other.rank
        # return self_tuple < other_tuple

first_card = Card(3, 3)
print(first_card)
# second_card = Card(3,2)
# print(second_card)
# print(second_card.__lt__(first_card))

class Deck():
    """ GENERATES FIFTY-TW0 CARDS RANDOM-UNIQUE"""
    def __init__(self):
        self.cards = [
            Card(suit,rank) for suit in range(len(Card.suit_l1st)) for rank in range(len(Card.rank_l1st))
            ]

    def __str__(self):
        return '\n'.join([
        str(card) for card in self.cards
        ])
# ------------------------------------------
deste = Deck()
print(len(deste.cards))

