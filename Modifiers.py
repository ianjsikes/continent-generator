__author__ = 'Ian'
import MapUtility
import colorsys

def scale(arr, factor):
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            arr[x][y] *= factor
            arr[x][y] = MapUtility.clamp(arr[x][y])
    return arr

def subtractConstant(arr, const):
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            arr[x][y] -= const
            arr[x][y] = MapUtility.clamp(arr[x][y])
    return arr

def subtract(arrA, arrB):
    arrC = list()
    for x in range(len(arrA)):
        arrC.append(list())
        for y in range(len(arrA[0])):
            arrC[x].append(arrA[x][y] - arrB[x][y])
            arrC[x][y] = MapUtility.clamp(arrC[x][y])
    return arrC

def evaluate(arr, cutoff):
    out = list()
    for x in range(len(arr)):
        out.append(list())
        for y in range(len(arr[0])):
            out[x].append(MapUtility.evaluateColor(arr[x][y], cutoff))
    return out
