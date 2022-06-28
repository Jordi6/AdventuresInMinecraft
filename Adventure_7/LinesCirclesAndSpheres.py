# Adventure 7 
# lines circles and speheres, also maths


import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time


mc = minecraft.Minecraft.create()
playerId = mc.getPlayerEntityId("TonyStarkJ6")


mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.entity.getTilePos(playerId)


# draw line stright-up
mcdrawing.drawLine(pos.x, pos.y, pos.z,
				   pos.x, pos.y + 20, pos.z,
				   block.WOOL.id, 1)

# horizontal line
mcdrawing.drawLine(pos.x, pos.y, pos.z,
				   pos.x + 20, pos.y, pos.z,
				   block.WOOL.id, 2)

# diagonal line
mcdrawing.drawLine(pos.x, pos.y, pos.z,
				   pos.x + 20, pos.y + 20, pos.z,
				   block.WOOL.id, 3)

time.sleep(6)


# draw a circle
pos = mc.entity.getTilePos(playerId)


mcdrawing.drawCircle(pos.x, pos.y + 20, pos.z, 20,
					 block.WOOL.id, 4)

time.sleep(5)


# draw a spehere
pos = mc.entity.getTilePos(playerId)


mcdrawing.drawSphere(pos.x, pos.y + 20, pos.z, 15,
					 block.WOOL.id, 5)

time.sleep(5)
