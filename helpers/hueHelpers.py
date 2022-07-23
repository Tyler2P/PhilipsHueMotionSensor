from phue import Bridge, PhueRequestTimeout
import logging as logger

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