import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

playerId = mc.getPlayerEntityId("TonyStarkJ6")


pos = mc.entity.getTilePos(playerId)


for a in range(100):
	mc.setBlock(pos.x + 3, pos.y + a, pos.z, block.GRASS.id)



