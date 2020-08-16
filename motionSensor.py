from datetime import datetime
import time

from gpiozero import MotionSensor
motion_counter = 0

#import socketio

#sio = socketio.Client()


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/home/pi/Sensors_Database/MLXWebServer/mystove-79717-firebase-adminsdk-c9gn5-acd851d033.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

pir = MotionSensor(23)        
print("Waiting for PIR to settle")
pir.wait_for_no_motion()

def connect():
    global motion_counter
    while True:
        pir.wait_for_motion()
        if (pir.wait_for_motion()):     
            motion_counter += 1
            if motion_counter >= 3:
                 #sio.emit('humanBack', {'message': 'humanBack'})
                 print("Motion detected!", str(datetime.now()))  
                 db.collection(u'human_motion').add({
     
                 u'motion_detected': True,
                 u'timestamp': firestore.SERVER_TIMESTAMP
                 })   

                 motion_counter = 0            
        time.sleep(3) #to avoid multiple detection

#sio.connect('http://localhost:55555')
    
if __name__ == '__main__':
    connect()
