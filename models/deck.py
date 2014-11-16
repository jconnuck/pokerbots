from suit import Suit
from value import Value
from card import Card
from random import shuffle

class Deck(object):
  """docstring for Deck"""
  def __init__(self):
    super(Deck, self).__init__()
    self.cards = [Card(suit, value) for suit in Suit for value in Value]
    
  def shuffle(self):
    shuffle(self.cards)