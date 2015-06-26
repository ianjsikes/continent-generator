__author__ = 'Ian'

import Generators
import Modifiers
import MapUtility
import random
from TerrainMap import TerrainMap

RESOLUTION = 512

randomOffset = (random.randint(-500, 500), random.randint(-500, 500))
noise = Generators.generateNoise(RESOLUTION, randomOffset, 2, 256.0)
radial = Generators.generateRadial(RESOLUTION, 3.0, 2.0)

randomOffset = (random.randint(-500, 500), random.randint(-500, 500))
detailNoise = Generators.generateNoise(RESOLUTION, randomOffset, 6, 128.0)

shape = Modifiers.subtract(radial, noise)
height = Modifiers.subtract(shape, detailNoise)

#terrainMap = TerrainMap(height, 0.1)

ridgedNoise = Generators.generateRidgedNoise(RESOLUTION, randomOffset, 3, 256.0)

ridgedNoise = Modifiers.scale(ridgedNoise, 0.75)
ridgedHeight = Modifiers.overlay(ridgedNoise, height)

terrainMap = TerrainMap(height, 0.1)
ridgedMap = TerrainMap(ridgedHeight, 0.1)

img = terrainMap.get_terrain_map_image()
img.save("test.png", "PNG")

ridged = ridgedMap.get_terrain_map_image()
ridged.save("ridged.png", "PNG")

height_map = terrainMap.get_height_map_image()
height_map.save("height.png", "PNG")
