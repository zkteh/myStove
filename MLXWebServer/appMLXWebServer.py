import json
import random
import time
from datetime import datetime
import sqlite3

from flask import Flask, Response, render_template, jsonify
from flask_socketio import *


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("mystove-79717-firebase-adminsdk-c9gn5-acd851d033.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })

# doc_ref = db.collection(u'users').document(u'aturing')
# doc_ref.set({
#     u'first': u'Alan',
#     u'middle': u'Mathison',
#     u'last': u'Turing',
#     u'born': 1912
# })

# users_ref = db.collection(u'users')
# docs = users_ref.stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')
  
  





application = Flask(__name__)
# socketio = SocketIO(application, cors_allowed_origins = '*')

# @socketio.on('connect')
# def test_connect():
#     print('Client connected')
#     #emit('my response', {'data': 'Connected'})

# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')

# @socketio.on('humanBack')
# def handle_message(message):
#     print('received message: ' + str(message), str(datetime.now()))
#     #emit('my_message1', message, broadcast=True)
#     emit('humanBack', {'message': 'humanBack'}, broadcast=True)


# @socketio.on('stoveON')
# def handle_message(message):
#     print('received message: ' + str(message), str(datetime.now()))
#     #emit('my_message1', message, broadcast=True)
#     emit('stoveON', {'message': 'stoveON'}, broadcast=True)


# @socketio.on('stoveOFF')
# def handle_message(message):
#     print('received message: ' + str(message), str(datetime.now()))
#     #emit('my_message1', message, broadcast=True)
#     emit('stoveOFF', {'message': 'stoveOFF'}, broadcast=True)        
  

   
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
    average = query_db("SELECT AVG (mlx_object) FROM MLX_data WHERE timestamp >= datetime('now', '-1 minute')")

    json_output =  my_query
    json_output2 =  average

    global data

    #combine two output into one JSON array
    both_json = {
        'c' : json_output,
        'd' : json_output2,
    }	
    
    return jsonify(both_json)

if __name__ == "__main__":
    #socketio.run(application, host='0.0.0.0', port=55555, debug=False)    
    application.run(host='0.0.0.0', port='55555', debug=False)

    
