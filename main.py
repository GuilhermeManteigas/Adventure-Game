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
BLUE = (0, 0, 255)

world_size = 500
world = WorldGenerator(world_size, world_size).get_world()
world_section = []
Cube_Size = 30
scroll = [0, 0]
true_scroll = [0, 0]

def load_image_resources():
    ############### Blocks ##############################
    images = [None] * 500
    ########## index 0 reserved for future use ##########
    #images.append(pygame.image.load('dirt.png').convert())
    #####################################################
    images[1] = [pygame.image.load('images/Blocks/grass/grass1.png').convert(), pygame.image.load('images/Blocks/grass/grass2.png').convert(), pygame.image.load('images/Blocks/grass/grass3.png').convert(), pygame.image.load('images/Blocks/grass/grass4.png').convert(), pygame.image.load('images/Blocks/grass/grass5.png').convert(), pygame.image.load('images/Blocks/grass/grass6.png').convert(), pygame.image.load('images/Blocks/grass/grass7.png').convert(), pygame.image.load('images/Blocks/grass/grass8.png').convert(), pygame.image.load('images/Blocks/grass/grass9.png').convert(), pygame.image.load('images/Blocks/grass/grass10.png').convert(), pygame.image.load('images/Blocks/grass/grass11.png').convert(), pygame.image.load('images/Blocks/grass/grass12.png').convert(), pygame.image.load('images/Blocks/grass/grass13.png').convert(), pygame.image.load('images/Blocks/grass/grass14.png').convert(), pygame.image.load('images/Blocks/grass/grass15.png').convert(), pygame.image.load('images/Blocks/grass/grass16.png').convert()]
    images[2] = [pygame.image.load('images/Blocks/sand/sand1.png').convert(), pygame.image.load('images/Blocks/sand/sand2.png').convert(), pygame.image.load('images/Blocks/sand/sand3.png').convert(), pygame.image.load('images/Blocks/sand/sand4.png').convert(), pygame.image.load('images/Blocks/sand/sand5.png').convert(), pygame.image.load('images/Blocks/sand/sand6.png').convert(), pygame.image.load('images/Blocks/sand/sand7.png').convert(), pygame.image.load('images/Blocks/sand/sand8.png').convert(), pygame.image.load('images/Blocks/sand/sand9.png').convert(), pygame.image.load('images/Blocks/sand/sand10.png').convert(), pygame.image.load('images/Blocks/sand/sand11.png').convert(), pygame.image.load('images/Blocks/sand/sand12.png').convert(), pygame.image.load('images/Blocks/sand/sand13.png').convert(), pygame.image.load('images/Blocks/sand/sand14.png').convert(), pygame.image.load('images/Blocks/sand/sand15.png').convert(), pygame.image.load('images/Blocks/sand/sand16.png').convert()]
    images[3] = [pygame.image.load('images/Blocks/water/water1.png').convert_alpha(),pygame.image.load('images/Blocks/water/water2.png').convert_alpha()]

    ############### Entities ##############################
    images[100] = pygame.image.load('tree.png').convert()

    return images


image_resources = load_image_resources()


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
    screen_width, screen_height = screen.get_size()
    for idx, i in enumerate(world_section):
        if (player.x - (screen_width/2)) - Cube_Size * 5 < i.x * Cube_Size < (player.x + (screen_width/2)) + Cube_Size * 5 and (player.y - (screen_height/2)) - Cube_Size * 5 < i.y * Cube_Size < (player.y + (screen_height/2)) + Cube_Size * 5:
        #if(player.x - (screen_width / 2)) - Cube_Size * 5 < i.x * Cube_Size < (player.x + (screen_width / 2)) + Cube_Size * 5 and (player.y - (screen_height / 2)) - Cube_Size * 5 < i.y * Cube_Size < (player.y + (screen_height / 2)) + Cube_Size * 5:
            if i.entity.id != 0:
                screen.blit(image_resources[i.entity.id], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1] - image_resources[i.entity.id].get_height() + Cube_Size))
                i.entity.hitbox = pygame.Rect((i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]), (Cube_Size, Cube_Size))
                #pygame.draw.rect(screen, GREEN, i.entity.hitbox, 1)
                #recti = pygame.Rect((x, y), (Cube_Size, Cube_Size))
                #recti.center = x - scroll[0], y - scroll[1]
                #pygame.draw.rect(screen, RED, i.entity.hitbox, 1)

                #image_resources[i.entity].get_height()
                #screen.blit(image_resources[i.entity], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]))

            #if (player.x - (screen_width / 2)) - Cube_Size * 5 < i.x * Cube_Size < (player.x + (screen_width / 2)) + Cube_Size * 5
                #and
                #(player.y - (screen_height / 2)) - Cube_Size * 5 < i.y * Cube_Size < (player.y + (screen_height / 2)) + Cube_Size * 5:


def show_fps(window, clock):
    FPS_FONT = pygame.font.SysFont("Verdana", 15)
    black = pygame.Color("black")
    fps_overlay = FPS_FONT.render(str(int(clock.get_fps())), True, black)
    window.blit(fps_overlay, (0, 0))
    # Coords on screen
    coors_overlay = FPS_FONT.render(str((int(player.x / Cube_Size), int(player.y / Cube_Size))), True, black)
    window.blit(coors_overlay, (0, 20))
    #world[int(player.y / Cube_Size)+1][int(player.x / Cube_Size)+1].id = 69
    #coors_overlay = FPS_FONT.render(str((player.x / Cube_Size, player.y / Cube_Size)), True, black)
    #window.blit(coors_overlay, (0, 40))
    #coors_overlay = FPS_FONT.render(str((player.x, player.y)), True, black)
    #window.blit(coors_overlay, (0, 60))

def collision_checker(x, y):
    #blocks_around = []
    #blocks_around.append(world[(int(player.x / Cube_Size)+1) - 1][(int(player.y / Cube_Size)+1)])
    #blocks_around.append(world[(int(player.x / Cube_Size) + 1) + 1][(int(player.y / Cube_Size) + 1)])
    #blocks_around.append(world[(int(player.x / Cube_Size) + 1)][(int(player.y / Cube_Size) + 1) - 1])
    #blocks_around.append(world[(int(player.x / Cube_Size) + 1)][(int(player.y / Cube_Size) + 1) + 1])

    #blocks_around.append(world[(int(player.x / Cube_Size) + 1) - 1][(int(player.y / Cube_Size) + 1) - 1])
    #blocks_around.append(world[(int(player.x / Cube_Size) + 1) - 1][(int(player.y / Cube_Size) + 1) + 1])
    #blocks_around.append(world[(int(player.x / Cube_Size) + 1) + 1][(int(player.y / Cube_Size) + 1) - 1])
    #blocks_around.append(world[(int(player.x / Cube_Size) + 1) + 1][(int(player.y / Cube_Size) + 1) + 1])

    ## More efficient with if before every block append! i think!
    #for i in blocks_around:
    #    if not i.collision and not i.entity.collision:
    #        blocks_around.remove(i)

    #print("===============================")
    #print("Checking ", int(x / 30), int(y / 30))
    #print(world[int(x / 30)][int(y / 30)].x, world[int(x / 30)][int(y / 30)].y, world[int(x / 30)][int(y / 30)].id,world[int(x / 30)][int(y / 30)].collision)

    if world[int(x / 30)][int(y / 30)].entity.collision:
        pass
        #print("Entity Collision")
        #recti = world[int(x / 30)][int(y / 30)].entity.hitbox
        #rectp = player.hitbox
        #if rectp.colliderect(recti):
            #world[int(player.x / Cube_Size)][int(player.y / Cube_Size)].id = 69
            #print("colided")
        #else:
            #player.move(x, y)

    elif world[int(x/30)][int(y/30)].collision:
        pass
    elif int(x/30) < 25 or int(y/30) < 20 or int(x/30) > world_size - 25 or int(y/30) > world_size - 20:
        pass
    else:
        #print("Pass")
        player.move(x, y)

    #print("===============================")

def block_face_checker():
    #MAKE IT RUN ONLY AT THE BEGGINING OF THE GAME
    while game_running:
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

                    elif world[x][y - 1].height < 1:
                        world[x][y].block_face = 1
                    elif world[x - 1][y].height < 1:
                        world[x][y].block_face = 3
                    elif world[x + 1][y].height < 1:
                        world[x][y].block_face = 5
                    elif world[x][y + 1].height < 1:
                        world[x][y].block_face = 7

                elif world[x][y].height == 0:
                    if world[x][y - 1].height == 0 and world[x - 1][y].height == 0 and world[x + 1][y].height == 0 and world[x][y + 1].height == 0:
                        world[x][y].block_face = 0
                    else:
                        world[x][y].block_face = 1


        time.sleep(1)



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

block_checker = threading.Thread(target=block_face_checker)
block_checker.start()

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

    #screen.fill(BLUE)

    screen_width, screen_height = screen.get_size()
    true_scroll[0] += (player.x - true_scroll[0] - (screen_width / 2)) / 20
    true_scroll[1] += (player.y - true_scroll[1] - (screen_height / 2)) / 20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    draw_world()
    draw_entities()

    rect = player.image.get_rect()
    rect.center = player.x - scroll[0], player.y - scroll[1] - (player.image.get_height() - Cube_Size - 5)  #fixed the size because was messign up colisions now colision point is at feet
    player.hitbox = pygame.Rect(rect)
    screen.blit(player.image, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    #screen.blit(player.image, (player.x - scroll[0], player.y - scroll[1]))
    show_fps(screen, clock)



    pygame.display.flip()

    clock.tick(120)

pygame.quit()