# OLD
# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software
# NEW (Get the temperature from your w1 therm sensor in a single line of code!)
# https://github.com/timofurrer/w1thermsensor


# Import Libraries
import os
import glob
import time
from datetime import datetime
 
# Initialize the GPIO Pins
os.system('modprobe w1-gpio')  # Turns on the GPIO module
os.system('modprobe w1-therm') # Turns on the Temperature module
 
# Finds the correct device file that holds the temperature data
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
# A function that reads the sensors data
def read_temp_raw():
  f = open(device_file, 'r') # Opens the temperature device file
  lines = f.readlines() # Returns the text
  f.close()
  return lines
 
# Convert the value of the sensor into a temperature
def read_temp():
  lines = read_temp_raw() # Read the temperature 'device file'
 
  # While the first line does not contain 'YES', wait for 0.2s
  # and then read the device file again.
  while lines[0].strip()[-3:] != 'YES':
    time.sleep(0.2)
    lines = read_temp_raw()
 
  # Look for the position of the '=' in the second line of the
  # device file.
  equals_pos = lines[1].find('t=')
 
  # If the '=' is found, convert the rest of the line after the
  # '=' into degrees Celsius, then degrees Fahrenheit
  if equals_pos != -1:
    temp_string = lines[1][equals_pos+2:]
    temp_c = float(temp_string) / 1000.0
    temp_f = temp_c * 9.0 / 5.0 + 32.0

    #store data into a log file with timestamp
    f = open("/var/log/ds18b20.log", 'a')
    now = datetime.now()
    d  = now.strftime("%Y-%m-%d_%H:%M:%S")
    f.write(str(d) + " " +  str(float(temp_string)) +  "\n")
    f.close()

    return temp_c, temp_f
 
# Print out the temperature until the program is stopped.
while True:
  print(read_temp())  
  time.sleep(1)
