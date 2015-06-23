__author__ = 'Ian'

from PIL import Image
from noise import pnoise2, snoise2

def generate(resolution, octaves, frequency):
    img = Image.new('RGB', (resolution, resolution), "black")
    pixels = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            sample = int(snoise2(x / frequency, y / frequency, octaves) * 127 + 128)
            color = (sample, sample, sample)
            pixels[x, y] = color

    return img

z = generate(255, 3, 48.0)
z.save("test.png", "PNG")