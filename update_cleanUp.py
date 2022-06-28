#!/usr/bin/env python2.7
import mcpi.minecraft as minecraft
import mcpi.block as block


mc = minecraft.Minecraft.create()

playerId = mc.getPlayerEntityId("TonyStarkJ6")


def cleanUp():
    quit = False
    
    while(not quit):

        # option = int(raw_input("enter num: "))
        option = int(raw_input("Please enter your choice: \n" +
                                "1. set blocks in front of you, and above\n" +
                                "2. set blocks in a cube, set number of blocks above and below you\n" +
                                "3. exit.\n\n"))

        player = mc.entity.getTilePos(playerId)

        direction = mc.entity.getDirection(playerId)

        if option == 1:
            block_to_use = choseBlock()
            
            # block to use above 
            print("How many blocks to set above: ")
            size_above = setBlock()

            # block to use in front
            print("How many blocks to set in-front: ")
            size_front = setBlock()

            x = round(player.x + (direction.x * 5))
            y = round(player.y + (direction.y * 5) + 1)
            z = round(player.z + (direction.z * 5))

            mc.setBlocks( x, y, z,
                (player.x), (y), (player.z), block_to_use)
        
        elif option == 2:
            print("impliment")
            # block_to_use = choseBlock()

        elif option == 3:
            quit = True
            
# use a class
def setBlock():
    size = int(raw_input("Enter how many blocks to set: "))
    return size
            
def choseBlock():
    block_type = int(raw_input("Enter type of block to use: "))
    block_type = block.Block(block_type)
    return block_type

            
cleanUp()