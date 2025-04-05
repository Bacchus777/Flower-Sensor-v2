Soil moisture sensor

![Flower-Sensor2](https://github.com/user-attachments/assets/eeecd25c-9b8a-444b-b915-c32054b1b50d)


The wireless soil moisture sensor is designed to work in Zigbee networks. Works in the Home Assistant Zigbee2MQTT automation system.

![image](https://github.com/user-attachments/assets/8ee8b440-00bb-44cc-b410-61f1b9f83288)


Instructions
To add a sensor, you need to press the Permit join button in Zigbee2MQTT , remove the cap (the top cover for the compact version of the sensor) from the sensor and pull out the strip that breaks the battery contact. The sensor will blink the LED and join the network. If the connection does not occur, you need to slide the board out of the case, press the button and hold it for about 7 seconds.

![image](https://github.com/user-attachments/assets/846c8639-2e32-41ea-a1c2-c87be6a39267)


Sensor data
Sensor functionality

The sensor transmits data on measured soil moisture to the zigbee network. The sensor also transmits data on temperature and illumination, as well as data on battery charge.

Main data transmitted:
Soil moisture (measured soil moisture value)
Battery (remaining charge in %)
Voltage (battery voltage in millivolts)

Additional transmitted data:
Temperature (measured temperature value)
Illuminance (raw measured illuminance)
Illuminance_lux (illuminance in lux)

Settings:
Interval (report sending frequency in minutes)
To set the interval, you need to set the selected value and press the button on the sensor so that it accepts this value.

Threshold (sensor response threshold)
The sensor can control another zigbee device directly. For example, it can be a signal lamp or even an irrigation system . You need to set a threshold value and press the button on the sensor. If the soil moisture falls below this value, the sensor will automatically send a command to the linked device.

Binding a device.

Device binding is configured in the Bind tab.

![image](https://github.com/user-attachments/assets/ba565678-4d02-4bea-857b-5a5b9e154d26)

To bind, you need to select Source Endpoint 1, select the device you want to bind to and the Endpoint to which the binding is performed. After that, press the Bind button and the button on the sensor. The setup is complete.
