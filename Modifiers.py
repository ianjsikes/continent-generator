__author__ = 'Ian'
import MapUtility
import colorsys

def scale(arr, factor):
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            arr[x][y] *= factor
            arr[x][y] = MapUtility.clamp(arr[x][y])
    return arr

def invert(arr):
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            arr[x][y] = 1 - arr[x][y]
            arr[x][y] = MapUtility.clamp(arr[x][y])
    return arr

def cutoff(arr, val):
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] < val:
                arr[x][y] = 0
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

def add(arrA, arrB):
    arrC = list()
    for x in range(len(arrA)):
        arrC.append(list())
        for y in range(len(arrA[0])):
            arrC[x].append(arrA[x][y] + arrB[x][y])
            arrC[x][y] = MapUtility.clamp(arrC[x][y])
    return arrC

def overlay(arrA, arrB):
    arrC = list()
    val = 0
    for x in range(len(arrA)):
        arrC.append(list())
        for y in range(len(arrA[0])):
            if arrB[x][y] < 0.5:
                val = 2.0 * arrA[x][y] * arrB[x][y]
            else:
                val = 1.0 - (2.0 * (1 - arrA[x][y]) * (1 - arrB[x][y]))
            arrC[x].append(val)
    return arrC

def evaluate(arr, cutoff):
    out = list()
    for x in range(len(arr)):
        out.append(list())
        for y in range(len(arr[0])):
            out[x].append(MapUtility.evaluateColor(arr[x][y], cutoff))
    return out
