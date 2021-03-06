# Adventure 7 
# pyramid in minecraft


import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import math

def findPointOnCircle(cx, cy, radius, angle):
	x = cx + math.sin(math.radians(angle)) * radius
	y = cy + math.cos(math.radians(angle)) * radius
	x = int(round(x, 0))
	y = int(round(y, 0))
	return(x,y)

mc = minecraft.Minecraft.create()
playerId = mc.getPlayerEntityId("TonyStarkJ6")
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pyramidMiddle = mc.entity.getTilePos(playerId)

PYRAMID_RADIUS = 20
PYRAMID_HEIGHT = 10
PYRAMID_SIDES = 4

for side in range(0, PYRAMID_SIDES):

	point1Angle = int(round((360 / PYRAMID_SIDES) * side, 0))
	point1X, point1Z = findPointOnCircle(
		pyramidMiddle.x, pyramidMiddle.z,
		PYRAMID_RADIUS, point1Angle)
	point2Angle = int(round((360 / PYRAMID_SIDES)
							* (side + 1), 0))
	point2X, point2Z, = findPointOnCircle(
		pyramidMiddle.x, pyramidMiddle.z, 
		PYRAMID_RADIUS, point2Angle)

	trianglePoints = []
	trianglePoints.append(
		minecraft.Vec3(point1X, pyramidMiddle.y, point1Z))
	trianglePoints.append(
		minecraft.Vec3(point2X, pyramidMiddle.y, point2Z))
	trianglePoints.append(
		minecraft.Vec3(pyramidMiddle.x,
					   pyramidMiddle.y + PYRAMID_HEIGHT,
					   pyramidMiddle.z))

	mcdrawing.drawFace(trianglePoints, True, block.SANDSTONE.id)