import os
from worldgenerator import WorldGenerator
from player import Player
import pygame
import threading
import time
import random


os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

size = (1280, 720)
#screen = pygame.display.set_mode(size, pygame.SCALED | pygame.RESIZABLE) #pygame.FULLSCREEN
#screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
#screen = pygame.display.set_mode(size, pygame.RESIZABLE | pygame.SCALED)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adventure Game")

black = (0, 0, 0)

Game_Map_Size = 30
Game_Tick = 0.1
game_running = True
# The loop will carry on until the user exit the game (e.g. clicks the close button).
playing = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
# Player declaration
player = Player(1000, 1000)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

world_size = 100
world = WorldGenerator(100, 100).get_world()
world_section = []
Cube_Size = 30
scroll = [0, 0]
true_scroll = [0, 0]


def load_image_resources():
    ############### Blocks ##############################
    images = []
    ########## index 0 reserved for future use ##########
    images.append(pygame.image.load('dirt.png').convert())
    #####################################################
    images.append(pygame.image.load('grass.png').convert())  # id = 1
    images.append(pygame.image.load('sand.png').convert())  # id = 2
    images.append(pygame.image.load('water.png').convert())  # id = 3

    return images


image_resources = load_image_resources()

def update_world_section():
    global world_section
    while True:
        #start_time = time.time()
        temp_world = []

        for i in range(int(player.y/30) - 30, int(player.y/30) + 30):
            for j in range(int(player.x/30) - 30, int(player.x/30) + 30):
                if 0 < i < world_size - 1 and 0 < j < world_size - 1:
                    temp_world.append(world[i][j])

        world_section = temp_world[:]
        #print("--- %s seconds ---" % (time.time() - start_time))
        time.sleep(Game_Tick*5)


def draw_world():
    screen_width, screen_height = screen.get_size()
    counter = 0
    for idx, i in enumerate(world_section):
        if (player.x - (screen_width/2)) - Cube_Size * 5 < i.x * Cube_Size < (player.x + (screen_width/2)) + Cube_Size * 5 and (player.y - (screen_height/2)) - Cube_Size * 5 < i.y * Cube_Size < (player.y + (screen_height/2)) + Cube_Size * 5:
            if i.id != 0:
                screen.blit(image_resources[i.id], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]))

        counter = idx


def show_fps(window, clock):
    FPS_FONT = pygame.font.SysFont("Verdana", 15)
    black = pygame.Color("black")
    fps_overlay = FPS_FONT.render(str(int(clock.get_fps())), True, black)
    window.blit(fps_overlay, (0, 0))


def player_movement_handler():
    while game_running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.move(player.x - player.speed, player.y)
        elif keys[pygame.K_d]:
            player.move(player.x + player.speed, player.y)
        if keys[pygame.K_w]:
            player.move(player.x, player.y - player.speed)
        if keys[pygame.K_s]:
            player.move(player.x, player.y + player.speed)

        time.sleep(Game_Tick/15)


player_movement = threading.Thread(target=player_movement_handler)
player_movement.start()

update_visible_world = threading.Thread(target=update_world_section)
update_visible_world.start()




#pygame.display.toggle_fullscreen()

# -------- Main Program Loop -----------
while playing:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            playing = False  # Flag that we are done so we exit this loop
        if (event.type is pygame.KEYDOWN and event.key == pygame.K_f):
            print("f")
            if screen.get_flags() & pygame.FULLSCREEN:
                pygame.display.set_mode(size)
            else:
                pygame.display.set_mode(size, pygame.FULLSCREEN)

    screen.fill(WHITE)

    screen_width, screen_height = screen.get_size()
    true_scroll[0] += (player.x - true_scroll[0] - (screen_width / 2)) / 20
    true_scroll[1] += (player.y - true_scroll[1] - (screen_height / 2)) / 20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    draw_world()

    screen.blit(player.image, (player.x - scroll[0], player.y - scroll[1]))
    show_fps(screen, clock)





    pygame.display.flip()

    clock.tick(120)

pygame.quit()