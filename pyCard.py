import numpy as np
import random
# import namegenerator
# --------------------------
# print (namegenerator.gen())


class Card:
    """ CARD OBJECT FOR POKER SIMULATION"""

    def __init__(self, suit=0, rank=2):
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
    rank_l2st = [None, "A", "2", "3", "4", "5",
                 "6", "7", "8", "9", "10", "J", "Q", "K"]

    def title(self):
        title = str(Card.rank_names[self.rank]) + \
            ' of ' + str(Card.suit_names[self.suit])
        return title

    def __split2rows__(self):
        """ 
        FUNCTION RETURNS A LIST OF STRINGS WHERE EACH ELEMENT
        REPRESENTS A ROW OF A PLAYING CARD
        """
        pass
        suit = str(Card.suits_symbols[self.suit])
        rank = str(Card.rank_l2st[self.rank])
        # ten 10 rank is irregular thus below is req'd
        margin = ''
        if rank != '10':
            margin = ' '
    # briefly store building blocks under variables
        # t1tle =  str(Card.rank_names[self.rank]) + ' of ' + str(Card.suit_names[self.suit])
        top = '┌───┐'
        rank_left = '│{}{} │'.format(rank, margin)
        suit_center = '│ {} │'.format(suit)
        frame_lower = '│ {}{}│'.format(margin, rank)
        bottom = '└───┘'
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
        top = '┌───┐'
        rank_left = '│{}{} │'.format(rank, margin)
        suit_center = '│ {} │'.format(suit)
        frame_lower = '│ {}{}│'.format(margin, rank)
        bottom = '└───┘'
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

    def __lt__(self, other):
        """FIRST APPROACH: CHK THE SUITS; IF SAME:CHECK RANKS///SECOND APPROACH: TUPLES
        ///HOWEVER COMPARING CARDS INDVLY MAY NOT BE SO USEFUL IN POKER """
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False
        return self.rank < other.rank
        # self_tuple = self.suit, self.rank
        # other_tuple = other.suit, other.rank
        # return self_tuple < other_tuple

# ---------- TEST -----------------


def cardTester():
    pass
    first_card = Card(3, 3)
    print(first_card)
    second_card = Card(3, 2)
    print(second_card)
    print(second_card.__lt__(first_card))
    print(first_card.rank_names)
    print(first_card.suit_names)
    return None
# ---------- DECK -----------------


class Deck():
    """ GENERATES FIFTY-TW0 CARDS RANDOM-UNIQUE """

    def __init__(self):
        self.cards = [
            Card(suit, rank) for suit in range(len(Card.suit_l1st)) for rank in range(1, len(Card.rank_l1st))
        ]

    def __str__(self):
        return '\n'.join([
            str(card) for card in self.cards
        ])

    def to_l1st(self):
        """
        JUST TO MAKE SURE OUR DECK OBJECT IS ITERABLE
        """
        get4_list = [card
                     for card in self.cards
                     ]
        return get4_list

    def shuffle(self):
        """
        SHUFFLE B4 BURN-N-TURN
        """
        random.shuffle(self.cards)

    play3r_names = [
        'Attila',
        'Bob',
        'Codie',
        'Daniel',
        'Erce',
        'Funk'
    ]
    play3r_hands = [

    ]

    # def table4SixPlz(self):
    #     """
    #     SIMULATES A SIX PLAYER TABLE BRIEFLY FOR SIMULATION POPULATION
    #     """

    def test_0utput(self):
        """
        THIS IS A FUNCTION PRINTS OUT 10 HANDS 50 CARDS WITH ASCII-CHARACTERS
        """
        # create a string
        out = ''
        start = 0
        br3ak = 5
        s3lf = self.to_l1st()
        sample_card = Card()
        while br3ak < len(s3lf):
            pass
            for n in range(len(sample_card.__split2rows__())):
                for kart in s3lf[start:br3ak]:
                    out += kart.__split2rows__()[n]
                out += '\n'
            start = br3ak
            br3ak += 5
        print(out)
        return out

    # -------------------HAND-----------------------
    def add_card(self, card):
        """

        """
        pass
        self.cards.append(card)

    def pop_card(self, i=0):
        """Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def move_cards(self, hand, num):
        """
        Moves the given number of cards from the deck into the Hand.
        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())
    # -------------------------
    
class Hand(Deck):
    """
    INHERIT FROM DECK SO  ALL METHODS AVLBLE
    """

    def __init__(self, label, play3r_name='playerstr'+str(random.randint(0, 99))
                 ):
        self.label = label
        self.cards = []
        self.play3r_name = ''

    def __str__(self):
        """
        THIS IS A FUNCTION PRINTS OUT ALL CARDS IN HAND BY ILLSTRTN 
        WITH ASCII-CHARACTERS
        """
        # create a string
        out = ''
        s3lf = self.to_l1st()
        sample_card = Card()
        for n in range(len(sample_card.__split2rows__())):
            for kart in s3lf:
                out += kart.__split2rows__()[n]
            out += '\n'
        # print(out)
        return(out)
# -----------------------
play3r_names=[
            'Attila',
            'Bob',
            'Codie',
            'Daniel',
            'Erce',
            'Funky'
            ]

def dealFor6Players(self,
                        play3r_names=[
            'Attila',
            'Bob',
            'Codie',
            'Daniel',
            'Erce',
            'Funky'
            ],
            play3r_hands=[
                Hand(name) for name in play3r_names
                ]
                ):
        """
        POKER TABLE FOR SIX PLAYERS
        """
        pass
        self.shuffle()
        play3r_index = [
            str(integer) for integer in np.arange(len(play3r_names))
        ]
        print(play3r_index)
        print(play3r_hands)
        x = range(5)
        for n in x:
            for hand in play3r_hands:
                self.move_cards(hand, 1)
                print(hand)

            for hand in play3r_hands:
                print(hand)


class Hand(Deck):
    """
    INHERIT FROM DECK SO  ALL METHODS AVLBLE
    """

    def __init__(self, label, play3r_name='playerstr'+str(random.randint(0, 99))
                 ):
        self.label = label
        self.cards = []
        self.play3r_name = ''

    def __str__(self):
        """
        THIS IS A FUNCTION PRINTS OUT ALL CARDS IN HAND BY ILLSTRTN 
        WITH ASCII-CHARACTERS
        """
        # create a string
        out = ''
        s3lf = self.to_l1st()
        sample_card = Card()
        for n in range(len(sample_card.__split2rows__())):
            for kart in s3lf:
                out += kart.__split2rows__()[n]
            out += '\n'
        # print(out)
        return(out)

# class Player()


# ----------------------
if __name__ == "__main__":
    d3ste = Deck()
    d3ste.shuffle()
    # d3ste.show_ten_hands()
    # h4nd = Hand()
    # print(h4nd)
# ==========================================
    # play3r_names = [
    #         'Attila',
    #         'Bob',
    #         'Codie',
    #         'Daniel',
    #         'Erce',
    #         'Funky'
    #     ]
    # play3r_hands = [
    #     Hand(name) for name in  play3r_names
    # ]

    # x = range(5)
    # for n in x:
    #     for hand in play3r_hands:
    #         d3ste.move_cards( hand, 1)
    # print(hand)
    # for hand in play3r_hands:
    # print(hand)
# ==========================================
    d3ste.dealFor6Players()
