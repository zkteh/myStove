import sqlite3
import board
import busio as io
import adafruit_mlx90614
import time
import random 


dbname='sensorsData.db'
sampleFreq = 1*60 # time in seconds ==> Sample each 1 min

# get data from DHT sensor
def getMLXdata():	
    i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
    mlx = adafruit_mlx90614.MLX90614(i2c)
            
    if mlx is not None:
        ds18b20 = round(random.uniform(25.0, 35.0), 2)   #randome for DS18B20 for graph purpose 
        mlx_ambient = round(mlx.ambient_temperature, 2)
        mlx_object = round(mlx.object_temperature, 2)    
        logData (ds18b20, mlx_ambient, mlx_object)
        return ds18b20, mlx_ambient, mlx_object
    
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
            ds18b20, mlx_ambient, mlx_object = getMLXdata()
            logData (ds18b20, mlx_ambient, mlx_object)
            time.sleep(sampleFreq)
            
# ------------ Execute program 
main()
