import random
from block import Block
import numpy as np
import sys
from scipy.ndimage.interpolation import zoom
#from perlin_noise import PerlinNoise
from noise import snoise2;
import math
from tqdm import tqdm


class WorldGenerator:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.world = []
        self.generate()

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

                basePerlinValue = (snoise2(float(x) * 0.0025, float(y) * 0.0025, octaves=8, persistence=0.5,
                                           lacunarity=2.0, repeatx=2048, repeaty=2048,
                                           base=random.random() * 2048) + 1) / 2.0;
                print(basePerlinValue)
                if value[y][x] > 0.3:
                    self.world.append(Block(1, x, y))
                elif value[y][x] > 0.2:
                    self.world.append(Block(2, x, y))
                elif value[y][x] > 0.1:
                    self.world.append(Block(3, x, y))

        basePerlinValue = (snoise2(float(x)*0.0025, float(y)*0.0025, octaves=8, persistence=0.5, lacunarity=2.0, repeatx=2048, repeaty=2048, base=random.random()*2048) + 1)/2.0;



    def get_world(self):
        print(self.world)
        return self.world


