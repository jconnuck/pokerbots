from enum import Enum

class Suit(Enum):
  DIAMONDS = 0
  SPADES = 1
  HEARTS = 2
  CLUBS = 3

  def __str__(self):
    return self.name