import os
import pickle

GAME_NAME = "GuiGame"

class Options:
    def __init__(self):
        self.fullscreen = False
        self.languages = ["English", "Portuguese", "French", "German"]
        self.language = 0
        self.fps = True
        self.coords = True
        self.load()

    def update_fullscreen(self):
        if self.fullscreen:
            self.fullscreen = False
        else:
            self.fullscreen = True

    def update_fps(self):
        if self.fps:
            self.fps = False
        else:
            self.fps = True

    def update_coords(self):
        if self.coords:
            self.coords = False
        else:
            self.coords = True

    def update_language(self, num):
        # num should be 1 or -1
        if 0 <= self.language + num < len(self.languages):
            self.language += num
        elif self.language + num < 0:
            self.language = len(self.languages)
        elif self.language + num >= len(self.languages):
            self.language = 0

    def load(self):
        filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\options.save"
        print(filename)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        try:
            with open(filename, "rb") as f:
                tmp_dict = pickle.load(f)
                self.__dict__.update(tmp_dict)
                print("loaded")
        except:
            pass

    def save(self):
        filename = os.getenv('APPDATA') + "\\" + GAME_NAME + "\options.save"
        print(filename)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as f:
            pickle.dump(self.__dict__, f)

