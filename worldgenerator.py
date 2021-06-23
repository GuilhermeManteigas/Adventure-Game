import random
from block import Block
from entity import Entity
from drop_list import Drop_list
import time

import cProfile

class WorldGenerator:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.world = []
        self.generategui()
        self.drop = Drop_list()

    def generategui(self):
        height = self.height
        width = self.width


        # Generate Grass
        start_time = time.time()
        self.world = [[Block(1, x, y) for y in range(height)] for x in range(width)]
        world = self.world
        print("--- Generate grass: %s seconds ---" % (time.time() - start_time))
        start_time = time.time()

        # Generate Ocean
        start_time = time.time()
        for i in range(height):
            for j in range(width):
                if i < 25 or j < 25 or i > height - 25 or j > width - 25:
                    block = world[i][j]
                    block.id = 3
                    block.collision = True
                    block.height = 0
        print("--- Generated Ocean: %s seconds ---" % (time.time() - start_time))

        # Generate desert
        start_time = time.time()
        for i in range(30, height - 30):
            for j in range(30, width - 30):
                if random.randint(0, 4000) == 1:
                    for y in range(i, i + 20):
                        for x in range(j, j + 20):
                            if 0 < y < height - 1 and 0 < x < width - 1:
                                block = world[y][x]
                                block.id = 2
                                block.collision = False
                                block.height = 1
        print("--- Generate desert: %s seconds ---" % (time.time() - start_time))

        # Build on desert
        start_time = time.time()
        for c in range(2, 100):
            for i in range(height):
                for j in range(width):
                    if world[i][j].id == 2:

                        block = world[i][j - 1]
                        if block.id == 1 and random.randint(0, c) == 1 and j > 0:
                            block.id = 2
                            block.collision = False
                            block.height = 1

                        block = world[i][j + 1]
                        if block.id == 1 and random.randint(0, c) == 1 and j < width - 1:
                            block.id = 2
                            block.collision = False
                            block.height = 1

                        block = world[i - 1][j]
                        if block.id == 1 and random.randint(0, c) == 1 and i > 0:
                            block.id = 2
                            block.collision = False
                            block.height = 1

                        block = world[i + 1][j]
                        if block.id == 1 and random.randint(0, c) == 1 and i < height - 1:
                            block.id = 2
                            block.collision = False
                            block.height = 1
        print("--- Build desert: %s seconds ---" % (time.time() - start_time))

        # Generate water
        start_time = time.time()
        for i in range(height):
            for j in range(width):
                if random.randint(0, 1200) == 1:
                    for y in range(i, i + 10):
                        for x in range(j, j + 10):
                            if 0 < y < height - 1 and 0 < x < width - 1:
                                block = world[y][x]
                                block.id = 3
                                block.collision = True
                                block.height = 0
        print("--- Generate water: %s seconds ---" % (time.time() - start_time))

        # Build on water
        start_time = time.time()
        for c in range(2, 8):
            for i in range(height):
                for j in range(width):
                    if world[i][j].id == 3:

                        if random.randint(0, c) == 1 and j > 0:
                            block = world[i][j - 1]
                            block.id = 3
                            block.collision = True
                            block.height = 0

                        if random.randint(0, c) == 1 and j < width - 1:
                            block = world[i][j + 1]
                            block.id = 3
                            block.collision = True
                            block.height = 0

                        if random.randint(0, c) == 1 and i > 0:
                            block = world[i - 1][j]
                            block.id = 3
                            block.collision = True
                            block.height = 0

                        if random.randint(0, c) == 1 and i < height - 1:
                            block = world[i + 1][j]
                            block.id = 3
                            block.collision = True
                            block.height = 0
        print("--- Generate Lakes: %s seconds ---" % (time.time() - start_time))

        # Remove single block islands
        start_time = time.time()
        for i in range(height):
            for j in range(width):
                if world[i][j].id == 3:
                    if j > 0 and j < width - 1 and i > 0 and i < height - 1:
                        if world[i + 1][j].id == 3 and world[i - 1][j].id == 3 and world[i][j + 1].id == 3 and world[i][j - 1].id == 3:
                            block = world[i][j]
                            block.id = 3
                            block.collision = True
                            block.height = 0
        print("--- Remove single block islands: %s seconds ---" % (time.time() - start_time))

        # Generate Trees
        for i in range(height):
            for j in range(width):
                block = world[i][j]
                if block.id == 1 and random.randint(0, 100) == 1:
                    block.entity = Entity(200, i, j, True, 4, [True, 400])
                    block.entity.create_time = -5
                    #block.entity.entity_face = 2
        print("--- Generate Trees: %s seconds ---" % (time.time() - start_time))
        start_time = time.time()



    def get_world(self):
        return self.world


