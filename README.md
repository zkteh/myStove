# myStove
This is a final year project as part fulfillment for the degree in my university.

# This IoT will 
1. monitor the food temperature to know whether the stove is ON/OFF using MLX90614 sensor
2. motnior the human motion with PIR Motion Sensor
3. sends sensors data to Firestore
4. populate the data in a user dashboard with Flask
3. alert user to go back to the cooking region by sending Telegram message.


# Screnshots

High Level Architecture  

![image](https://user-images.githubusercontent.com/9402322/90789697-c8385f00-e339-11ea-8268-e0386d14418c.png)  


Flowchart  

![image](https://user-images.githubusercontent.com/9402322/90789738-d5ede480-e339-11ea-95a5-d24db8243122.png)  


This graph is populated using chart.js, flask for web hosting and Firestore for database  

![dashboard](https://user-images.githubusercontent.com/9402322/90789333-624bd780-e339-11ea-8fde-c701ac5c86e3.png)  


User will receive the Telegram reminder message after the countdown has ended.  

![telegram](https://user-images.githubusercontent.com/9402322/90789455-87d8e100-e339-11ea-98e5-d48703232641.png)  

Hardware implementation  

![wiringDiagram](https://user-images.githubusercontent.com/9402322/90790199-63c9cf80-e33a-11ea-9657-67805d88ec2c.png)  

![hardware](https://user-images.githubusercontent.com/9402322/90790296-7b08bd00-e33a-11ea-93d5-c9c3c807ca7e.png)  


# Hardware Cost
1. Non Contact Infrared Thermometer MLX90614 Breakout Board – GY-906    **RM24.90**
https://shopee.com.my/GY-906-MLX90614-MLX90614ESF-Non-Contact-Infrared-Temperature-Sensor-Module-i.33091591.1975305507

2. Low Cost PIR sensor Module                                           **RM5.00**
(https://my.cytron.io/p-low-cost-pir-sensor-module)                                     

3. Raspberry Pi 4 Model B - 1GB                                         **RM142.20**
https://my.cytron.io/p-raspberry-pi-4-model-b-1gb

4. Official RPi 15W (5V/3A) PSU USB C UK Plug-Black                     **RM28.00**
https://my.cytron.io/p-official-rpi-15w-5v-3a-psu-usb-c-uk-plug-black

Total Cost                                                              **RM200.10**


# Limitation / Project Scode
1. Heat sensor, MLX90614 need to be placed  quite near to the food, 50cm maximum of height
2. Real food temperature is not accurate due to wide field of Field Of View, 90 degree
3. Only works for one pan
4. User is not allowed to cover the pan with lid
5. Requires strong internet connection 
6. When user turn off the stove, they also have to remove the pan
7. Reminder time period & Telegram recipient user is code in static way




# Future Work
1. OpenCV for object detection, to make sure it is really human triggering the motion
2. Offiline support
3. Dynamic coding, allow user to change reminder period and Telegram message recepient user.
4. Enhance temperature logic, to able to sense whether the temperature is increasing or decreasing, so user still can leave the pan while the stove is OFF.
