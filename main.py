import os
from worldgenerator import WorldGenerator
from player import Player
import pygame
import threading
import time
from resources import Resources
from drop import Drop
from entity import Entity
import random


os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

size = (1280, 720)
#screen = pygame.display.set_mode(size, pygame.SCALED | pygame.RESIZABLE) #pygame.FULLSCREEN
#screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
#screen = pygame.display.set_mode(size, pygame.RESIZABLE | pygame.SCALED)


screen = pygame.display.set_mode(size, pygame.SCALED)

#screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adventure Game")

black = (0, 0, 0)

entities_to_remove = []

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
player = Player(2000, 2000)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

world_size = 500
world = WorldGenerator(world_size, world_size).get_world()
drop_map = []
drop_map_section = []
world_section = []
Cube_Size = 30
scroll = [0, 0]
true_scroll = [0, 0]

mouse_position = (0, 0)

image_resources = Resources().get_images()


def update_world_section():
    global world_section
    while True:
        temp_world = []

        for x in range(int(player.x / 30) - 30, int(player.x / 30) + 30):
            for y in range(int(player.y/30) - 30, int(player.y/30) + 30):
                if 0 <= x < world_size - 1 and 0 <= y < world_size - 1:
                    temp_world.append(world[x][y])

        world_section = temp_world[:]
        time.sleep(Game_Tick*5)


def draw_world():
    for i in world_section:
        screen.blit(image_resources[i.id][i.block_face], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]))
        #i.hitbox = pygame.Rect((i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]), (Cube_Size, Cube_Size))


def draw_entities():
    light = image_resources[600][0]
    a, b = light.get_size()
    mouse_x, mouse_y = mouse_position

    if night_value > 0:
        night_filter.fill((night_value, night_value, night_value))

    entity_remover()
    for i in world_section:

            if i.entity.id != 0:
                if i.x == mouse_x and i.y == mouse_y:
                    # Draw Marker
                    screen.blit(image_resources[601][0], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]))
                i.entity.update(game_days)
                screen.blit(image_resources[i.entity.id][i.entity.entity_face], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1] - image_resources[i.entity.id][i.entity.entity_face].get_height() + Cube_Size))
                i.entity.hitbox = pygame.Rect((i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]), (Cube_Size, Cube_Size))
                if i.entity.health < i.entity.max_health:
                    # Draw grey back
                    pygame.draw.rect(screen, (30, 30, 30), (i.x * Cube_Size - scroll[0] - 2, i.y * Cube_Size - scroll[1] + Cube_Size + 10 - 2, 30 + 4, 5 + 4))
                    # Draw life Green/Red
                    if i.entity.health >= i.entity.max_health/2:
                        pygame.draw.rect(screen, (127, 255, 0), (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1] + Cube_Size + 10, i.entity.health / 3.3, 5))
                    else:
                        pygame.draw.rect(screen, (255, 0, 0), (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1] + Cube_Size + 10, i.entity.health / 3.3, 5))

                if night_value > 0:
                    night_filter.blit(light, (i.x * Cube_Size - scroll[0] - a/2, i.y * Cube_Size - scroll[1] - b/2))


def draw_drops():
    for i in drop_map_section:
        screen.blit(image_resources[i.id][i.face], (i.x - scroll[0], i.y - scroll[1] - image_resources[i.id][i.face].get_height() + Cube_Size))


def show_fps(window, clock):
    FPS_FONT = pygame.font.SysFont("Verdana", 10)
    color = pygame.Color("white")
    fps_overlay = FPS_FONT.render(str(int(clock.get_fps())), True, color)
    window.blit(fps_overlay, (55, 0))
    # Coords on screen
    coors_overlay = FPS_FONT.render(str((int(player.x / Cube_Size), int(player.y / Cube_Size))), True, color)
    window.blit(coors_overlay, (0, 0))


def entity_remover():
    for i in entities_to_remove:
        x, y = i
        entity = world[x][y].entity
        if entity.id != 0:
            if entity.drop_list.pop(0):
                for a in entity.drop_list:
                    for i in range(entity.entity_face + 1):
                        rand_x = random.randint(-30, 30)
                        rand_y = random.randint(-30, 30)
                        drop_map.append(Drop(entity.x * Cube_Size + rand_x, entity.y * Cube_Size + rand_y, a, 1, game_days))
            else:
                for i in entity.drop_list:
                    rand_x = random.randint(-30, 30)
                    rand_y = random.randint(-30, 30)
                    drop_map.append(Drop(entity.x * Cube_Size + rand_x, entity.y * Cube_Size + rand_y, i, 1, game_days))
            if entity.drop:
                pass
            entity.destroy()

    entities_to_remove.clear()


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


def drop_timeout_remover():
    global drop_map
    while True:
        #Remove uncollected drops
        for x in reversed(drop_map):
            if game_days - x.creation_day > 1:
                drop_map.remove(x)

        time.sleep(10)


def drop_manager():
    global drop_map
    global drop_map_section
    while True:
        # Update list of visible drops
        temp_drop = []
        for i in drop_map:
            if player.x - 900 < i.x < player.x + 900 and player.y - 900 < i.y < player.y + 900:
                temp_drop.append(i)
        drop_map_section = temp_drop[:]


        # Stacks drops
        temp_to_remove = []
        for i in range(len(drop_map_section)):
            for j in range(i + 1, len(drop_map_section)):
                a = drop_map_section[i]
                b = drop_map_section[j]
                if a.id == b.id:
                    distance = (((a.x - b.x) ** 2) + ((a.y - b.y) ** 2)) ** 0.5
                    player_distance_a = (((player.x - a.x) ** 2) + ((player.y - a.y) ** 2)) ** 0.5
                    player_distance_b = (((player.x - b.x) ** 2) + ((player.y - b.y) ** 2)) ** 0.5
                    if abs(distance) < 90 and abs(player_distance_a) > 220 and abs(player_distance_b) > 220:
                        temp_to_remove.append([a, b])

        for i in reversed(temp_to_remove):
            a, b = i
            drop_map.append(Drop(b.x, b.y, b.id, a.quantity + b.quantity, a.creation_day))
            drop_map.remove(b)
            drop_map.remove(a)

            for x in reversed(temp_to_remove):
                if x[0] == a or x[1] == a or x[0] == b or x[1] == b:
                    temp_to_remove.remove(x)

        time.sleep(0.05)


def drop_collection_manager():
    global drop_map_section
    while True:
        # Move drops to player
        for i in drop_map_section:
            distance = (((player.x - i.x) ** 2) + ((player.y - i.y) ** 2)) ** 0.5
            if abs(distance) < 190:
                if player.x - Cube_Size - i.x < 0:
                    i.x -= 4
                elif player.x - Cube_Size - i.x > 0:
                    i.x += 4

                if player.y - Cube_Size - i.y < 0:
                    i.y -= 4
                elif player.y - Cube_Size - i.y > 0:
                    i.y += 4

                if i.x - 35 < player.x - Cube_Size < i.x + 35 and i.y - 35 < player.y - Cube_Size < i.y + 35:
                    player.add_to_inventory((i.id, i.quantity))
                    try:
                        drop_map.remove(i)
                        drop_map_section.remove(i)
                    except:
                        print("problem")
                    pass
        #print(player.inventory)

        time.sleep(0.01)

def time_handler():
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
        elif 360 < timer < 420:
            night_value -= 2

        timer += 1
        time.sleep(0.01)#time.sleep(1)


def player_movement_handler():
    while game_running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            #global screen
            #screen = pygame.display.set_mode(size, pygame.SCALED | pygame.NOFRAME)
            collision_checker(player.x - player.speed, player.y)
        elif keys[pygame.K_d]:
            collision_checker(player.x + player.speed, player.y)
        if keys[pygame.K_w]:
            collision_checker(player.x, player.y - player.speed)
        if keys[pygame.K_s]:
            collision_checker(player.x, player.y + player.speed)

        time.sleep(Game_Tick/15)


def mouse_movement_handler():
    global mouse_position
    while game_running:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        block_x = int((mouse_x * (1 / 30)) + (scroll[0] * (1 / 30)))
        block_y = int((mouse_y * (1 / 30)) + (scroll[1] * (1 / 30)))
        mouse_position = (block_x, block_y)

        time.sleep(0.01)


def mouse_clicker_handler():
    while game_running:
        mouse_x, mouse_y = mouse_position
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            entity = world[mouse_x][mouse_y].entity
            if entity.health <= 0:
                entities_to_remove.append((mouse_x, mouse_y))
            else:
                entity.damage(10)

            time.sleep(0.1)

        time.sleep(0.01)





player_movement = threading.Thread(target=player_movement_handler)
player_movement.start()

mouse_movement = threading.Thread(target=mouse_movement_handler)
mouse_movement.start()

mouse_clicker = threading.Thread(target=mouse_clicker_handler)
mouse_clicker.start()

update_visible_world = threading.Thread(target=update_world_section)
update_visible_world.start()

drop_timeout = threading.Thread(target=drop_timeout_remover)
drop_timeout.start()

drop_man = threading.Thread(target=drop_manager)
drop_man.start()

drop_col_man = threading.Thread(target=drop_collection_manager)
drop_col_man.start()

time_handler = threading.Thread(target=time_handler)
time_handler.start()


block_face_checker()

button_pressed = False

#pygame.display.toggle_fullscreen()

# -------- Main Program Loop -----------
while playing:
    # --- Main event loop
    #for event in pygame.event.get():  # User did something
        #if event.type == pygame.QUIT:  # If user clicked close
            #playing = False  # Flag that we are done so we exit this loop
        #if (event.type is pygame.KEYDOWN and event.key == pygame.K_f):
            #print("f")
            #if screen.get_flags() & pygame.FULLSCREEN:
                #pygame.display.set_mode(size)
            #else:
                #pygame.display.set_mode(size, pygame.FULLSCREEN)
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_F2:
                screen = pygame.display.set_mode(size, pygame.SCALED | pygame.FULLSCREEN)
                #night_filter = pygame.Surface(size)
        if e.type == pygame.QUIT:
            playing = False

    start_time = time.time()
    screen_width, screen_height = screen.get_size()
    true_scroll[0] += (player.x - true_scroll[0] - (screen_width / 2)) / 20
    true_scroll[1] += (player.y - true_scroll[1] - (screen_height / 2)) / 20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    #print("--- A: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    draw_world()
    #print("--- Draw World: %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    draw_entities()
    draw_drops()
    #print("--- Draw Entities: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    rect = player.image.get_rect()
    rect.center = player.x - scroll[0], player.y - scroll[1] - (player.image.get_height() - Cube_Size - 5)  #fixed the size because was messign up colisions now colision point is at feet
    player.hitbox = pygame.Rect(rect)
    screen.blit(player.image, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    #print("--- Player: %s seconds ---" % (time.time() - start_time))
    #screen.blit(player.image, (player.x - scroll[0], player.y - scroll[1]))
    start_time = time.time()
    show_fps(screen, clock)
    #print("--- FPS: %s seconds ---" % (time.time() - start_time))

    if night_value > 0:
        start_time = time.time()
        screen.blit(night_filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        #print("--- Night: %s seconds ---" % (time.time() - start_time))



    pygame.display.flip()

    clock.tick(120)

pygame.quit()
