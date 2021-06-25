import threading
import time
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.health = 100
        self.speed = 2
        self.index = 0
        self.images_idle = []
        self.images_right = []
        self.images_left = []
        self.load_sprites()
        self.image = self.images_idle[self.index]
        self.hitbox = 0
        self.inventory = []
        self.inventory_full = False


        player_movement = threading.Thread(target=self.idle)
        player_movement.start()



        #self.image = pygame.image.load('player.png').convert_alpha()

    def load_sprites(self):
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_000.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_001.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_002.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_003.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_004.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_005.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_006.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_007.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_008.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_009.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_010.png').convert_alpha())
        self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_011.png').convert_alpha())

        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_000.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_000.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_001.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_001.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_002.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_002.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_003.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_003.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_004.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_004.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_005.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_005.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_006.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_006.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_007.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_007.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_008.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_008.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_009.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_009.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_010.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_010.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_011.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_011.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_012.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_012.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_013.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_013.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_014.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_014.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_015.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_015.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_016.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_016.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_017.png').convert_alpha())
        self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_017.png').convert_alpha())

    def move(self, x, y):
        self.x = x
        self.y = y
        self.update_sprite()

    def update_sprite(self):
        if self.index >= len(self.images_right) - 1:
            self.index = 0
        else:
            self.image = self.images_right[self.index]
            self.index += 1

    def idle(self):
        idx = 0
        x1 = self.x
        y1 = self.y
        while True:
            if x1 == self.x and y1 == self.y:
                if idx >= len(self.images_idle) - 1:
                    idx = 0
                else:
                    self.image = self.images_idle[idx]
                    idx += 1
            else:
                x1 = self.x
                y1 = self.y

            time.sleep(0.080)

    #player_movement = threading.Thread(target=idle)
    #player_movement.start()

    #def start_thread(self):
        #player_movement = threading.Thread(target=self.idle)
        #player_movement.start()

    def get_inventory(self):
        return self.inventory

    def add_to_inventory(self, drop):
        item_added = False
        for idx, i in enumerate(self.inventory):
            if i[0] == drop[0]:
                self.inventory[idx] = (i[0], i[1] + drop[1])
                #i[1] += drop[1]
                item_added = True
                return True
        if not item_added:
            if len(self.inventory) < 20:
                self.inventory.append((drop[0], drop[1]))
                return True
            else:
                self.inventory_full = True
                return False

