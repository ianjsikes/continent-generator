__author__ = 'Ian'

import colorsys

class MapPixel:
    """A single unit of map terrain"""

    TUNDRA, BOREAL_FOREST, COLD_DESERT, WOODLAND, TEMPERATE_FOREST, TEMPERATE_RAINFOREST, SUBTROPICAL_DESERT, SAVANNA, TROPICAL_RAINFOREST = range(9)
    waterColor = (0.55, 1.0, 0.2)
    landColor = (0.17, 1.0, 0.1)

    def __init__(self, coordinates, height, sea_level):
        self.coordinates = coordinates
        self.height = height
        self.seaLevel = sea_level
        self.rainfall = 0.0
        self.temperature = 0.0
        self.windDirection = 0
        self.biome = self.TUNDRA
        self.isWater = True if self.height <= self.seaLevel else False

    def calculate_biome(self):
        if self.temperature < 0.15:
            self.biome = self.TUNDRA
        elif self.temperature < 0.58:
            if self.rainfall < 0.1:
                self.biome = self.COLD_DESERT
            elif self.rainfall < 0.2:
                self.biome = self.WOODLAND
            elif self.temperature < 0.2:
                self.biome = self.BOREAL_FOREST
            elif self.rainfall < 0.35:
                self.biome = self.TEMPERATE_FOREST
            else:
                self.biome = self.TEMPERATE_RAINFOREST
        else:
            if self.rainfall < 0.12:
                self.biome = self.SUBTROPICAL_DESERT
            elif self.rainfall < 0.45:
                self.biome = self.SAVANNA
            else:
                self.biome = self.TROPICAL_RAINFOREST

    def get_biome_map_color(self):
        if self.isWater:
            return 0, 0, 0
        elif self.biome == self.TUNDRA:
            return 165, 208, 230
        elif self.biome == self.BOREAL_FOREST:
            return 117, 209, 181
        elif self.biome == self.COLD_DESERT:
            return 209, 191, 117
        elif self.biome == self.WOODLAND:
            return 171, 78, 41
        elif self.biome == self.TEMPERATE_FOREST:
            return 39, 125, 46
        elif self.biome == self.TEMPERATE_RAINFOREST:
            return 53, 150, 61
        elif self.biome == self.SUBTROPICAL_DESERT:
            return 191, 158, 57
        elif self.biome == self.SAVANNA:
            return 149, 196, 55
        else:
            # TROPICAL RAIN FOREST
            return 34, 222, 13

    def get_rainfall_map_color(self):
        if self.isWater:
            return (0, 0, 0)
        else:
            return (int(255*self.rainfall), int(255*self.rainfall), int(255*self.rainfall))

    def get_wind_direction_map_color(self):
        if self.isWater:
            return (0, 0, 0)
        else:
            hue = float(self.windDirection) / 360.0
            col = colorsys.hsv_to_rgb(hue, 1.0, 0.6)
            return (int(col[0] * 255), int(col[1] * 255), int(col[2] * 255))

    def get_temperature_map_color(self):
        if self.isWater:
            return (0, 0, 0)
        else:
            return (int(255*self.temperature), int(255*self.temperature), int(255*self.temperature))

    def get_greyscale_color(self):
        return (int(255*self.height), int(255*self.height), int(255*self.height))

    def get_rgb_color(self):
        if(self.isWater):
            col = colorsys.hsv_to_rgb(self.waterColor[0], self.waterColor[1], self.waterColor[2] + self.height)
        else:
            col = colorsys.hsv_to_rgb(self.landColor[0] + (self.rainfall / 10.0), self.landColor[1], self.landColor[2] + self.height)
        return (int(col[0] * 255), int(col[1] * 255), int(col[2] * 255))

