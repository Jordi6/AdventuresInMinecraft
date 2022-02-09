# set the tile pos of a user
# Jr_17
#TonyStarkJ6

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()


# get player entity id number
playerId = mc.getPlayerEntityId("TonyStarkJ6")

# get the tile pos of player
pos = mc.entity.getTilePos(playerId)

#print the position
print("pos: " + str(pos))

# set the position of: argument one.
mc.entity.setPos(playerId, pos)

