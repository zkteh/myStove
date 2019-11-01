#  Designed specifically to work with the MLX90614 sensors in the
#  adafruit shop
#  ----> https://www.adafruit.com/product/1747
#  ----> https://www.adafruit.com/product/1748
#
#  These sensors use I2C to communicate, 2 pins are required to
#  interface Adafruit invests time and resources providing this open
#  source code,
#  please support Adafruit and open-source hardware by purchasing
#  products from Adafruit!

#github link 
#------>https://github.com/adafruit/Adafruit_CircuitPython_MLX90614

import board
import busio as io
import adafruit_mlx90614
import time

# the mlx90614 must be run at 100k [normal speed]
# i2c default mode is is 400k [full speed]
# the mlx90614 will not appear at the default 400k speed
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

# temperature results in celsius
while True:
    print("Ambent Temp: ", "%.2f" % mlx.ambient_temperature)
    print("Object Temp: ", "%.2f" % mlx.object_temperature, "\n")
    time.sleep(1) //delay 1 second 
