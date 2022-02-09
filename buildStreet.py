# Adventure 3, building houses 2

import mcpi.minecraft as minecraft
import mcpi.block as block


mc = minecraft.Minecraft.create()

playerId = mc.getPlayerEntityId("TonyStarkJ6")


SIZE = 10 


player = mc.entity.getTilePos(playerId)
x = player.x + 2
y = player.y
z = player.z


def house():

	midx = x + SIZE/2
	midy = y + SIZE/2

	# House Shell
	mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE,
		block.COBBLESTONE.id)

	# Carve inside of house
	mc.setBlocks(x+1, y, z+1, x+SIZE-2, y+SIZE-1, z+SIZE-2,
		block.AIR.id)

	# Carve door way
	mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)

	# Carve out two windows
	mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z,
		block.GLASS.id)
	mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z,
		block.GLASS.id)

	# Add woden roof
	mc.setBlocks(x, y+SIZE-1, z, x+SIZE, y+SIZE-1, z+SIZE,
		block.WOOD.id)

	# add a woollen carpet
	mc.setBlocks(x+1, y-1, z+1, x+SIZE-2, y-1, z+SIZE-2,
		block.WOOL.id, 14)

for h in range(5):
	house()
	x = x + SIZE

#END
