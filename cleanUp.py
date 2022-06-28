#!/usr/bin/env python2.7
import mcpi.minecraft as minecraft
import mcpi.block as block


mc = minecraft.Minecraft.create()

playerId = mc.getPlayerEntityId("TonyStarkJ6")
# playerId2 = mc.getPlayerEntityId("Jr_17")

def cleanUp():

    player = mc.entity.getTilePos(playerId)
    size = int(raw_input("enter size of area to clear: "))

    x = player.x
    y = player.y
    z = player.z

    # # create a specific block
    block_type = block.Block(0)

    # player will be in the middle.
    # x1, y1, z1 by x2, y2, z2

    # cube in front of you
    # mc.setBlocks((x + size), (y), (z + size),
    #              (x), (y), (z), block_type)

    # cube, steve is in the middle
    mc.setBlocks(x - size, y-size, z- size, 
                x+size, y+size, z+size, block_type)

cleanUp()
