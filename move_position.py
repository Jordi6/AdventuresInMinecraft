#!/usr/bin/env python2.7


import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()


playerId = mc.getPlayerEntityId("TonyStarkJ6")

mc.entity.setTilePos(playerId, 10, 64, 10)
