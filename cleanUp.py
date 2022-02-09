import mcpi.minecraft as minecraft
import mcpi.block as block


mc = minecraft.Minecraft.create()

playerId = mc.getPlayerEntityId("TonyStarkJ6")
playerId2 = mc.getPlayerEntityId("Jr_17")


player = mc.entity.getTilePos(playerId)
#size = int(raw_input("enter size of area to clear? "))

x = player.x
y = player.y
z = player.z

# # create a specific block
blockObj = block.Block(165)


# this sets a foundation of blocks around the player.
# player will be in the middle. 
# change the block type with the last argument. 
# x1, y1, z1 by x2, y2, z2.
mc.setBlocks((x - size), (y - 1), (z - size), 
	(x + size), (y - 1), (z + size), block.AIR.id)



