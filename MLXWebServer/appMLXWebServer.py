import json
import random
import time
from datetime import datetime
import sqlite3

from flask import Flask, Response, render_template, jsonify

application = Flask(__name__)

@application.route('/')
def index():
	return render_template('index.html')

@application.route('/data')
def chart_data():
	def db(database_name='../sensorsData.db'):
		return sqlite3.connect(database=database_name)

	def query_db(query, args=(), one=False):
		cur = db().execute(query, args)
		rv = cur.fetchall()
		cur.close()
		return (rv[0] if rv else None) if one else rv

	my_query = query_db("SELECT * FROM MLX_data ORDER BY timestamp DESC LIMIT 1")
	my_query2 = query_db("SELECT AVG (mlx_object) FROM MLX_data WHERE timestamp >= datetime('now', '-1 minute')")

	json_output =  my_query
	json_output2 =  my_query2

	print(json_output2)

	#combine two output into one JSON array
	both_json = {
		'c' : json_output,
		'd' : json_output2
	}	

	#Creates a Response with the JSON representation 
	#Expected ouput :-
	# {'c': [{'timestamp': '2019-11-09 09:35:50', 'ds18b20': 27.12, 'mlx_ambient': 31.53, 'mlx_object': 30.59}], 'd': [{'AVG(mlx_object)': 30.552033898305083}]}

	# {"c":[["2019-11-09 16:08:51",45.81,30.83,37.21]],"d":[[37.46322033898304]]}

	
	return jsonify(both_json)

if __name__ == "__main__":	
	application.run(host='0.0.0.0', port=55555, debug=False)
