# program to get my player id.

import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

def getIds():
    entityIds = mc.getPlayerEntityIds()
    for player in entityIds:
        print player

getIds()



# entityId = mc.getPlayerEntityId("TonyStarkJ6")
def withName():
	entityId = mc.getPlayerEntityId("TonyStarkJ6")
	print entityId

withName()


