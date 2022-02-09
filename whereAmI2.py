import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()


while True:
	time.sleep(1)
	player = mc.entity.getTilePos(27)
	print("x= " + str(player.x) + " y= " + str(player.y) + " z=" + str(player.z))
	mc.postToChat("x= " + str(player.x) + " y= " + str(player.y) + " z=" + str(player.z))





