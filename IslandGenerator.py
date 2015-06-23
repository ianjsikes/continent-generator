__author__ = 'Ian'

from PIL import Image
from noise import pnoise2, snoise2

res = 255
img = Image.new('RGB', (res, res), "black")
grad = Image.open("radial.png")
gradPixels = grad.load()
pixels = img.load()

octaves = 5
freq = 16.0 * octaves


for i in range(img.size[0]):
    for j in range(img.size[1]):
        sample = int(snoise2(i / freq, j / freq, octaves) * 127 + 128)
        gradSample = gradPixels[i, j][0]
        sample -= int((255 - gradSample) * 0.5)
        color = (0, 0, 0)
        if sample > 200:
            color = (280, 100, 100)
        elif sample > 100:
            color = (100, 200, 100)
        else:
            color = (100, 100, 200)
        pixels[i,j] = color

img.save("island.png", "PNG");