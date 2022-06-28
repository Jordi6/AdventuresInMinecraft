#!/usr/bin/env python2.7

# Adventure 5
# we are trying to connect the arduino to our minecraft world

import mcpi.minecraft as minecraft
import mcpi.block as block

import time
import anyio.GPIO as GPIO

# getting entity/player id
mc = minecraft.Minecraft.create()
playerId = mc.getPlayerEntityId("TonyStarkJ6")

# mat home location
HOME_X = -19
HOME_Y = 71
HOME_Z = -57

mc.setBlock(HOME_X, HOME_Y, HOME_Z, block.WOOL.id, 15)


# arduino set up
LED = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)


# def to make led flash
def flash(t):
    GPIO.output(LED, True)
    time.sleep(t)
    GPIO.output(LED, False)
    time.sleep(t)


try:
    while True:
        pos = mc.entity.getTilePos(playerId)
        if pos.x == HOME_X and pos.z == HOME_Z:
            flash(0.5)
            print("flash")
finally:
    GPIO.cleanup()            
