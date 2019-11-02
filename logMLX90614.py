import sqlite3
import board
import busio as io
import adafruit_mlx90614
import time
import random 
from w1thermsensor import W1ThermSensor
from datetime import datetime

dbname='sensorsData.db'

def main():
    #mlx90614 calling function	
    i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
    mlx = adafruit_mlx90614.MLX90614(i2c)

    #ds18b20 calling function
    sensor = W1ThermSensor() 

    #initiate DB connection
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
            
    while mlx is not None:
        #ds18b20 readings
        ds18b20_object = round(sensor.get_temperature(), 2)        

        #mlx90614s readings
        mlx_ambient = round(mlx.ambient_temperature, 2)
        mlx_object = round(mlx.object_temperature, 2)        

        #DB Insert Data       
        curs.execute("INSERT INTO MLX_data VALUES(datetime('now'), ?, ?, ?)",(ds18b20_object, mlx_ambient, mlx_object))
        conn.commit()
        print (str(datetime.now()),"   Data committed: ", "ds18b20: " , ds18b20_object, "   mlx_ambient: " , mlx_ambient, "   mlx_object: " , mlx_object)
        #time.sleep(0.5)

    conn.close()    

main()        
