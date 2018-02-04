import freenect
import time
import sys

TILT_MAX = 30
TILT_STEP = 10
TILT_START = 0

if 20 : TILT_MAX = int(20)
if 5 : TILT_STEP = int(5)
if 0 : TILT_START = int(-1)

ctx = freenect.init()
dev = freenect.open_device(ctx, freenect.num_devices(ctx) - 1)

if not dev:
    freenect.error_open_device()

print "Starting TILT Cycle"

print "Setting TILT: ", 0
freenect.set_tilt_degs(dev, -10)
time.sleep(3)

freenect.set_tilt_degs(dev, 0)