import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()


# set the global enity id of our player. 
playerId = mc.getPlayerEntityId("TonyStarkJ6")

# railroad
# blockObj = block.Block(66)
# block.GLASS.id

# define our function
def buildBridge():
	pos = mc.entity.getTilePos(playerId)
	b = mc.getBlock(pos.x, pos.y-1, pos.z)
	if (b == block.AIR.id or b == block.WATER_STATIONARY.id or
	b == block.WATER_FLOWING.id): 
		mc.setBlock(pos.x, pos.y-1, pos.z, block.GLASS.id)

# infinite game loop
while True:
	buildBridge()


