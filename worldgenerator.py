import random
from block import Block
import time
import numpy as np
import sys
from scipy.ndimage.interpolation import zoom

#from perlin_noise import PerlinNoise
from noise import snoise2
import math
from tqdm import tqdm
import time


class WorldGenerator:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.world = []
        #self.generate()
        self.generategui()

    def generate(self):
        #print("aa")
        #for i in range(self.height):
            #if i > 10:
            #for j in range(self.width):
                #self.world.append(Block(1, j, i))


        #np.set_printoptions(threshold=sys.maxsize)

        #arr = np.random.uniform(size=(4, 4))
        #arr = zoom(arr, 8)
        #arr = arr > 0.5
        #arr = np.where(arr, '-', '#')
        #arr = np.array_str(arr, max_line_width=500)
        #print(arr)

        from opensimplex import OpenSimplex
        gen = OpenSimplex()

        def noise(nx, ny):
            # Rescale from -1.0:+1.0 to 0.0:1.0
            return gen.noise2d(nx, ny) / 2.0 + 0.5

        #print("aa")
        value = []
        for y in range(self.height):
            value.append([0] * self.width)
            for x in range(self.width):
                nx = x / self.width - 0.5
                ny = y / self.height - 0.5
                value[y][x] = noise(nx, ny)

                basePerlinValue = (snoise2(float(x) * 384 * 0.01, float(y) * 384 * 0.01, octaves=60, persistence=0.2,lacunarity=2, repeatx=4048, repeaty=4048, base=random.random() * 2048) + 1) / 2.0
                print(basePerlinValue)
                if basePerlinValue > 0.6:
                    self.world.append(Block(1, x, y))
                elif basePerlinValue > 0.3:
                    self.world.append(Block(2, x, y))
                elif basePerlinValue > 0.0:
                    self.world.append(Block(3, x, y))

        #basePerlinValue = (snoise2(float(x)*0.0025, float(y)*0.0025, octaves=8, persistence=0.5, lacunarity=2.0, repeatx=2048, repeaty=2048, base=random.random()*2048) + 1)/2.0;

    def generategui(self):
        start_time = time.time()
        # Generate Grass
        for i in range(self.height):
            for j in range(self.width):
                self.world.append(Block(1, j, i))
        print("--- %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
        # Generate water
        for i in self.world:
           if random.randint(0, 1000) == 1:
               self.world[self.world.index(i)] = Block(3, i.x, i.y)
        print("--- %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
        # Build on water
        for c in range(2, 200):
            for i in self.world:
                if i.id == 3:
                    if random.randint(0, c) == 1:
                        self.world[self.world.index(i)-1] = Block(3, self.world[self.world.index(i)-1].x, self.world[self.world.index(i)-1].y)
                    if random.randint(0, c) == 1:
                        self.world[self.world.index(i)+1] = Block(3, self.world[self.world.index(i)+1].x, self.world[self.world.index(i) + 1].y)
                    if random.randint(0, c) == 1 and self.world.index(i) > self.width:
                        self.world[self.world.index(i)-self.width] = Block(3, self.world[self.world.index(i)-self.width].x, self.world[self.world.index(i) - self.width].y)
                    if random.randint(0, c) == 1 and self.world.index(i) + self.width < self.width + self.height:
                        self.world[self.world.index(i)+self.width] = Block(3, self.world[self.world.index(i)+self.width].x, self.world[self.world.index(i) + self.width].y)
        print("--- %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
        # Remove single block islands
        for i in self.world:
            if i.id != 3:
                if self.world.index(i) + self.width < self.width + self.height and self.world.index(i) > self.width:
                    if self.world[self.world.index(i) - 1] == 3 and self.world[self.world.index(i) + 1] == 3 and self.world[self.world.index(i) - self.width] == 3 and self.world[self.world.index(i) + self.width] == 3:
                        self.world[self.world.index(i)] = Block(3, self.world[self.world.index(i)].x, self.world[self.world.index(i)].y)
        print("--- %s seconds ---" % (time.time() - start_time))

        # Generate sand
        for i in self.world:
            if i.id == 3:
                if self.world[self.world.index(i) - 1].id == 1:
                    self.world[self.world.index(i) - 1] = Block(2, self.world[self.world.index(i) - 1].x,self.world[self.world.index(i) - 1].y)
                if self.world[self.world.index(i) + 1].id == 1:
                    self.world[self.world.index(i) + 1] = Block(2, self.world[self.world.index(i) + 1].x,self.world[self.world.index(i) + 1].y)
                if self.world.index(i) > self.width and self.world[self.world.index(i) - self.width].id == 1:
                    self.world[self.world.index(i) - self.width] = Block(2, self.world[self.world.index(i) - self.width].x, self.world[self.world.index(i) - self.width].y)
                if self.world.index(i) + self.width < self.width * self.height and self.world[self.world.index(i) + self.width].id == 1:
                    self.world[self.world.index(i) + self.width] = Block(2, self.world[self.world.index(i) + self.width].x, self.world[self.world.index(i) + self.width].y)

        # Build on sand - Add 2 or 3 block of sand around water



    def get_world(self):
        print(self.world)
        return self.world


