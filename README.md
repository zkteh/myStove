# myStove
WOU-FYP
http://zkteh.ddns.net:55555

# This IoT will 
1. monitor the food temperature to know whether the stove is warming, cooling, heating or off.
2. alert user to go back to the cooking region with the help of PIR motion sensor

# Screnshots
1. This graph is populated using chart.js, flask for web hosting and sqlite3 for database

**Boiling** : the mlx_object temperature is fluctuating due to sensor miss-reading of the water vapour(steam)
![Boiling](/screenshots/boiling.png)

**Heating** : the mlx sensor reading is quite steady when there is no obstruction (boiling steam)
![Heating](/screenshots/heating.png)


# Hardware 
1. Non Contact Infrared Thermometer MLX90614 Breakout Board – GY-906    **RM24.90**
https://shopee.com.my/GY-906-MLX90614-MLX90614ESF-Non-Contact-Infrared-Temperature-Sensor-Module-i.33091591.1975305507

2. Low Cost PIR sensor Module                                           **RM5.00**
(https://my.cytron.io/p-low-cost-pir-sensor-module)                                     

3. Raspberry Pi 4 Model B - 1GB                                         **RM142.20**
https://my.cytron.io/p-raspberry-pi-4-model-b-1gb

4. Official RPi 15W (5V/3A) PSU USB C UK Plug-Black                     **RM28.00**
https://my.cytron.io/p-official-rpi-15w-5v-3a-psu-usb-c-uk-plug-black

Total Cost                                                              **RM200.10**


# Limitation
1. pan tempearture is impossible due to low sensitivity of the OEM brand MLX90614 sensor 
2. food temperature is not accurate due to same reason as above
3. only works for one pan
4. user is not allowed to cover the pan with lid

# Things I learnt
1. Python doesn't like inconsitently mixed tabs and spaces for indentation, use VScode to convert indentation into tabs/spaces
https://blender.stackexchange.com/questions/44364/how-to-prevent-indentation-errors
2. ps -aux , kill -9 <PID>
