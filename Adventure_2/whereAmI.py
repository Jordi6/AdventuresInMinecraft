import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

entityTile = mc.entity.getTilePos(35)

print("x= " + str(entityTile.x) + " y= " + str(entityTile.y) + " z=" + str(entityTile.z))

mc.postToChat("x= " + str(entityTile.x) + " y= " + str(entityTile.y) + " z=" + str(entityTile.z))


