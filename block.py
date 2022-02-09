import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.entity.getTilePos(27)

mc.setBlock(pos.x+3, pos.y + 6, pos.z, block.SAND.id)

