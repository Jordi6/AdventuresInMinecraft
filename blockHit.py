# Adventrue 4 - sensing that a block has been hit

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

#get player id
playerId = mc.getPlayerEntityId("TonyStarkJ6")

diamond_pos = mc.entity.getTilePos(playerId)

diamond_pos.x = diamond_pos.x + 1

mc.setBlock(diamond_pos.x, diamond_pos.y, diamond_pos.z, block.DIAMOND_BLOCK.id)

def checkHit():
	events = mc.events.pollBlockHits()
	for e in events:
		pos = e.pos
		v = e.face
		mc.postToChat(v)
		if pos.x == diamond_pos.x and pos.y == diamond_pos.y and pos.z == diamond_pos.z:
			mc.postToChat("HIT")


while True:
	time.sleep(1)
	checkHit()


#END