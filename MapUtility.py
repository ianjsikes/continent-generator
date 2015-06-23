__author__ = 'Ian'
from PIL import Image
import colorsys

def floatArrayToImage(arr):
    img = Image.new('RGB', (len(arr), len(arr)), "black")
    pixels = img.load();
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            val = int(255 * arr[x][y])
            pixels[x, y] = (val, val, val)
    return img

def rgbArrayToImage(arr):
    img = Image.new('RGB', (len(arr), len(arr)), "black")
    pixels = img.load();
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            pixels[x, y] = arr[x][y]
    return img

def clamp(val):
    return max(0.0, min(1.0, val))

def evaluateColor(val, cutoff):
    if(val < cutoff):
        col = colorsys.hsv_to_rgb(0.55, 1.0, val + 0.2)
        return (int(col[0] * 255), int(col[1] * 255), int(col[2] * 255))
    else:
        col = colorsys.hsv_to_rgb(0.2, 1.0, val + 0.1)
        return (int(col[0] * 255), int(col[1] * 255), int(col[2] * 255))