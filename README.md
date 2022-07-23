# PhilipsHueMotionSensor
A simple script to connect a raspberry pi motion sensor to your Philips Hue smart lights

## Setup

1. Install the required dependancies
```
pip install -r requirements.txt
```

2. Change the config file for your needs
```py
# The IP address of your philips hue bridge
bridge_ip_address = ""
# List of lights this motion sensor controls
lightsID = []
```
