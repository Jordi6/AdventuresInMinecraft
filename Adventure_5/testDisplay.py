#!/usr/bin/env python2.7

# Adventure 5
# 7-segment LED


import anyio.GPIO as GPIO

LED_PINS = [7,6,14,16,10,8,9,15] # order important

GPIO.setmode(GPIO.BCM)

ON = True

for g in LED_PINS:
	GPIO.setup(g, GPIO.OUT)

pattern = [True, True, True, True, True, True, True, False] #ABCDEFG (no Decimal Point)

for g in range(8):

	if pattern[g]:

		GPIO.output(LED_PINS[g], ON)
	else:

		GPIO.output(LED_PINS[g], not ON)

raw_input("finished?")

GPIO.cleanup()

# END

