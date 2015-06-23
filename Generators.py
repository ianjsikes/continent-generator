__author__ = 'Ian'

from noise import snoise2
import math
import MapUtility

# Returns a 2D array of perlin noise values
def generateNoise(resolution, offset, octaves, frequency):
    arr = list()

    for x in range(resolution):
        arr.append(list())
        for y in range(resolution):
            sample = (snoise2((x+offset[0]) / frequency, (y+offset[1]) / frequency, octaves)/2) + 0.5
            sample = MapUtility.clamp(sample)
            arr[x].append(sample)
    return arr

def generateInflectedNoise(resolution, offset, octaves, frequency):
    arr = list()

    for x in range(resolution):
        arr.append(list())
        for y in range(resolution):
            sample = abs(snoise2((x+offset[0]) / frequency, (y+offset[1]) / frequency, octaves)/2)
            sample = MapUtility.clamp(sample)
            arr[x].append(sample)
    return arr

def generateRidgedNoise(resolution, offset, octaves, frequency):
    arr = list()

    for x in range(resolution):
        arr.append(list())
        for y in range(resolution):
            sample = 1.0 - abs(snoise2((x+offset[0]) / frequency, (y+offset[1]) / frequency, octaves)/2)
            sample = MapUtility.clamp(sample)
            arr[x].append(sample)
    return arr

# Returns a 2D array with a radial gradient
def generateRadial(resolution, threshold, scale=1.0):
    arr = list()
    center = resolution / 2

    for x in range(resolution):
        arr.append(list())
        for y in range(resolution):
            distance = math.pow(math.pow(x - center, 2) + math.pow(y - center, 2), 0.5)
            val = ((center - (distance*(1/scale))) / resolution) * threshold
            #val = MapUtility.clamp(val)
            arr[x].append(val)

    return arr