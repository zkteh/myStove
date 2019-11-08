import json
import random
import time
from datetime import datetime
import sqlite3

from flask import Flask, Response, render_template

application = Flask(__name__)

@application.route('/')
def index():
	return render_template('index.html')

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
	my_query2 = query_db("SELECT AVG(mlx_object) FROM MLX_data WHERE timestamp >= datetime('now', '-1 minute')")

	json_output = json.dumps(my_query)	
	json_output2 = json.dumps(my_query2)	

	print(json_output) 	 #[{"timestamp": "2019-11-08 13:54:44", "ds18b20": 26.31, "mlx_ambient": 29.63, "mlx_object": 28.77}]
	print(json_output2)  #[{"AVG(mlx_object)": 28.775901639344255}]	

	return json_output

if __name__ == "__main__":	
	application.run(host='0.0.0.0', port=55555, debug=False)
