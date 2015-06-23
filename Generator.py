__author__ = 'Ian'

from PIL import Image, ImageChops
from noise import pnoise2, snoise2
import HeightMapGen
import math
import MapUtility
import Modifiers

def generateNoise(resolution, octaves, frequency):
    arr = list()

    for x in range(resolution):
        arr.append(list())
        for y in range(resolution):
            sample = snoise2(x / frequency, y / frequency, octaves) + 0.5
            arr[x].append(sample)

    return arr

def generateRadial(resolution, threshold, scale=1):
    arr = list()
    center = resolution / 2

    for x in range(resolution):
        arr.append(list())
        for y in range(resolution):
            distance = math.pow(math.pow(x - center, 2) + math.pow(y - center, 2), 0.5)
            val = ((center - (distance*(1/scale))) / resolution) * threshold
            arr[x].append(val)

    return arr

#noise = HeightMapGen.generateNoise(255, 5, 80.0)
#grad = HeightMapGen.generateRadial(255, 4)

#heightMap = ImageChops.subtract(grad, noise, 1, 50)

noiseArray = generateNoise(255, 6, 96.0)
radialArray = generateRadial(255, 4, 1)
islandArray = Modifiers.subtract(radialArray, noiseArray)
img = MapUtility.floatArrayToImage(islandArray)

img.save("test.png", "PNG")

