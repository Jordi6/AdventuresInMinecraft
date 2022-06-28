#!/usr/bin/env python2.7

# Adventure 5
# detonator button / 7-segment LED


import mcpi.minecraft as minecraft
import mcpi.block as block 
import time
import anyio.seg7 as display


import anyio.GPIO as GPIO


BUTTON = 4
LED_PINS = [7,6,14,16,10,8,9,15] # order important

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

ON = True

display.setup(GPIO, LED_PINS, ON)

mc = minecraft.Minecraft.create()

playerId = mc.getPlayerEntityId("TonyStarkJ6")


# drops a block of TNT to mark where the bomb will go off

# countds down to zero

# blows a big crater where the TNT block was

def bomb(x, y, z):
	mc.setBlock(x+1, y, z+1, block.TNT.id)
	for t in range(6):
		display.write(str(5-t))
		time.sleep(1)
	mc.postToChat("BANG!")
	mc.setBlocks(x-10, y-5, z-10, x+10, y+10, z+10, block.AIR.id)




try:
	while True:
		time.sleep(0.1)
		if GPIO.input(BUTTON) == False:
			pos = mc.entity.getTilePos(playerId)
			bomb(pos.x, pos.y, pos.z)
finally:
	GPIO.cleanup()