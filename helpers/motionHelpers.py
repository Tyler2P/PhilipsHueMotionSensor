from config import bridge_ip_address as bridgeIP
from config import lightsID
from helpers.hueHelpers import getAvailableLights, filterArray
from datetime import datetime

# Get the list of lights to control
lightArr = filterArray(getAvailableLights(bridgeIP), lightsID)

# When motion is no longer detected
def motionStopped():
	# If the time is over 10pm or below 9am, return
	if (datetime.now().hour > 22 or datetime.now().hour < 9):
		return
	# Loop through the list of filtered lights
	for light in lightArr:
		# Turn the light off
		light.on = False

# When motion is detected
def motionStarted():
	# If the time is over 10pm or below 9am, return
	if (datetime.now().hour > 22 or datetime.now().hour < 9):
		return
	# Loop through the list of filtered lights
	for light in lightArr:
		# Turn the light on
		light.on = True