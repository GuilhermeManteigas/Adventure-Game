import random
from block import Block
from entity import Entity
import time


class WorldGenerator:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.world = []
        self.generategui()

    def generategui(self):
        # Generate Grass
        start_time = time.time()
        self.world = [[Block(1, x, y) for y in range(self.height)] for x in range(self.width)]
        print("--- Generate grass: %s seconds ---" % (time.time() - start_time))
        start_time = time.time()

        # Generate Ocean
        start_time = time.time()
        for i in range(self.height):
            for j in range(self.width):
                if i < 25 or j < 25 or i > self.height - 25 or j > self.width - 25:
                    self.world[i][j].id = 3
                    self.world[i][j].collision = True
                    self.world[i][j].height = 0
        print("--- Generated Ocean: %s seconds ---" % (time.time() - start_time))

        # Generate desert
        start_time = time.time()
        for i in range(30, self.height - 30):
            for j in range(30, self.width - 30):
                if random.randint(0, 4000) == 1:
                    for y in range(i, i + 20):
                        for x in range(j, j + 20):
                            if 0 < y < self.height - 1 and 0 < x < self.width - 1:
                                self.world[y][x].id = 2
                                self.world[y][x].collision = False
                                self.world[y][x].height = 1
        print("--- Generate desert: %s seconds ---" % (time.time() - start_time))

        # Build on desert
        start_time = time.time()
        for c in range(2, 100):
            for i in range(self.height):
                for j in range(self.width):
                    if self.world[i][j].id == 2:
                        if self.world[i][j - 1].id == 1 and random.randint(0, c) == 1 and j > 0:
                            self.world[i][j - 1].id = 2
                            self.world[i][j - 1].collision = False
                            self.world[i][j - 1].height = 1
                        if self.world[i][j + 1].id == 1 and random.randint(0, c) == 1 and j < self.width - 1:
                            self.world[i][j + 1].id = 2
                            self.world[i][j + 1].collision = False
                            self.world[i][j + 1].height = 1
                        if self.world[i - 1][j].id == 1 and random.randint(0, c) == 1 and i > 0:
                            self.world[i - 1][j].id = 2
                            self.world[i - 1][j].collision = False
                            self.world[i - 1][j].height = 1
                        if self.world[i + 1][j].id == 1 and random.randint(0, c) == 1 and i < self.height - 1:
                            self.world[i + 1][j].id = 2
                            self.world[i + 1][j].collision = False
                            self.world[i + 1][j].height = 1
        print("--- Build desert: %s seconds ---" % (time.time() - start_time))

        # Generate water
        start_time = time.time()
        for i in range(self.height):
            for j in range(self.width):
                if random.randint(0, 1200) == 1:
                    for y in range(i, i + 10):
                        for x in range(j, j + 10):
                            if 0 < y < self.height - 1 and 0 < x < self.width - 1:
                                self.world[y][x].id = 3
                                self.world[y][x].collision = True
                                self.world[y][x].height = 0
        print("--- Generate water: %s seconds ---" % (time.time() - start_time))

        # Build on water
        start_time = time.time()
        for c in range(2, 8):
            for i in range(self.height):
                for j in range(self.width):
                    if self.world[i][j].id == 3:
                        if random.randint(0, c) == 1 and j > 0:
                            self.world[i][j - 1].id = 3
                            self.world[i][j - 1].collision = True
                            self.world[i][j - 1].height = 0
                            # self.world[self.world.index(i)-1] = Block(3, self.world[self.world.index(i)-1].x, self.world[self.world.index(i)-1].y)
                        if random.randint(0, c) == 1 and j < self.width - 1:
                            self.world[i][j + 1].id = 3
                            self.world[i][j + 1].collision = True
                            self.world[i][j + 1].height = 0
                            # self.world[self.world.index(i)+1] = Block(3, self.world[self.world.index(i)+1].x, self.world[self.world.index(i) + 1].y)
                        if random.randint(0, c) == 1 and i > 0:
                            self.world[i - 1][j].id = 3
                            self.world[i - 1][j].collision = True
                            self.world[i - 1][j].height = 0
                            # self.world[self.world.index(i)-self.width] = Block(3, self.world[self.world.index(i)-self.width].x, self.world[self.world.index(i) - self.width].y)
                        if random.randint(0, c) == 1 and i < self.height - 1:
                            self.world[i + 1][j].id = 3
                            self.world[i + 1][j].collision = True
                            self.world[i + 1][j].height = 0
                            # self.world[self.world.index(i)+self.width] = Block(3, self.world[self.world.index(i)+self.width].x, self.world[self.world.index(i) + self.width].y)
        print("--- Generate Lakes: %s seconds ---" % (time.time() - start_time))

        # Remove single block islands
        start_time = time.time()
        for i in range(self.height):
            for j in range(self.width):
                if self.world[i][j].id == 3:
                    if j > 0 and j < self.width - 1 and i > 0 and i < self.height - 1:
                        if self.world[i + 1][j].id == 3 and self.world[i - 1][j].id == 3 and self.world[i][
                            j + 1].id == 3 and self.world[i][j - 1].id == 3:
                            self.world[i][j].id = 3
                            self.world[i][j].collision = True
                            self.world[i][j].height = 0
        print("--- Remove single block islands: %s seconds ---" % (time.time() - start_time))

        # Generate Trees
        for i in range(self.height):
            for j in range(self.width):
                if self.world[i][j].id == 1 and random.randint(0, 100) == 1:
                    self.world[i][j].entity = Entity(100, True)
                    self.world[i][j].entity.entity_face = 2
        print("--- Generate Trees: %s seconds ---" % (time.time() - start_time))
        start_time = time.time()






    def get_world(self):
        return self.world










    # Generate sand
        #start_time = time.time()
        #for i in range(self.height):
            #for j in range(self.width):
                #if self.world[i][j].id == 3:
                    #if i > 0 and self.world[i - 1][j].id == 1:
                    #    self.world[i - 1][j].id = 2
                    #if i < self.height - 1 and self.world[i + 1][j].id == 1:
                    #    self.world[i + 1][j].id = 2
                    #if j > 0 and self.world[i][j - 1].id == 1:
                    #    self.world[i][j - 1].id = 2
                    #if j < self.width - 1 and self.world[i][j + 1].id == 1:
                    #    self.world[i][j + 1].id = 2
        #print("--- Generate sand: %s seconds ---" % (time.time() - start_time))

        # Build on sand - Add 2 or 3 block of sand around water
        #start_time = time.time()
        #for c in range(2, 5):
            #for i in range(self.height):
                #for j in range(self.width):
                    #if self.world[i][j].id == 2:
                        #if random.randint(0, c) == 1 and i > 0 and self.world[i - 1][j].id == 1:
                        #    self.world[i - 1][j].id = 2
                        #if random.randint(0, c) == 1 and i < self.height - 1 and self.world[i + 1][j].id == 1:
                        #    self.world[i + 1][j].id = 2
                        #if random.randint(0, c) == 1 and j > 0 and self.world[i][j - 1].id == 1:
                        #    self.world[i][j - 1].id = 2
                        #if random.randint(0, c) == 1 and j < self.width - 1 and self.world[i][j + 1].id == 1:
                        #    self.world[i][j + 1].id = 2
        #print("--- Expand sand: %s seconds ---" % (time.time() - start_time))


