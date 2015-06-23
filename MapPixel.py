__author__ = 'Ian'

import colorsys

class MapPixel:
    """A single unit of map terrain"""

    waterColor = (0.55, 1.0, 0.2)
    landColor = (0.2, 1.0, 0.1)

    def __init__(self, coordinates, height, sea_level):
        self.coordinates = coordinates
        self.height = height
        self.seaLevel = sea_level
        self.isWater = True if self.height <= self.seaLevel else False

    def get_greyscale_color(self):
        return (int(255*self.height), int(255*self.height), int(255*self.height))

    def get_rgb_color(self):
        if(self.isWater):
            col = colorsys.hsv_to_rgb(self.waterColor[0], self.waterColor[1], self.waterColor[2] + self.height)
        else:
            col = colorsys.hsv_to_rgb(self.landColor[0], self.landColor[1], self.landColor[2] + self.height)
        return (int(col[0] * 255), int(col[1] * 255), int(col[2] * 255))

