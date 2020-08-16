import sqlite3
#dbname='sensorsData.db'

import board
import busio as io
import adafruit_mlx90614
import time
import random 
import json
from w1thermsensor import W1ThermSensor
from datetime import datetime


import socketio

sio = socketio.Client()



human_presence = 0

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/home/pi/Sensors_Database/MLXWebServer/mystove-79717-firebase-adminsdk-c9gn5-acd851d033.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def main():
    #mlx90614 calling function	
    i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
    mlx = adafruit_mlx90614.MLX90614(i2c)

    #ds18b20 calling function
    #sensor = W1ThermSensor() 

    #initiate DB connection
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()


    while mlx is not None:
        
        #ds18b20 readings
        ds18b20_object = 1 #round(sensor.get_temperature(), 2)        
        #human_presence = 0

        #mlx90614s readings
        mlx_ambient = round(mlx.ambient_temperature, 2)
        mlx_object = round(mlx.object_temperature, 2)
    
        #DB Insert Data       
        #curs.execute("INSERT INTO MLX_data VALUES(datetime('now'), ?, ?, ?, ?)",(ds18b20_object, mlx_ambient, mlx_object, human_presence ))

        #conn.commit()
        print (str(datetime.now()),"   Data committed: ", "ds18b20: " , ds18b20_object, "   mlx_ambient: " , mlx_ambient, "   mlx_object: " , mlx_object, "   human_presence: " , human_presence)

        #Heating up
        print (mlx_object - mlx_ambient)
        if (mlx_object - mlx_ambient > 3):
            print (">3 Heating up")
            sio.emit('stoveON', {'message': 'stoveON'})

        #Cool
        if (mlx_object - mlx_ambient < 1):
            print ("cold")
            sio.emit('stoveOFF', {'message': 'stoveOFF'})


        
        db.collection(u'heat_sensor').add({
            u'mlx_ambient': mlx_ambient,
            u'mlx_object': mlx_object,
            u'timestamp': firestore.SERVER_TIMESTAMP
        })    

   
     
        time.sleep(3) #to prevent over limit firebase free plan

    #conn.close()    

#main()        

#sio.connect('http://localhost:55555', namespaces='/chat')
    
if __name__ == '__main__':
    main()
