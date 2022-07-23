from config import bridge_ip_address as bridgeIP
from config import lightsID, pir_port
from helpers.hueHelpers import connectBridge
from helpers.motionHelpers import motionStarted, motionStopped

from gpiozero import MotionSensor

# Define which data port the motion sensor is on
pir = MotionSensor(pir_port)

# Connect to the bridge
connectBridge(bridgeIP)

while True:
	# Wait for there to be motion in the room
	pir.wait_for_motion()
	# Call the motion started function
	motionStarted()
	# Wait for the motion to no longer be detected
	pir.wait_for_no_motion()
	# Call the motion stopped function
	motionStopped()