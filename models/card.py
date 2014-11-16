from suit import Suit
from value import Value

class Card(object):
  def __init__(self, suit, value):
    if not isinstance(suit, Suit):  
      raise Exception("%s is not a valid Suit" % suit)
    if not isinstance(value, Value):
      raise Exception("%s is not a valid card Value" % value)
    self.suit = suit
    self.value = value

  def __eq__(self, other_card):
    if type(other_card) is type(self):
      return self.value == other_card.value
    else:
      raise Exception("Attempt to compare %s with %s" % (self.__class__, other_card.__class__))

  def __ne__(self, other_card):
    return not self.__eq__(other_card)

  def __str__(self):
    return "%s of %s" % (self.value, self.suit)