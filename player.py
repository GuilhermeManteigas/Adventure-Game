import threading
import time
import pygame
from resources import Resources
from random import randrange

class Player():

    def __init__(self, x, y):
        image_resources = Resources().get_player()
        #pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.health = 100
        self.speed = 2
        self.index = 0
        self.images_idle = image_resources[0]
        self.images_right = image_resources[1]
        self.images_left = []
        #self.load_sprites()
        self.image = self.images_idle[self.index]
        self.hand_image = ""
        self.hand_shake = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.hand_movement = 0
        self.hitbox = 0
        self.inventory = [None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None]
        self.inventory_full = False
        self.looking_direction = False
        self.last_move = time.time()
        self.max_inventory_stack = 2


        #player_movement = threading.Thread(target=self.idle)
        #player_movement.start()



        #self.image = pygame.image.load('player.png').convert_alpha()

    #def load_sprites(self):
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_000.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_001.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_002.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_003.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_004.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_005.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_006.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_007.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_008.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_009.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_010.png').convert_alpha())
        #self.images_idle.append(pygame.image.load('images/Player/Minotaur_01_Idle_011.png').convert_alpha())

        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_000.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_000.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_001.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_001.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_002.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_002.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_003.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_003.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_004.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_004.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_005.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_005.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_006.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_006.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_007.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_007.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_008.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_008.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_009.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_009.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_010.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_010.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_011.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_011.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_012.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_012.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_013.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_013.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_014.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_014.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_015.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_015.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_016.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_016.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_017.png').convert_alpha())
        #self.images_right.append(pygame.image.load('images/Player/Minotaur_01_Walking_017.png').convert_alpha())


    def get_image(self):
        #print(self.hand_image)
        temp = self.image.copy()
        #img = pygame.image.load(self.hand_image)
        #angle = -150 - self.hand_shake[self.hand_movement]
        angle = 5 + self.hand_shake[self.hand_movement]

        if self.hand_movement >= len(self.hand_shake)-1:
            self.hand_movement = 0
        self.hand_movement += 1
        #self.hand_movement += 1
        #angle = self.hand_movement

        if self.hand_image != "":
            #rotated_image = pygame.transform.rotate(self.hand_image, randrange(50))
            #temp.blit(rotated_image, (56, 24))
            # offset from pivot to center
            #image_rect = self.hand_image.get_rect(bottomright=(56 + 27, 24 + 11))
            #offset_center_to_pivot = pygame.math.Vector2((56+27, 24+11)) - image_rect.center

            # roatated offset from pivot to center
            #rotated_offset = offset_center_to_pivot.rotate(-angle)

            # roatetd image center
            #rotated_image_center = (50, 50)

            # get a rotated image
            #rotated_image = pygame.transform.rotate(self.hand_image, angle)
            #rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
            #temp.blit(rotated_image, rotated_image_rect) #(50,20))

            rotated_image = pygame.transform.rotozoom(self.hand_image, -angle, 1)  # Rotate the image.
            rotated_offset = pygame.math.Vector2(0, 0).rotate(angle)  # Rotate the offset vector.
            # Add the offset vector to the center/pivot point to shift the rect.
            rect = rotated_image.get_rect(center=(65, 50) + rotated_offset)
            temp.blit(rotated_image, rect)



        if self.looking_direction:
            return pygame.transform.flip(temp, True, False)
        else:
            return temp


    def move(self, x, y):
        if self.x == x:
            pass
        elif self.x < x:
            self.looking_direction = False
        else:
            self.looking_direction = True
        self.x = x
        self.y = y
        self.update_sprite()
        self.last_move = time.time()

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
            if i is not None and i[0] == drop[0] and i[1] < self.max_inventory_stack:
                self.inventory[idx] = (i[0], i[1] + drop[1])
                item_added = True
                return True
        if not item_added:
            for idx, i in enumerate(self.inventory):
                if i is None:
                    self.inventory[idx] = (drop[0], drop[1])
                    return True

            print("Drop failed to be added to the inventory")
            return False

    def has_space_for_drop(self, drop):
        item_added = False
        for idx, i in enumerate(self.inventory):
            if i is not None and i[0] == drop[0] and i[1] < self.max_inventory_stack:
                item_added = True
                return True
        if not item_added:
            for idx, i in enumerate(self.inventory):
                if i is None:
                    return True
            return False
