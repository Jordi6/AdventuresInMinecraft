# get the entity id's of the players connected to the game

import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

# 35, 38

entityIds = mc.getPlayerEntityIds()
oneEntityId = entityIds[0]
twoEntityId = entityIds[1]

print("1: " + str(oneEntityId) + ", 2: " + str(twoEntityId))


entityPos = mc.entity.getPos(oneEntityId)


entityTile = mc.entity.getTilePos(38)

print(entityTile)










