import sqlite3
import board
import busio as io
import adafruit_mlx90614
import time
import random 
from w1thermsensor import W1ThermSensor


dbname='sensorsData.db'
sampleFreq = 1 # time in seconds ==> Sample each 1 min

# get data from DHT sensor
def getMLXdata():
    #mlx90614 calling function	
    i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
    mlx = adafruit_mlx90614.MLX90614(i2c)

    #ds18b20 calling function
    ds18b20_sensor = W1ThermSensor()
    ds18b20_object = ds18b20_sensor.get_temperature()
            
    if mlx and ds18b20_object is not None:     
        #ds18b20       
        ds18b20_object = round(ds18b20_object, 2)
        #mlx90614s
        mlx_ambient = round(mlx.ambient_temperature, 2)
        mlx_object = round(mlx.object_temperature, 2)    
        #logData
        logData (ds18b20_object, mlx_ambient, mlx_object)
        return ds18b20_object, mlx_ambient, mlx_object
    
# log sensor data on database
def logData (ds18b20, mlx_ambient, mlx_object):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO MLX_data VALUES(datetime('now'), ?, ?, ?)",(ds18b20, mlx_ambient, mlx_object))
    conn.commit()
    conn.close()

# main function
def main():
	while True:
            #print (getMLXdata())            
            ds18b20, mlx_ambient, mlx_object = getMLXdata()          
            logData (ds18b20, mlx_ambient, mlx_object)
            time.sleep(sampleFreq)
            
# ------------ Execute program 
main()
