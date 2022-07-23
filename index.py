from phue import Bridge, PhueRequestTimeout
from config import bridge_ip_address as bridgeIP
from config import lightsID
from gpiozero import MotionSensor
import logging as logger
from datetime import datetime

# Define which data port the motion sensor is on
pir = MotionSensor(10)

def connectBridge(ip):
	# Log basic information to the console
	logger.info("Connecting to the philips hue bridge")

	try:
		# Define the philips hue bridge
		b = Bridge(ip)
		# Connect to the bridge
		b.connect()
	except Exception as error:
		# Return with an error
		logger.error("Unable to connect to the philips hue bridge")
		raise error
	except RuntimeError as error:
		# Return with an error
		logger.error("Something went wrong whilst connecting to the philips hue bridge")
		raise error
	except PhueRequestTimeout as error:
		# Warn the client that a connection to the bridge was not successful
		logger.warning("Could not connect with the philips hue bridge, retrying")
		# Retry the connection
		connectBridge(ip)

def getAvailableLights(ip):
	# Define the philips hue bridge
	b = Bridge(ip)
	# Get a list of available lights by their name
	list = b.get_light_objects('name')
	# Return the list
	return list

def filterArray(arr, filter):
	filteredArr = []

	for x in arr:
		if x in filter:
			filteredArr.append(arr[x])

	return filteredArr

# Connect to the bridge
connectBridge(bridgeIP)

# Get the list of lights to control
lightArr = filterArray(getAvailableLights(bridgeIP), lightsID)

# When motion is no longer detected
def motionStopped():
	# If the time is over 10pm or below 7am, return
	if (datetime.now().hour > 22 or datetime.now().hour < 7):
		return
	# Loop through the list of filtered lights
	for light in lightArr:
		# Turn the light off
		light.on = False

# When motion is detected
def motionStarted():
	# If the time is over 10pm or below 7am, return
	if (datetime.now().hour > 22 or datetime.now().hour < 7):
		return
	# Loop through the list of filtered lights
	for light in lightArr:
		# Turn the light on
		light.on = True

while True:
	# Wait for there to be motion in the room
	pir.wait_for_motion()
	# Call the motion started function
	motionStarted()
	# Wait for the motion to no longer be detected
	pir.wait_for_no_motion()
	# Call the motion stopped function
	motionStopped()
