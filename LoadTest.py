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

terrainMap = TerrainMap(ridgedHeight, 0.1)
terrainMap.calculate_wind_direction(3, 50)
terrainMap.generate_rivers(0.2, 0.002)
terrainMap.calculate_rainfall_from_wind()
terrainMap.calculate_temperature()
terrainMap.calculate_biomes()

img = terrainMap.get_terrain_map_image()
img.save("test.png", "PNG")

wind_map = terrainMap.get_wind_direction_map_image()
wind_map.save("wind.png", "PNG")

height_map = terrainMap.get_height_map_image()
height_map.save("height.png", "PNG")

water_map = terrainMap.get_water_map_image()
water_map.save("water.png", "PNG")

temperature_map = terrainMap.get_temperature_map_image()
temperature_map.save("temperature.png", "PNG")

rainfall_map = terrainMap.get_rainfall_map_image()
rainfall_map.save("rainfall.png", "PNG")

biome_map = terrainMap.get_biome_map_image()
biome_map.save("biome.png", "PNG")
