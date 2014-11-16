from copy import deepcopy
from random import shuffle

SUITS = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]




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