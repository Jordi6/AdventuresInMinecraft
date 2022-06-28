import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

# get entity
# entityIds = mc.getPlayerEntityIds()
# for a in entityIds:
# 	print a


x1 = 19
z1 = 10
x2 = 30
z2 = 20

HOME_X = 33
HOME_Y = 150
HOME_Z = 29


rent = 0
inField = 0

# land 33, 65, 29

while True:
	time.sleep(1)
	entityTile = mc.entity.getTilePos(27)
	if entityTile.x > x1 and entityTile.x < x2 and entityTile.z > z1 and entityTile.z < z2:
		rent = rent + 1
		mc.postToChat("You owe rent: " + str(rent))
		inField = inField + 1
		if inField > 3:
			mc.postToChat("To slow!")
			mc.entity.setPos(27, HOME_X, HOME_Y, HOME_Z)
	else: # not inside the field
		inField = 0
			




