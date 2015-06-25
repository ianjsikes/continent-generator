__author__ = 'Ian'

from noise import snoise2, pnoise2
import math
import MapUtility

# Returns a 2D array of perlin noise values
def generateNoise(resolution, offset, octaves, frequency):
    arr = list()
    min = 1.0
    max = 0.0

    for x in range(resolution):
        arr.append(list())
        for y in range(resolution):
            sample = (snoise2((x+offset[0]) / frequency, (y+offset[1]) / frequency, octaves)/2) + 0.5
            if sample < min:
                min = sample
            elif sample > max:
                max = sample
            sample = MapUtility.clamp(sample)
            arr[x].append(sample)
    print "min: " + str(min)
    print "max: " + str(max)
    return arr

def generateInflectedNoise(resolution, offset, octaves, frequency):
    arr = list()
    min = 1.0
    max = 0.0

    for x in range(resolution):
        arr.append(list())
        for y in range(resolution):
            sample = sumInflectedNoise((x+offset[0], y+offset[1]), frequency, octaves)
            if sample < min:
                min = sample
            elif sample > max:
                max = sample
            sample = MapUtility.clamp(sample)
            arr[x].append(sample)
    print "min: " + str(min)
    print "max: " + str(max)
    return arr

def generateRidgedNoise(resolution, offset, octaves, frequency):
    arr = list()
    min = 1.0
    max = 0.0

    for x in range(resolution):
        arr.append(list())
        for y in range(resolution):
            sample = sumRidgedNoise((x+offset[0], y+offset[1]), frequency, octaves)
            if sample < min:
                min = sample
            elif sample > max:
                max = sample
            sample = MapUtility.clamp(sample)
            arr[x].append(sample)
    print "min: " + str(min)
    print "max: " + str(max)
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

def sumNoise(point, frequency, octaves=2, lacunarity=2.0, persistence=0.5):
    sum = (snoise2(point[0] / frequency, point[1] / frequency) / 2.0) + 0.5
    amplitude = 1.0
    ran = 1.0
    for o in range(1, octaves):
        frequency /= lacunarity
        amplitude *= persistence
        ran += amplitude
        sum += (snoise2(point[0] / frequency, point[1] / frequency) * 0.5 + 0.5) * amplitude
    return sum / ran

def sumInflectedNoise(point, frequency, octaves=2, lacunarity=2.0, persistence=0.5):
    sum = abs(snoise2(point[0] / frequency, point[1] / frequency))
    amplitude = 1.0
    ran = 1.0
    for o in range(1, octaves):
        frequency /= lacunarity
        amplitude *= persistence
        ran += amplitude
        sum += abs(snoise2(point[0] / frequency, point[1] / frequency)) * amplitude
    return sum / ran

def sumRidgedNoise(point, frequency, octaves=2, lacunarity=2.0, persistence=0.5):
    sum = 1.0 - abs(snoise2(point[0] / frequency, point[1] / frequency))
    amplitude = 1.0
    ran = 1.0
    for o in range(1, octaves):
        frequency /= lacunarity
        amplitude *= persistence
        ran += amplitude
        sum += (1.0 - abs(snoise2(point[0] / frequency, point[1] / frequency))) * amplitude
    return sum / ran

def generateFBMNoise(resolution, offset, octaves, frequency):
    arr = list()
    min = 1.0
    max = 0.0

    for x in range(resolution):
        arr.append(list())
        for y in range(resolution):
            sample = sumNoise((x + offset[0], y + offset[1]), frequency, octaves)
            if sample < min:
                min = sample
            elif sample > max:
                max = sample
            sample = MapUtility.clamp(sample)
            arr[x].append(sample)
    print "min: " + str(min)
    print "max: " + str(max)
    return arr