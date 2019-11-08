import json
import random
import time
from datetime import datetime
import sqlite3

from flask import Flask, Response, render_template
from flask_socketio import SocketIO

application = Flask(__name__)
application.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(application, cors_allowed_origins = 'http://192.168.1.156:55555' )



@application.route('/')
def index():
	return render_template('index.html')

def background_thread():
	"""Example of how to send server generated events to clients."""
	count = 0
	while True:
		socketio.sleep(10)
		count += 1
		socketio.emit('my_response',
					{'data': 'Server generated event', 'count': count},
					namespace='/test')

@socketio.on('connect', namespace='/test')
def test_connect():
	global thread
	with thread_lock:
		if thread is None:
			thread = socketio.start_background_task(background_thread)
	emit('my_response', {'data': 'Connected', 'count': 0})

@application.route('/data')
def chart_data():
	def db(database_name='../sensorsData.db'):
		return sqlite3.connect(database=database_name)

	def query_db(query, args=(), one=False):
		cur = db().cursor()
		cur.execute(query, args)
		r = [dict((cur.description[i][0], value) \
				for i, value in enumerate(row)) for row in cur.fetchall()]
		cur.connection.close()
		return (r[0] if r else None) if one else r

	my_query = query_db("SELECT * FROM MLX_data ORDER BY timestamp DESC LIMIT 1")
	query3 = 8
	query2 = query_db("SELECT mlx_object FROM MLX_data WHERE timestamp >= datetime('now', '-1 minute')")

	json_output = json.dumps(my_query)
	#socketio.emit('average', query3)

	#print(json_output)
	#print("AVGAVGAVGA", query2)
	return json_output


if __name__ == "__main__":	
   application.run(host='0.0.0.0', port=55555, debug=False)
   socketio.run(application)
