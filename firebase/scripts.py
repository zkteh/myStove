#https://medium.com/@varuldcube100/store-temperature-sensor-data-in-firebase-real-time-database-through-raspberry-pi-d16e2086718f
#This program will upload data to firebase in a loop(whileTrue)

import board
import busio as io
import adafruit_mlx90614

from w1thermsensor import W1ThermSensor
import time 

from firebase import firebase

# Global variables 
firebase = firebase.FirebaseApplication('https://mystove-24023.firebaseio.com/', None)



#script 
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)
sensor = W1ThermSensor() 

#ds18b20 readings
ds18b20_object = round(sensor.get_temperature(), 2)        

#mlx90614s readings
mlx_ambient = round(mlx.ambient_temperature, 2)
mlx_object = round(mlx.object_temperature, 2)     



##Date time formatting
dateString = '%d/%m/%Y %H:%M:%S'


#store the readings in variable and convert it into string and using firbase.post then data will be posted to databse of firebase 
while True:
    result = firebase.post('Project Name', {'cTemp':str(ds18b20_object),'ftemp':str(mlx_ambient), 'humidity':str(mlx_object)})
    print(result)
