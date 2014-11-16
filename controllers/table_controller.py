from flask import Flask
from models.table import Table

app = Flask(__name__)

class TableController(object):
  def __init__(self):
    super(TableController, self).__init__()
    self.tables = {}

  def get_table_by_id(self, table_id):
    return self.tables[table_id]

  def get_tables(self):
    return self.tables.values()

  def new_table(self):
    table = Table();
    table_id = table.get_id_as_int()
    self.tables[table_id] = table
    return 'new table %d' % table.get_id_as_int()

  def join_table(self, table_id):
    table = self.get_table_by_id(table_id)
    return 'joined table %d' % table.get_id_as_int()
    