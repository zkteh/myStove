import json
import random
import time
from datetime import datetime
import sqlite3

from flask import Flask, Response, render_template

application = Flask(__name__)
random.seed()  # Initialize the random number generator


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

	json_output = json.dumps(my_query)

	#print(json_output)
	return json_output


if __name__ == "__main__":
   application.run(host='0.0.0.0', port=55555, debug=False)
