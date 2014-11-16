from copy import deepcopy
from random import shuffle

SUITS = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]

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


class Table:
  def __init__(self, deck, players, max_players):
    self.deck = deck
    self.max_players = max_players
    if isinstance(players, list):
      self._players = players
    else:
      self._players = []
    if len(players) > max_players:
      raise Exception("Too many players in list")
    num_players = 0
    for x in range(len(players)):
      if players[x] is not None:
        num_players += 1
    self.num_players = num_players

  def add_player(self, player):
    if not isinstance(player, Player):
      return -1
    if len(self._players == 0):
      self._players.append(player)
      self.num_players += 1
      return self.num_players
    for x in range(len(self._players)):
      if self._players[x] is None:
        self._players[x] = player
        self.num_players += 1
        return self.num_players
    if len(self._players) >= self.max_players:
      return -1
    else:
      self._players.append(player)
      self.num_players += 1
      return self.num_players

  def remove_player(self, p_id):
    for x in range(len(self._players)):
      if self._players[x] is not None:
        if self._players[x].p_id == p_id:
          self._players[x] = None
          self.num_players -= 1
          return self.num_players
    return -1


class Game:
  def __init__(self, players, table, deck):
    self.players = players
    self.table = table
    self.deck = deck

  def start(self):
    pass
  # TODO: I want to put all (or at least as many as make sense) of the
  # game operational methods that the server API calls into this class

class TexasHoldEm(Game):
  def __init__(self, players):
    self.MAX_CARDS = 2
    self.MIN_CARDS = 0
    self
    deck = create_standard_deck()
    table = Table(deck, players, self.)
    super(players, )


def create_standard_deck():
  deck = []
  for suit in SUITS:
    for value in range(1,14):
      deck.append(Card(suit, value))
  shuffle(deck)
  return deck


# t = Table([])
# for deck in t._decks:
#   for card in deck:
#     print card
p = Player(1, 2)
p.set_hand([Card(SUITS[0], 1), Card(SUITS[1], 1)])
print p.show_cards()