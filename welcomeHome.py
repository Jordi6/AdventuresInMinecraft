import mcpi.minecraft as minecraft
import time

# x= 247 y= 64 z=-71

mc = minecraft.Minecraft.create()

while True:
	time.sleep(1)
	pos = mc.player.getTilePos()
	if pos.x == 247 and pos.z == -71:
		mc.postToChat("Welcome Home!")

