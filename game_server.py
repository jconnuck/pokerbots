from flask import Flask, redirect, url_for, render_template
from controllers.table_controller import TableController
app = Flask(__name__)

app.debug = True

TableControllerSingleton = TableController()

@app.route('/')
def index():
  tables = TableControllerSingleton.get_tables()
  return render_template('index.html', tables=tables)

@app.route('/table/new')
def new_table():
  TableControllerSingleton.new_table()
  return redirect(url_for('index'))

@app.route('/table/join/<int:table_id>')
def join_table(table_id):
  return TableControllerSingleton.join_table(table_id)

@app.route('/table/game/new')
def new_game_at_table(table_id):
  return TableControllerSingleton.new_game_at_table(table_id)

if __name__ == "__main__":
	app.run()
