import uuid

class Table(object):
  """Table represents a group of players who play one or more rounds of poker."""

  def __init__(self):
    super(Table, self).__init__()
    self.id = uuid.uuid4()
    self.players = []
    
  def get_id_as_int(self):
    return self.id.int
    