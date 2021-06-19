import os
from worldgenerator import WorldGenerator
import pygame
import threading
import time
import random



os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()


FPS_FONT = pygame.font.SysFont("Verdana", 15)

black = (0, 0, 0)

Game_Map_Size = 30
Game_Tick = 0.1
game_running = True

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (1280, 720)
#screen = pygame.display.set_mode(size, pygame.SCALED | pygame.RESIZABLE) #pygame.FULLSCREEN
#screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
#screen = pygame.display.set_mode(size, pygame.RESIZABLE | pygame.SCALED)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adventure Game")

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

def show_fps(window, clock):
    fps_overlay = FPS_FONT.render(str(int(clock.get_fps())), True, black)
    window.blit(fps_overlay, (50, 50))

def player_movement_handler():
    global screen
    while game_running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            #if screen.get_flags() & pygame.FULLSCREEN:
            #    pygame.display.set_mode(size)
            #else:
            #    pygame.display.set_mode(size)
            #    pygame.display.set_mode(size, pygame.FULLSCREEN)
            print("d")
            global screen
            screen = pygame.display.set_mode(size)

        time.sleep(Game_Tick)


player_movement = threading.Thread(target=player_movement_handler)
player_movement.start()

World_width = 1000
World_height = 1000

world = WorldGenerator(World_width, World_height).get_world()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        if (event.type is pygame.KEYDOWN and event.key == pygame.K_f):
            print("f")
            if screen.get_flags() & pygame.FULLSCREEN:
                pygame.display.set_mode(size)
            else:
                pygame.display.set_mode(size, pygame.FULLSCREEN)

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 30, 30), 0)


    pygame.display.flip()

    show_fps(screen, clock)
    clock.tick(120)

pygame.quit()