#!/usr/bin/env python2.7

import mcpi.minecraft as minecraft
import mcpi.block as block
import time


mc = minecraft.Minecraft.create()

playerId = mc.getPlayerEntityId("TonyStarkJ6")

pos = mc.entity.getTilePos(playerId)

direction = mc.entity.getDirection(playerId)

# loop over the distance 
# BLOCKDISTANCE = 5

# get width to work !

for a in range(5,10):

	# instead of doing a cuboid do a for loop of space where I want to put

	x = round(pos.x + (direction.x * 5))
	# BLOCKDISTANCE + 1, distance go further
	y = round(pos.y + (direction.y * 5) + 1)
	z = round(pos.z + (direction.z * 5) + a)

	# BLOCKDISTANCE = BLOCKDISTANCE + 1
	
	mc.setBlock(x ,y, z ,block.DIAMOND_BLOCK)
	time.sleep(0.3)
	mc.setBlock(x,y,z,block.AIR)









