"""
Digital Ready Summer 2024
Card Game Project

The card class is a representation of a card in a deck of cards.
"""
from rank import Rank
from suit import Suit
import random

class Card():
    def __init__(self, rank, suit):
        self.rank = rank.value
        self.suit = suit.value

    def __repr__(self):
        return f"{self.rank}{self.suit}"
    
    @staticmethod
    def new_deck():
        deck = []
        for rank in Rank:
            for suit in Suit:
                deck.append(Card(rank, suit))
        random.shuffle(deck)
        return deck
    
### Examples

# Making a new card
# card_1 = Card(Rank.print(card_1.rank)
# TEN, Suit.SPADES)
# card_2 = Card(Rank.TWO, Suit.DIAMONDS)
# card_3 = Card(Rank.THREE, Suit.CLUBS)
# card_4 = Card(Rank.FOUR, Suit.SPADES)

# Making a new deck
# deck = Card.new_deck()

# for card in deck:
    # print(card)

#playercard = input("Give me a card please")
#print("New card")



