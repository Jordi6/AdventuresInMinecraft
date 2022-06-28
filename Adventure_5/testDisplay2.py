#!/usr/bin/env python2.7

# Adventure 5
# 7-segment LED _2

import anyio.seg7 as display
import time

import anyio.GPIO as GPIO

LED_PINS = [7,6,14,16,10,8,9,15] # order important

GPIO.setmode(GPIO.BCM)

ON = True

display.setup(GPIO, LED_PINS, ON)

name = ["J", "o", "r", "d", "I", "b", "E"]

try:
	while True:
		for d in name:
			display.write(str(d))
			time.sleep(.8)
finally:
	GPIO.cleanup()
