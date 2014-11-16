class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    if suit not in SUITS or value < 1 or value > 13:
      raise Exception

  def __eq__(self, other_card):
    if type(other_card) is type(self.__class__):
      return self.value == other_card.value
    else:
      return False

  def __ne__(self, other_card):
    return not self.__eq__(other_card)

  def __str__(self):
    value = self.value
    if value == 1:
      value = "Ace"
    elif value == 11:
      value = "Jack"
    elif value == 12:
      value = "Queen"
    elif value == 13:
      value = "King"
    else:
      value = str(value)
    return_string = value + " of " + self.suit
    return return_string