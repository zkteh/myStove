from datetime import datetime
import time

from gpiozero import MotionSensor
motion_counter = 0

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

pir = MotionSensor(23)      #PIR motion sensor is connected to Pin23     
print("Waiting for PIR to settle")
pir.wait_for_no_motion()    #When first powered on, the PIR motion sensor will trigger itself for several time, which is normal, 
                            #thus, we can call a wait_for_no_motion(), then only let the program continue to runs.

def connect():
    global motion_counter
    while True:
        pir.wait_for_motion()
        if (pir.wait_for_motion()):     
            motion_counter += 1
            if motion_counter >= 3:  #only store data if the motion has been triggered more than 3 times.               
                 print("Motion detected!", str(datetime.now()))  

                 db.collection('human_motion').add({    
                 'motion_detected': True,
                 'timestamp': firestore.SERVER_TIMESTAMP
                 })   
                 
                 motion_counter = 0        #reset the counter    
        time.sleep(3) #to avoid multiple detection

if __name__ == '__main__':
    connect()