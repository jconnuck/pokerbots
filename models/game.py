class Game(object):
  def __init__(self, players, table, deck):
    self.players = players
    self.table = table
    self.deck = deck

  def start(self):
    pass
  # TODO: I want to put all (or at least as many as make sense) of the
  # game operational methods that the server API calls into this class