import os
from worldgenerator import WorldGenerator
from player import Player
import pygame
import threading
import time
from resources import Resources
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

night_value = 0
night_filter = pygame.Surface(size)
night_filter.fill((0, 0, 0))
game_days = 0
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
BLUE = (0, 0, 255)

world_size = 500
world = WorldGenerator(world_size, world_size).get_world()
world_section = []
Cube_Size = 30
scroll = [0, 0]
true_scroll = [0, 0]

image_resources = Resources().get_images()


def update_world_section():
    global world_section
    while True:
        #start_time = time.time()
        temp_world = []

        for x in range(int(player.x / 30) - 30, int(player.x / 30) + 30):
            for y in range(int(player.y/30) - 30, int(player.y/30) + 30):
                if 0 <= x < world_size - 1 and 0 <= y < world_size - 1:
                    temp_world.append(world[x][y])

        world_section = temp_world[:]
        #print("--- %s seconds ---" % (time.time() - start_time))
        time.sleep(Game_Tick*5)

def draw_world():
    for i in world_section:
        screen.blit(image_resources[i.id][i.block_face], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]))
        #i.hitbox = pygame.Rect((i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]), (Cube_Size, Cube_Size))

def draw_worldold():
    screen_width, screen_height = screen.get_size()
    for idx, i in enumerate(world_section):
        if (player.x - (screen_width/2)) - Cube_Size * 5 < i.x * Cube_Size < (player.x + (screen_width/2)) + Cube_Size * 5 and (player.y - (screen_height/2)) - Cube_Size * 5 < i.y * Cube_Size < (player.y + (screen_height/2)) + Cube_Size * 5:
            if i.id != 0:
                screen.blit(image_resources[i.id][i.block_face], (i.x * Cube_Size - scroll[0] , i.y * Cube_Size - scroll[1] ))
                i.hitbox = pygame.Rect((i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]),(Cube_Size, Cube_Size))
                #pygame.draw.rect(screen, BLACK, (i.x * Cube_Size - scroll[0],i.y * Cube_Size - scroll[1], 10, 10))
                #if i.id == 3:
                    #pygame.draw.rect(screen, GREEN, i.hitbox, 1)
            #if i.entity != 0:
                #screen.blit(image_resources[i.entity], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]))


def draw_entities():
    a, b = light.get_size()

    if night_value > 0:
        night_filter.fill((night_value, night_value, night_value))

    for i in world_section:
            if i.entity.id != 0:
                i.entity.update(game_days)
                screen.blit(image_resources[i.entity.id][i.entity.entity_face], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1] - image_resources[i.entity.id][i.entity.entity_face].get_height() + Cube_Size))
                i.entity.hitbox = pygame.Rect((i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]), (Cube_Size, Cube_Size))
                if night_value > 0:
                    night_filter.blit(light, (i.x * Cube_Size - scroll[0] - a/2, i.y * Cube_Size - scroll[1] - b/2))


def show_fps(window, clock):
    FPS_FONT = pygame.font.SysFont("Verdana", 10)
    color = pygame.Color("white")
    fps_overlay = FPS_FONT.render(str(int(clock.get_fps())), True, color)
    window.blit(fps_overlay, (55, 0))
    # Coords on screen
    coors_overlay = FPS_FONT.render(str((int(player.x / Cube_Size), int(player.y / Cube_Size))), True, color)
    window.blit(coors_overlay, (0, 0))



def collision_checker(x, y):

    if world[int(x / 30)][int(y / 30)].entity.collision:
        pass
    elif world[int(x/30)][int(y/30)].collision:
        pass
    elif int(x/30) < 25 or int(y/30) < 20 or int(x/30) > world_size - 25 or int(y/30) > world_size - 20:
        pass
    else:
        player.move(x, y)


def block_face_checker():
    for x in range(world_size-1):
        for y in range(world_size-1):
            if world[x][y].height == 1:

                #   O X O    O O O
                #   X B X    O B O
                #   O X O    O O O
                if world[x][y - 1].height == 1 and world[x - 1][y].height == 1 and world[x + 1][y].height == 1 and world[x][y + 1].height == 1:
                    world[x][y].block_face = 4
                elif world[x][y - 1].height < 1 and world[x - 1][y].height < 1 and world[x + 1][y].height < 1 and world[x][y + 1].height < 1:
                    world[x][y].block_face = 9

                #   O X O    O X O   O X O   O O O
                #   X B O    O B X   X B X   X B X
                #   O X O    O X O   O O O   O X O
                elif world[x][y - 1].height < 1 and world[x - 1][y].height < 1 and world[x][y + 1].height < 1:
                    world[x][y].block_face = 10
                elif world[x][y - 1].height < 1 and world[x + 1][y].height < 1 and world[x][y + 1].height < 1:
                    world[x][y].block_face = 11
                elif world[x][y - 1].height < 1 and world[x - 1][y].height < 1 and world[x + 1][y].height < 1:
                    world[x][y].block_face = 12
                elif world[x][y + 1].height < 1 and world[x - 1][y].height < 1 and world[x + 1][y].height < 1:
                    world[x][y].block_face = 13

                #   O X O    O X O   O O O   O O O   O X O   O O O
                #   X B O    O B X   X B O   O B X   O B O   X B X
                #   O O O    O O O   O X O   O X O   O X O   O O O
                elif world[x][y - 1].height < 1 and world[x - 1][y].height < 1:
                    world[x][y].block_face = 0
                elif world[x][y - 1].height < 1 and world[x + 1][y].height < 1:
                    world[x][y].block_face = 2
                elif world[x][y + 1].height < 1 and world[x - 1][y].height < 1:
                    world[x][y].block_face = 6
                elif world[x][y + 1].height < 1 and world[x + 1][y].height < 1:
                    world[x][y].block_face = 8
                elif world[x][y - 1].height < 1 and world[x][y + 1].height < 1:
                    world[x][y].block_face = 14
                elif world[x - 1][y].height < 1 and world[x + 1][y].height < 1:
                    world[x][y].block_face = 15

                #   O X O    O O O   O O O   O O O
                #   O B O    X B O   O B X   O B O
                #   O O O    O O O   O O O   O X O
                elif world[x][y - 1].height < 1:
                    world[x][y].block_face = 1
                elif world[x - 1][y].height < 1:
                    world[x][y].block_face = 3
                elif world[x + 1][y].height < 1:
                    world[x][y].block_face = 5
                elif world[x][y + 1].height < 1:
                    world[x][y].block_face = 7

            #Liquid Blocks
            elif world[x][y].height == 0:
                if world[x][y - 1].height == 1:
                    world[x][y].block_face = 1
                else:
                    world[x][y].block_face = 0

#def update_entities

def time_handler():
    #update_visible_world = threading.Thread(target=update_world_section)
    #update_visible_world.start()
    # 24 H = 1440 Min ==> a in game day will take 24 min
    # 6 AM Morning & 10 PM Night
    timer = 1300#420 # 7 AM
    global night_value
    global game_days
    while game_running:
        if timer >= 1440:
            game_days += 1
            timer = 0
        elif 1320 < timer < 1380:
            night_value += 2
            #night_filter.fill((night_value, night_value, night_value))
            #night_filter.set_alpha(night_value)  # alpha level
        elif 360 < timer < 420:
            night_value -= 2
            #night_filter.fill((night_value, night_value, night_value))
            #night_filter.set_alpha(night_value)

        #night_filter.fill((night_value, night_value, night_value))

        timer += 1

        time.sleep(0.01)#time.sleep(1)


def player_movement_handler():
    while game_running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            collision_checker(player.x - player.speed, player.y)
        elif keys[pygame.K_d]:
            collision_checker(player.x + player.speed, player.y)
        if keys[pygame.K_w]:
            collision_checker(player.x, player.y - player.speed)
        if keys[pygame.K_s]:
            collision_checker(player.x, player.y + player.speed)

        time.sleep(Game_Tick/15)


player_movement = threading.Thread(target=player_movement_handler)
player_movement.start()

update_visible_world = threading.Thread(target=update_world_section)
update_visible_world.start()

time_handler = threading.Thread(target=time_handler)
time_handler.start()


block_face_checker()


light = pygame.image.load('circle2.png').convert_alpha()

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

    #screen.fill(BLUE)

    start_time = time.time()
    screen_width, screen_height = screen.get_size()
    true_scroll[0] += (player.x - true_scroll[0] - (screen_width / 2)) / 20
    true_scroll[1] += (player.y - true_scroll[1] - (screen_height / 2)) / 20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    print("--- A: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    draw_world()
    print("--- Draw World: %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    draw_entities()
    print("--- Draw Entities: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    rect = player.image.get_rect()
    rect.center = player.x - scroll[0], player.y - scroll[1] - (player.image.get_height() - Cube_Size - 5)  #fixed the size because was messign up colisions now colision point is at feet
    player.hitbox = pygame.Rect(rect)
    screen.blit(player.image, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    print("--- Player: %s seconds ---" % (time.time() - start_time))
    #screen.blit(player.image, (player.x - scroll[0], player.y - scroll[1]))
    start_time = time.time()
    show_fps(screen, clock)
    print("--- FPS: %s seconds ---" % (time.time() - start_time))

    if night_value > 0:
        start_time = time.time()

        #night_filter.blit(light, (230, 30))
        #night_filter.blit(light, (330, 30))
        screen.blit(night_filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        print("--- Night: %s seconds ---" % (time.time() - start_time))

    pygame.display.flip()

    clock.tick(120)

pygame.quit()