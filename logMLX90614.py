import board
import busio as io
import adafruit_mlx90614
import time
from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def main():
    #mlx90614 calling function	
    i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
    mlx = adafruit_mlx90614.MLX90614(i2c)

    while mlx is not None:
        
        #mlx90614s readings
        mlx_ambient = round(mlx.ambient_temperature, 2)
        mlx_object = round(mlx.object_temperature, 2)
            
        print ("mlx_ambient: " , mlx_ambient, "   mlx_object: " , mlx_object, "  " , str(datetime.now()))
        
        #save sensor data to firestore
        db.collection('heat_sensor').add({
            'mlx_ambient': mlx_ambient,
            'mlx_object': mlx_object,
            'timestamp': firestore.SERVER_TIMESTAMP
        })    
        
        #store data every 3 seconds
        time.sleep(3) 

if __name__ == '__main__':
    main()