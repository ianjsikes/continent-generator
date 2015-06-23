__author__ = 'Ian'

from PIL import Image, ImageChops
from noise import pnoise2, snoise2
import math

def generateNoise(resolution, octaves, frequency):
    img = Image.new('RGB', (resolution, resolution), "black")
    pixels = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            sample = int(snoise2(x / frequency, y / frequency, octaves) * 127 + 128)
            color = (sample, sample, sample)
            pixels[x, y] = color

    return img

def generateRadial(resolution, threshold):
    img = Image.new('RGB', (resolution, resolution), "black")
    pixels = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            color = (255, 255, 255)
            distance = math.pow(math.pow(x - 127, 2) + math.pow(y - 127, 2), 0.5)
            val = (127 - int(distance)) * threshold
            pixels[x, y] = (val, val, val)

    return img

noise = generateNoise(255, 5, 80.0)
grad = generateRadial(255, 4)

heightMap = ImageChops.subtract(grad, noise)

heightMap.save("heightMap.png", "PNG")