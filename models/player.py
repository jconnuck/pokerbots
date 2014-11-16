class Player:
  def __init__(self, p_id, max_cards):
    self.id = p_id
    self.max_cards = max_cards
    self._cards = []
    self._money = 0

  def clear_hand(self):
    self._cards = []

  def set_hand(self, cards):
    if len(cards) > self.max_cards:
      raise Exception("Too many cards given")
    if any([not isinstance(x, Card) for x in cards]):
      raise Exception("Cards list contains non-cards")
    self._cards = cards

  def show_cards(self):
    return deepcopy(self._cards)

  def add_money(self, amount):
    if amount > 0:
      self._money += amount
