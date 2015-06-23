__author__ = 'Ian'

from PIL import Image
import math

res = 255
img = Image.new('RGB', (res, res), "black")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        color = (255, 255, 255)
        distance = math.pow(math.pow(i - 127, 2) + math.pow(j - 127, 2), 0.5)
        val = (127 - int(distance)) * 4
        pixels[i,j] = (val, val, val)

img.save("radial.png", "PNG");