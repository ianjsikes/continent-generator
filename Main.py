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

height = Modifiers.subtract(radial, noise)
height = Modifiers.subtract(height, detailNoise)

terrainMap = TerrainMap(height, 0.1)
terrainMap.generate_rivers(0.2, 0.002)
#terrainMap.calculate_rainfall()
terrainMap.calculate_temperature()
img = terrainMap.get_terrain_map_image()
img.save("test.png", "PNG")
rainfall_map = terrainMap.get_temperature_map_image()
rainfall_map.save("rainfall.png", "PNG")
