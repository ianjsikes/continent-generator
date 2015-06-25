__author__ = 'Ian'

from PIL import Image
from MapPixel import MapPixel
import random
import math
from Queue import Queue

class TerrainMap:
    """A map, duh"""

    MAX_ITERATIONS = 10000

    def __init__(self, height_array, sea_level):
        self.heightArray = height_array
        self.resolution = len(height_array)
        self.seaLevel = sea_level
        self.mapArray = list()
        self.fill_map_array()

        print "Map created"
        self.print_map_info()

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.resolution and 0 <= y < self.resolution

    def neighbors(self, id):
        (x, y) = id
        # results = [(x, y+1), (x-1, y), (x+1, y), (x, y-1)]
        results = [(x-1, y+1), (x, y+1), (x+1, y+1), (x-1, y), (x+1, y), (x-1, y-1), (x, y-1), (x+1, y-1)]
        if (x + y) % 2 == 0: results.reverse()
        results = filter(self.in_bounds, results)

        return results

    def cost(self, a, b):
        heightA = self.mapArray[a[0]][a[1]].height
        heightB = self.mapArray[b[0]][b[1]].height
        return (heightB - heightA)

    def generate_rivers(self, start_height, frequency):
        print "Generating rivers..."
        river_count = 0
        for x in range(len(self.mapArray)):
            for y in range(len(self.mapArray)):
                if self.mapArray[x][y].height >= start_height:
                    if random.random() <= frequency:
                        river_count += 1
                        came_from, goal = self.find_river_path((x, y))
                        path = self.reconstruct_path(came_from, (x, y), goal)
                        for location in path:
                            self.mapArray[location[0]][location[1]].isWater = True
        # print str(river_count) + " rivers created"

    def calculate_temperature(self):
        #simple north = cold model (boring)
        for x in range(len(self.mapArray)):
            for y in range(len(self.mapArray)):
                self.mapArray[x][y].temperature = float(y) / float(self.resolution)
                self.mapArray[x][y].temperature *= 1 - (self.mapArray[x][y].height * 0.9)

    def calculate_rainfall(self):
        print "Calculating rainfall..."
        area = 40
        amount = 0.04
        for x in range(len(self.mapArray)):
            for y in range(len(self.mapArray)):
                if not self.mapArray[x][y].isWater:
                    for a in range(x - (area / 2), x + (area / 2)):
                        if 0 <= a < self.resolution:
                            for b in range(y - (area / 2), y + (area / 2)):
                                if 0 <= b < self.resolution:
                                    if self.mapArray[a][b].isWater:
                                        radialAmount = math.pow(math.pow(a - x, 2) + math.pow(b - y, 2), 0.5)
                                        radialAmount = 1.0 / radialAmount
                                        radialAmount *= amount
                                        if self.mapArray[a][b].height <= self.seaLevel:
                                            radialAmount *= 0.02
                                        self.mapArray[x][y].rainfall += radialAmount
        for x in range(len(self.mapArray)):
            for y in range(len(self.mapArray)):
                self.mapArray[x][y].rainfall = min(self.mapArray[x][y].rainfall, 1.0)

    def fill_map_array(self):
        for x in range(len(self.heightArray)):
            self.mapArray.append(list())
            for y in range(len(self.heightArray[0])):
                self.mapArray[x].append(MapPixel((x, y), self.heightArray[x][y], self.seaLevel))

    def get_height_map_image(self):
        img = Image.new('RGB', (len(self.mapArray), len(self.mapArray)), "black")
        pixels = img.load()
        for x in range(len(self.mapArray)):
            for y in range(len(self.mapArray)):
                pixels[x, y] = self.mapArray[x][y].get_greyscale_color()
        return img

    def get_rainfall_map_image(self):
        img = Image.new('RGB', (len(self.mapArray), len(self.mapArray)), "black")
        pixels = img.load()
        for x in range(len(self.mapArray)):
            for y in range(len(self.mapArray)):
                pixels[x, y] = self.mapArray[x][y].get_rainfall_map_color()
        return img

    def get_temperature_map_image(self):
        img = Image.new('RGB', (len(self.mapArray), len(self.mapArray)), "black")
        pixels = img.load()
        for x in range(len(self.mapArray)):
            for y in range(len(self.mapArray)):
                pixels[x, y] = self.mapArray[x][y].get_temperature_map_color()
        return img

    def get_terrain_map_image(self):
        img = Image.new('RGB', (len(self.mapArray),len(self.mapArray)), "black")
        pixels = img.load()
        for x in range(len(self.mapArray)):
            for y in range(len(self.mapArray)):
                pixels[x, y] = self.mapArray[x][y].get_rgb_color()
        return img

    def print_map_info(self):
        print "**************************************"
        print "Input heightmap resolution: " + str(len(self.heightArray)) + "x" + str(len(self.heightArray[0]))
        print "Sea level: " + str(self.seaLevel)
        print "Map size: " + str(len(self.mapArray)) + "x" + str(len(self.mapArray[0]))
        print "**************************************"

    def find_river_path(self, start):
        frontier = Queue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()
            self.mapArray[current[0]][current[1]].isWater = True

            if self.mapArray[current[0]][current[1]].height <= self.seaLevel:
                break

            for next in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    #self.mapArray[next[0]][next[1]].isWater = True
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from, current

    def reconstruct_path(self, came_from, start, goal):
        current = goal
        path = [current]
        iterations = 0
        while current != start:
            iterations += 1
            if iterations >= self.MAX_ITERATIONS:
                break
            current = came_from[current]
            print str(current)
            path.append(current)
        path.reverse()
        return path
