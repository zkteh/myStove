====================
Storing sensor data
===================

cd Sensor_Database\
python3 appMLXWebServer.py 

ModuleNotFoundError: No module named 'board'
sudo pip3 install adafruit-blinka

ModuleNotFoundError: No module named 'adafruit_mlx90614'
sudo pip3 install adafruit-circuitpython-mlx90614

ModuleNotFoundError: No module named 'w1thermsensor'
sudo pip3 install w1thermsensor


python3 logMLX90614.py

Done.


Result
python3 logMLX90614.py 
2020-05-28 11:51:46.421234    Data committed:  ds18b20:  30.94    mlx_ambient:  32.57    mlx_object:  32.33
2020-05-28 11:51:50.452678    Data committed:  ds18b20:  31.0    mlx_ambient:  32.59    mlx_object:  32.33


========
WebSever
========

cd Sensor_Database\MLXWebServer\

python3 appMLXWebServer.py 


Result 
python3 appMLXWebServer.py 
 * Serving Flask app "appMLXWebServer" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:55555/ (Press CTRL+C to quit)
192.168.1.140 - - [28/May/2020 11:52:47] "GET / HTTP/1.1" 200 -
192.168.1.140 - - [28/May/2020 11:52:48] "GET /favicon.ico HTTP/1.1" 404 -
192.168.1.140 - - [28/May/2020 11:52:51] "GET /data HTTP/1.1" 200 -
