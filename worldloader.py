import copy
import os
import pickle
from datetime import date

GAME_NAME = "GuiGame"

class Worldloader:
    def __init__(self):
        self.world_in_use = 0
        self.worlds = [None, None, None, None, None, None, None, None]
        self.load()

    def load(self):
        filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world0.save"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world0.save"
            with open(filename, "rb") as f:
                self.worlds[0] = pickle.load(f)
                #self.__dict__.update(tmp_dict)
                #self.worlds[0]
                print("loaded")
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world1.save"
            with open(filename, "rb") as f:
                #tmp_dict = pickle.load(f)
                #self.__dict__.update(tmp_dict)
                print("loaded")
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world2.save"
            with open(filename, "rb") as f:
                #tmp_dict = pickle.load(f)
                #self.__dict__.update(tmp_dict)
                print("loaded")
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world3.save"
            with open(filename, "rb") as f:
                #tmp_dict = pickle.load(f)
                #self.__dict__.update(tmp_dict)
                print("loaded")
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world4.save"
            with open(filename, "rb") as f:
                #tmp_dict = pickle.load(f)
                #self.__dict__.update(tmp_dict)
                print("loaded")
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world5.save"
            with open(filename, "rb") as f:
                #tmp_dict = pickle.load(f)
                #self.__dict__.update(tmp_dict)
                print("loaded")
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world6.save"
            with open(filename, "rb") as f:
                #tmp_dict = pickle.load(f)
                #self.__dict__.update(tmp_dict)
                print("loaded")
        except:
            pass
        try:
            filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\world7.save"
            with open(filename, "rb") as f:
                #tmp_dict = pickle.load(f)
                #self.__dict__.update(tmp_dict)
                print("loaded")
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

