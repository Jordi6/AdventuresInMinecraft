# Jordi Becerril Enriquez
# Adventure 4 
# find out if our player's feet are on the ground. 

import mcpi.minecraft as minecraft
import mcpi.block as block
import time 

mc = minecraft.Minecraft.create()

# set the global enity id of our player. 
playerId = mc.getPlayerEntityId("TonyStarkJ6")


# define our function
def safeFeet():
	pos = mc.entity.getTilePos(playerId)
	b = mc.getBlock(pos.x, pos.y-1, pos.z)
	# note: pos.y-1 is important!

	if (b == block.AIR.id or b == block.WATER_STATIONARY.id or
	b == block.WATER_FLOWING.id): 
		# mc.postToChat("not safe")
		print("not safe")
	else:
		# mc.postToChat("safe")
		print("safe")


# infinite game loop
while True:
	time.sleep(0.5)
	safeFeet()


