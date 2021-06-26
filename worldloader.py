import copy
import os
import pickle
import time
from datetime import date

import numpy as np
from PIL import Image

GAME_NAME = "GuiGame"

class Worldloader:
    def __init__(self):
        self.world_in_use = 0
        self.worlds = [None, None, None, None, None, None, None, None]
        self.worlds_minimaps = [None, None, None, None, None, None, None, None]
        self.load()

    def load(self):
        filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world0.save"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world0.save"
            with open(filename, "rb") as f:
                self.worlds[0] = pickle.load(f)
                self.worlds_minimaps[0] = self.map_to_img(self.worlds[0][0], 0)
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world1.save"
            with open(filename, "rb") as f:
                self.worlds[1] = pickle.load(f)
                self.worlds_minimaps[1] = self.map_to_img(self.worlds[1][0], 1)
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world2.save"
            with open(filename, "rb") as f:
                self.worlds[2] = pickle.load(f)
                self.worlds_minimaps[2] = self.map_to_img(self.worlds[2][0], 2)
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world3.save"
            with open(filename, "rb") as f:
                self.worlds[3] = pickle.load(f)
                self.worlds_minimaps[3] = self.map_to_img(self.worlds[3][0], 3)
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world4.save"
            with open(filename, "rb") as f:
                self.worlds[4] = pickle.load(f)
                self.worlds_minimaps[4] = self.map_to_img(self.worlds[4][0], 4)
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world5.save"
            with open(filename, "rb") as f:
                self.worlds[5] = pickle.load(f)
                self.worlds_minimaps[5] = self.map_to_img(self.worlds[5][0], 5)
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world6.save"
            with open(filename, "rb") as f:
                self.worlds[6] = pickle.load(f)
                self.worlds_minimaps[6] = self.map_to_img(self.worlds[6][0], 6)
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world7.save"
            with open(filename, "rb") as f:
                self.worlds[7] = pickle.load(f)
                self.worlds_minimaps[7] = self.map_to_img(self.worlds[7][0], 7)
        except:
            pass

    def save(self, world, player, drop_map):
        # FORMAT: [World, Player, Drop Map, Last time played]
        today = date.today()
        p = [player.x, player.y, player.health, player.inventory, player.inventory_full]
        filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world" + str(self.world_in_use) + ".save"
        #print(filename)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as f:
            save = [world, p, drop_map, today.strftime("%d/%m/%Y")]
            pickle.dump(save, f)

    def map_to_img(self, world, num):
        filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\minimap" + str(num) + ".png"
        if not os.path.exists(filename):

            data = np.zeros((len(world), len(world), 3), dtype=np.uint8)

            for x in range(len(world)):
                for y in range(len(world)):
                    if world[x][y].id == 1:
                        data[x, y] = [128, 165, 63]
                    elif world[x][y].id == 2:
                        data[x, y] = [252, 198, 3]
                    elif world[x][y].id == 3:
                        data[x, y] = [3, 190, 252]

            Image.fromarray(data).save(filename)

        return filename
