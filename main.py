import copy
import os
import sys

from worldgenerator import WorldGenerator
from player import Player
import pygame
import threading
import time
from resources import Resources
from drop import Drop
from options import Options
from worldloader import Worldloader
import random


os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size, pygame.SCALED | pygame.DOUBLEBUF)
pygame.display.set_caption("Adventure Game")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN])

black = (0, 0, 0)

entities_to_remove = []

night_value = 0
night_filter = pygame.Surface(size)
night_filter.fill((0, 0, 0))
game_days = 0
Game_Tick = 0.1
game_running = True
game_paused = False
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
# Player declaration


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

world_size = 300

drop_map_section = []
world_section = []
world_section_entities = []
Cube_Size = 30

true_scroll = [0, 0]

mouse_position = (0, 0)

image_resources = Resources().get_images()

options = Options()

world_loader = Worldloader()


if options.fullscreen:
    screen = pygame.display.set_mode(size, pygame.SCALED | pygame.FULLSCREEN | pygame.DOUBLEBUF)


def main_menu():
    bg = pygame.image.load('images/Menu/bg.jpg').convert()
    button = [pygame.image.load('images/Menu/button1.png').convert_alpha(), pygame.image.load('images/Menu/button2.png').convert_alpha()]
    x = 0
    global screen
    while True:
        click = False
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_F2:
                    screen = pygame.display.set_mode(size, pygame.SCALED | pygame.FULLSCREEN)
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True
            if e.type == pygame.QUIT:
                return


        FPS_FONT = pygame.font.SysFont("franklingothicmedium", 60)
        color = pygame.Color("black")

        rel_x = x % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < size[0]:
            screen.blit(bg, (rel_x, 0))
        x -= 1

        mx, my = pygame.mouse.get_pos()

        text_start = FPS_FONT.render("Start", True, color)
        text_options = FPS_FONT.render("Options", True, color)
        text_exit = FPS_FONT.render("Exit", True, color)

        btn_start = pygame.Rect(450, 300, 400, 100)
        btn_options = pygame.Rect(450, 420, 400, 100)
        btn_exit = pygame.Rect(450, 540, 400, 100)

        screen.blit(button[0], btn_start)
        screen.blit(button[0], btn_options)
        screen.blit(button[0], btn_exit)

        if btn_start.collidepoint((mx, my)):
            screen.blit(button[1], btn_start)
            if click:
                save_selector_menu()
                #play()
        if btn_options.collidepoint((mx, my)):
            screen.blit(button[1], btn_options)
            if click:
                options_menu()
        if btn_exit.collidepoint((mx, my)):
            screen.blit(button[1], btn_exit)
            if click:
                return

        a, b = btn_start.center
        btn_center = (a, b - 15)
        text_rect = text_start.get_rect(center=btn_center)
        screen.blit(text_start, text_rect)

        a, b = btn_options.center
        btn_center = (a, b - 15)
        text_rect = text_options.get_rect(center=btn_center)
        screen.blit(text_options, text_rect)

        a, b = btn_exit.center
        btn_center = (a, b - 15)
        text_rect = text_exit.get_rect(center=btn_center)
        screen.blit(text_exit, text_rect)

        pygame.display.flip()

        clock.tick(60)


def save_selector_menu():
    bg = pygame.image.load('images/Menu/bg.jpg').convert()
    play_btn = [pygame.image.load('images/Menu/play1.png').convert_alpha(), pygame.image.load('images/Menu/play2.png').convert_alpha()]
    under_map_board = pygame.image.load('images/Menu/world_selector_board.png').convert()
    trash_can = [pygame.image.load('images/Menu/trash.png').convert_alpha(), pygame.image.load('images/Menu/trash2.png').convert_alpha()]
    loading_screen = pygame.image.load('images/Menu/loading.jpg').convert()

    #world_loader.load()


    print("worlds", world_loader.worlds_quick_load)


    x = 0
    global screen
    while True:
        click = False
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_F2:
                    screen = pygame.display.set_mode(size, pygame.SCALED | pygame.FULLSCREEN)
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True
            if e.type == pygame.QUIT:
                return



        FPS_FONT = pygame.font.SysFont("franklingothicmedium", 70)
        last_played_font = pygame.font.SysFont("franklingothicmedium", 15)
        color = pygame.Color("black")
        rectangle_color = pygame.Color("brown")

        rel_x = x % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < size[0]:
            screen.blit(bg, (rel_x, 0))
        x -= 1

        max_x, max_y = size

        s = pygame.Surface((max_x - 60, max_y - 60))  # the size of your rect
        s.set_alpha(128)
        s.fill((28, 28, 28))
        screen.blit(s, (30, 30))

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(30, 30, max_x - 60, max_y - 60), 2, 3)

        mx, my = pygame.mouse.get_pos()

        text_new_game = FPS_FONT.render("New Game", True, color)
        text_plus = FPS_FONT.render("+", True, color)
        text_play = FPS_FONT.render("▶", True, color)



        btn_save1 = pygame.Rect(96, 100, 200, 200)
        btn_save2 = pygame.Rect(392, 100, 200, 200)
        btn_save3 = pygame.Rect(688, 100, 200, 200)
        btn_save4 = pygame.Rect(984, 100, 200, 200)

        btn_save5 = pygame.Rect(96, 420, 200, 200)
        btn_save6 = pygame.Rect(392, 420, 200, 200)
        btn_save7 = pygame.Rect(688, 420, 200, 200)
        btn_save8 = pygame.Rect(984, 420, 200, 200)

        if world_loader.worlds_minimaps[0] is not None:
            map = pygame.transform.scale(pygame.image.load(world_loader.worlds_minimaps[0]).convert_alpha(), (200, 200))
            text_rect = map.get_rect(center=btn_save1.center)
            screen.blit(map, text_rect)
        if world_loader.worlds_minimaps[1] is not None:
            map = pygame.transform.scale(pygame.image.load(world_loader.worlds_minimaps[1]).convert_alpha(), (200, 200))
            text_rect = map.get_rect(center=btn_save2.center)
            screen.blit(map, text_rect)
        if world_loader.worlds_minimaps[2] is not None:
            map = pygame.transform.scale(pygame.image.load(world_loader.worlds_minimaps[2]).convert_alpha(), (200, 200))
            text_rect = map.get_rect(center=btn_save3.center)
            screen.blit(map, text_rect)
        if world_loader.worlds_minimaps[3] is not None:
            map = pygame.transform.scale(pygame.image.load(world_loader.worlds_minimaps[3]).convert_alpha(), (200, 200))
            text_rect = map.get_rect(center=btn_save4.center)
            screen.blit(map, text_rect)
        if world_loader.worlds_minimaps[4] is not None:
            map = pygame.transform.scale(pygame.image.load(world_loader.worlds_minimaps[4]).convert_alpha(), (200, 200))
            text_rect = map.get_rect(center=btn_save5.center)
            screen.blit(map, text_rect)
        if world_loader.worlds_minimaps[5] is not None:
            map = pygame.transform.scale(pygame.image.load(world_loader.worlds_minimaps[5]).convert_alpha(), (200, 200))
            text_rect = map.get_rect(center=btn_save6.center)
            screen.blit(map, text_rect)
        if world_loader.worlds_minimaps[6] is not None:
            map = pygame.transform.scale(pygame.image.load(world_loader.worlds_minimaps[6]).convert_alpha(), (200, 200))
            text_rect = map.get_rect(center=btn_save7.center)
            screen.blit(map, text_rect)
        if world_loader.worlds_minimaps[7] is not None:
            map = pygame.transform.scale(pygame.image.load(world_loader.worlds_minimaps[7]).convert_alpha(), (200, 200))
            text_rect = map.get_rect(center=btn_save8.center)
            screen.blit(map, text_rect)




        if btn_save1.collidepoint((mx, my)):
            btn_save1_inflated = pygame.Rect(btn_save1.x - 1, btn_save1.y - 1, btn_save1.width + 2, btn_save1.height + 2)
            pygame.draw.rect(screen, (255, 255, 255), btn_save1_inflated, 2)
            if world_loader.worlds_quick_load[0]:
                screen.blit(play_btn[1], play_btn[1].get_rect(center=btn_save1.center))
            if click:
                world_loader.world_in_use = 0
                screen.blit(loading_screen, (0, 0))
                pygame.display.flip()
                if world_loader.worlds_quick_load[0]:
                    play(world_loader.load_world(0))
                else:
                    play(None)


        if btn_save2.collidepoint((mx, my)):
            btn_save1_inflated = pygame.Rect(btn_save2.x - 1, btn_save2.y - 1, btn_save2.width + 2, btn_save2.height + 2)
            pygame.draw.rect(screen, (255, 255, 255), btn_save1_inflated, 2)
            if world_loader.worlds_quick_load[1]:
                screen.blit(play_btn[1], play_btn[1].get_rect(center=btn_save2.center))
            if click:
                world_loader.world_in_use = 1
                screen.blit(loading_screen, (0, 0))
                pygame.display.flip()
                if world_loader.worlds_quick_load[1]:
                    play(world_loader.load_world(1))
                else:
                    play(None)


        if btn_save3.collidepoint((mx, my)):
            btn_save1_inflated = pygame.Rect(btn_save3.x - 1, btn_save3.y - 1, btn_save3.width + 2, btn_save3.height + 2)
            pygame.draw.rect(screen, (255, 255, 255), btn_save1_inflated, 2)
            if world_loader.worlds_quick_load[2]:
                screen.blit(play_btn[1], play_btn[1].get_rect(center=btn_save3.center))
            if click:
                world_loader.world_in_use = 2
                screen.blit(loading_screen, (0, 0))
                pygame.display.flip()
                if world_loader.worlds_quick_load[2]:
                    play(world_loader.load_world(2))
                else:
                    play(None)


        if btn_save4.collidepoint((mx, my)):
            btn_save1_inflated = pygame.Rect(btn_save4.x - 1, btn_save4.y - 1, btn_save4.width + 2, btn_save4.height + 2)
            pygame.draw.rect(screen, (255, 255, 255), btn_save1_inflated, 2)
            if world_loader.worlds_quick_load[3]:
                screen.blit(play_btn[1], play_btn[1].get_rect(center=btn_save4.center))
            if click:
                world_loader.world_in_use = 3
                screen.blit(loading_screen, (0, 0))
                pygame.display.flip()
                if world_loader.worlds_quick_load[3]:
                    play(world_loader.load_world(3))
                else:
                    play(None)


        if btn_save5.collidepoint((mx, my)):
            btn_save1_inflated = pygame.Rect(btn_save5.x - 1, btn_save5.y - 1, btn_save5.width + 2, btn_save5.height + 2)
            pygame.draw.rect(screen, (255, 255, 255), btn_save1_inflated, 2)
            if world_loader.worlds_quick_load[4]:
                screen.blit(play_btn[1], play_btn[1].get_rect(center=btn_save5.center))
            if click:
                world_loader.world_in_use = 4
                screen.blit(loading_screen, (0, 0))
                pygame.display.flip()
                if world_loader.worlds_quick_load[4]:
                    play(world_loader.load_world(4))
                else:
                    play(None)


        if btn_save6.collidepoint((mx, my)):
            btn_save1_inflated = pygame.Rect(btn_save6.x - 1, btn_save6.y - 1, btn_save6.width + 2, btn_save6.height + 2)
            pygame.draw.rect(screen, (255, 255, 255), btn_save1_inflated, 2)
            if world_loader.worlds_quick_load[5]:
                screen.blit(play_btn[1], play_btn[1].get_rect(center=btn_save6.center))
            if click:
                world_loader.world_in_use = 5
                screen.blit(loading_screen, (0, 0))
                pygame.display.flip()
                if world_loader.worlds_quick_load[5]:
                    play(world_loader.load_world(5))
                else:
                    play(None)


        if btn_save7.collidepoint((mx, my)):
            btn_save1_inflated = pygame.Rect(btn_save7.x - 1, btn_save7.y - 1, btn_save7.width + 2, btn_save7.height + 2)
            pygame.draw.rect(screen, (255, 255, 255), btn_save1_inflated, 2)
            if world_loader.worlds_quick_load[6]:
                screen.blit(play_btn[1], play_btn[1].get_rect(center=btn_save7.center))
            if click:
                world_loader.world_in_use = 6
                screen.blit(loading_screen, (0, 0))
                pygame.display.flip()
                if world_loader.worlds_quick_load[6]:
                    play(world_loader.load_world(6))
                else:
                    play(None)


        if btn_save8.collidepoint((mx, my)):
            btn_save1_inflated = pygame.Rect(btn_save8.x - 1, btn_save8.y - 1, btn_save8.width + 2, btn_save8.height + 2)
            pygame.draw.rect(screen, (255, 255, 255), btn_save1_inflated, 2)
            if world_loader.worlds_quick_load[7]:
                screen.blit(play_btn[1], play_btn[1].get_rect(center=btn_save8.center))
            if click:
                world_loader.world_in_use = 7
                screen.blit(loading_screen, (0, 0))
                pygame.display.flip()
                if world_loader.worlds_quick_load[7]:
                    play(world_loader.load_world(7))
                else:
                    play(None)


        if world_loader.worlds_quick_load[0]:
            text_rect = play_btn[0].get_rect(center=btn_save1.center)
            screen.blit(play_btn[0], text_rect)

            file_last_modified_time = os.path.getmtime(
                os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world0.save")
            formatted_time = time.strftime('%Y-%m-%d  %H:%M', time.localtime(file_last_modified_time))
            last_time_played_text = last_played_font.render("Last time played:", True, color)
            last_time_played_time = last_played_font.render(formatted_time, True, color)
            btn_trash = pygame.Rect(text_rect.x + 75, text_rect.y + 123, 32, 32)
            screen.blit(under_map_board, (text_rect.x - 85, text_rect.y + 115))
            screen.blit(trash_can[0], btn_trash)
            if btn_trash.collidepoint((mx, my)):
                screen.blit(trash_can[1], btn_trash)
                if click:
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world0.save")
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\minimap0.png")
                    world_loader.worlds_quick_load[0] = False
                    world_loader.worlds_minimaps[0] = None
            screen.blit(last_time_played_text, (text_rect.x - 75, text_rect.y + 120))
            screen.blit(last_time_played_time, (text_rect.x - 75, text_rect.y + 140))
        else:
            text_rect = text_plus.get_rect(center=btn_save1.center)
            screen.blit(text_plus, text_rect)


        if world_loader.worlds_quick_load[1]:
            text_rect = play_btn[0].get_rect(center=btn_save2.center)
            screen.blit(play_btn[0], text_rect)

            file_last_modified_time = os.path.getmtime(
                os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world1.save")
            formatted_time = time.strftime('%Y-%m-%d  %H:%M', time.localtime(file_last_modified_time))
            last_time_played_text = last_played_font.render("Last time played:", True, color)
            last_time_played_time = last_played_font.render(formatted_time, True, color)
            btn_trash1 = pygame.Rect(text_rect.x + 75, text_rect.y + 123, 32, 32)
            screen.blit(under_map_board, (text_rect.x - 85, text_rect.y + 115))
            screen.blit(trash_can[0], btn_trash1)
            if btn_trash1.collidepoint((mx, my)):
                screen.blit(trash_can[1], btn_trash1)
                if click:
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world1.save")
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\minimap1.png")
                    world_loader.worlds_quick_load[1] = False
                    world_loader.worlds_minimaps[1] = None
            screen.blit(last_time_played_text, (text_rect.x - 75, text_rect.y + 120))
            screen.blit(last_time_played_time, (text_rect.x - 75, text_rect.y + 140))
        else:
            text_rect = text_plus.get_rect(center=btn_save2.center)
            screen.blit(text_plus, text_rect)


        if world_loader.worlds_quick_load[2]:
            text_rect = play_btn[0].get_rect(center=btn_save3.center)
            screen.blit(play_btn[0], text_rect)

            file_last_modified_time = os.path.getmtime(
                os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world2.save")
            formatted_time = time.strftime('%Y-%m-%d  %H:%M', time.localtime(file_last_modified_time))
            last_time_played_text = last_played_font.render("Last time played:", True, color)
            last_time_played_time = last_played_font.render(formatted_time, True, color)
            btn_trash2 = pygame.Rect(text_rect.x + 75, text_rect.y + 123, 32, 32)
            screen.blit(under_map_board, (text_rect.x - 85, text_rect.y + 115))
            screen.blit(trash_can[0], btn_trash2)
            if btn_trash2.collidepoint((mx, my)):
                screen.blit(trash_can[1], btn_trash2)
                if click:
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world2.save")
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\minimap2.png")
                    world_loader.worlds_quick_load[2] = False
                    world_loader.worlds_minimaps[2] = None
            screen.blit(last_time_played_text, (text_rect.x - 75, text_rect.y + 120))
            screen.blit(last_time_played_time, (text_rect.x - 75, text_rect.y + 140))
        else:
            text_rect = text_plus.get_rect(center=btn_save3.center)
            screen.blit(text_plus, text_rect)


        if world_loader.worlds_quick_load[3]:
            text_rect = play_btn[0].get_rect(center=btn_save4.center)
            screen.blit(play_btn[0], text_rect)

            file_last_modified_time = os.path.getmtime(
                os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world3.save")
            formatted_time = time.strftime('%Y-%m-%d  %H:%M', time.localtime(file_last_modified_time))
            last_time_played_text = last_played_font.render("Last time played:", True, color)
            last_time_played_time = last_played_font.render(formatted_time, True, color)
            btn_trash3 = pygame.Rect(text_rect.x + 75, text_rect.y + 123, 32, 32)
            screen.blit(under_map_board, (text_rect.x - 85, text_rect.y + 115))
            screen.blit(trash_can[0], btn_trash3)
            if btn_trash3.collidepoint((mx, my)):
                screen.blit(trash_can[1], btn_trash3)
                if click:
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world3.save")
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\minimap3.png")
                    world_loader.worlds_quick_load[3] = False
                    world_loader.worlds_minimaps[3] = None
            screen.blit(last_time_played_text, (text_rect.x - 75, text_rect.y + 120))
            screen.blit(last_time_played_time, (text_rect.x - 75, text_rect.y + 140))
        else:
            text_rect = text_plus.get_rect(center=btn_save4.center)
            screen.blit(text_plus, text_rect)


        if world_loader.worlds_quick_load[4]:
            text_rect = play_btn[0].get_rect(center=btn_save5.center)
            screen.blit(play_btn[0], text_rect)

            file_last_modified_time = os.path.getmtime(
                os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world4.save")
            formatted_time = time.strftime('%Y-%m-%d  %H:%M', time.localtime(file_last_modified_time))
            last_time_played_text = last_played_font.render("Last time played:", True, color)
            last_time_played_time = last_played_font.render(formatted_time, True, color)
            btn_trash4 = pygame.Rect(text_rect.x + 75, text_rect.y + 123, 32, 32)
            screen.blit(under_map_board, (text_rect.x - 85, text_rect.y + 115))
            screen.blit(trash_can[0], btn_trash4)
            if btn_trash4.collidepoint((mx, my)):
                screen.blit(trash_can[1], btn_trash4)
                if click:
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world4.save")
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\minimap4.png")
                    world_loader.worlds_quick_load[4] = False
                    world_loader.worlds_minimaps[4] = None
            screen.blit(last_time_played_text, (text_rect.x - 75, text_rect.y + 120))
            screen.blit(last_time_played_time, (text_rect.x - 75, text_rect.y + 140))
        else:
            text_rect = text_plus.get_rect(center=btn_save5.center)
            screen.blit(text_plus, text_rect)


        if world_loader.worlds_quick_load[5]:
            text_rect = play_btn[0].get_rect(center=btn_save6.center)
            screen.blit(play_btn[0], text_rect)

            file_last_modified_time = os.path.getmtime(
                os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world5.save")
            formatted_time = time.strftime('%Y-%m-%d  %H:%M', time.localtime(file_last_modified_time))
            last_time_played_text = last_played_font.render("Last time played:", True, color)
            last_time_played_time = last_played_font.render(formatted_time, True, color)
            btn_trash5 = pygame.Rect(text_rect.x + 75, text_rect.y + 123, 32, 32)
            screen.blit(under_map_board, (text_rect.x - 85, text_rect.y + 115))
            screen.blit(trash_can[0], btn_trash5)
            if btn_trash5.collidepoint((mx, my)):
                screen.blit(trash_can[1], btn_trash5)
                if click:
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world5.save")
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\minimap5.png")
                    world_loader.worlds_quick_load[5] = False
                    world_loader.worlds_minimaps[5] = None
            screen.blit(last_time_played_text, (text_rect.x - 75, text_rect.y + 120))
            screen.blit(last_time_played_time, (text_rect.x - 75, text_rect.y + 140))
        else:
            text_rect = text_plus.get_rect(center=btn_save6.center)
            screen.blit(text_plus, text_rect)


        if world_loader.worlds_quick_load[6]:
            text_rect = play_btn[0].get_rect(center=btn_save7.center)
            screen.blit(play_btn[0], text_rect)

            file_last_modified_time = os.path.getmtime(
                os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world6.save")
            formatted_time = time.strftime('%Y-%m-%d  %H:%M', time.localtime(file_last_modified_time))
            last_time_played_text = last_played_font.render("Last time played:", True, color)
            last_time_played_time = last_played_font.render(formatted_time, True, color)
            btn_trash6 = pygame.Rect(text_rect.x + 75, text_rect.y + 123, 32, 32)
            screen.blit(under_map_board, (text_rect.x - 85, text_rect.y + 115))
            screen.blit(trash_can[0], btn_trash6)
            if btn_trash6.collidepoint((mx, my)):
                screen.blit(trash_can[1], btn_trash6)
                if click:
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world6.save")
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\minimap6.png")
                    world_loader.worlds_quick_load[6] = False
                    world_loader.worlds_minimaps[6] = None
            screen.blit(last_time_played_text, (text_rect.x - 75, text_rect.y + 120))
            screen.blit(last_time_played_time, (text_rect.x - 75, text_rect.y + 140))
        else:
            text_rect = text_plus.get_rect(center=btn_save7.center)
            screen.blit(text_plus, text_rect)


        if world_loader.worlds_quick_load[7]:
            text_rect = play_btn[0].get_rect(center=btn_save8.center)
            screen.blit(play_btn[0], text_rect)

            file_last_modified_time = os.path.getmtime(
                os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world7.save")
            formatted_time = time.strftime('%Y-%m-%d  %H:%M', time.localtime(file_last_modified_time))
            last_time_played_text = last_played_font.render("Last time played:", True, color)
            last_time_played_time = last_played_font.render(formatted_time, True, color)
            btn_trash7 = pygame.Rect(text_rect.x + 75, text_rect.y + 123, 32, 32)
            screen.blit(under_map_board, (text_rect.x - 85, text_rect.y + 115))
            screen.blit(trash_can[0], btn_trash7)
            if btn_trash7.collidepoint((mx, my)):
                screen.blit(trash_can[1], btn_trash7)
                if click:
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\world7.save")
                    os.remove(os.getenv('APPDATA') + "\\" + world_loader.get_game_name() + "\minimap7.png")
                    world_loader.worlds_quick_load[7] = False
                    world_loader.worlds_minimaps[7] = None
            screen.blit(last_time_played_text, (text_rect.x - 75, text_rect.y + 120))
            screen.blit(last_time_played_time, (text_rect.x - 75, text_rect.y + 140))
        else:
            text_rect = text_plus.get_rect(center=btn_save8.center)
            screen.blit(text_plus, text_rect)


        pygame.draw.rect(screen, (0, 0, 0), btn_save1, 2)
        pygame.draw.rect(screen, (0, 0, 0), btn_save2, 2)
        pygame.draw.rect(screen, (0, 0, 0), btn_save3, 2)
        pygame.draw.rect(screen, (0, 0, 0), btn_save4, 2)
        pygame.draw.rect(screen, (0, 0, 0), btn_save5, 2)
        pygame.draw.rect(screen, (0, 0, 0), btn_save6, 2)
        pygame.draw.rect(screen, (0, 0, 0), btn_save7, 2)
        pygame.draw.rect(screen, (0, 0, 0), btn_save8, 2)


        # screen.blit(text_language, (200, 200))

        # pygame.draw.rect(screen, (0, 0, 0), rect_language_state)

        pygame.display.flip()

        clock.tick(60)



def options_menu():
    bg = pygame.image.load('images/Menu/bg.jpg').convert()
    back_button = [pygame.image.load('images/Menu/back_button1.png').convert_alpha(),
                   pygame.image.load('images/Menu/back_button2.png').convert_alpha()]
    left_arrow_button = [pygame.image.load('images/Menu/left_arrow1.png').convert_alpha(),
                         pygame.image.load('images/Menu/left_arrow2.png').convert_alpha()]
    right_arrow_button = [pygame.image.load('images/Menu/right_arrow1.png').convert_alpha(),
                         pygame.image.load('images/Menu/right_arrow2.png').convert_alpha()]
    x = 0
    global screen
    while True:
        click = False
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_F2:
                    screen = pygame.display.set_mode(size, pygame.SCALED | pygame.FULLSCREEN)
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True
            if e.type == pygame.QUIT:
                pygame.quit()
                print("quit from options")
                #return



        FPS_FONT = pygame.font.SysFont("franklingothicmedium", 25)
        color = pygame.Color("black")

        rel_x = x % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < size[0]:
            screen.blit(bg, (rel_x, 0))
        x -= 1

        max_x, max_y = size

        s = pygame.Surface((max_x - 60, max_y - 60))  # the size of your rect
        s.set_alpha(128)
        s.fill((28, 28, 28))
        screen.blit(s, (30, 30))

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(30, 30, max_x - 60, max_y - 60), 2, 3)

        mx, my = pygame.mouse.get_pos()

        text_back = FPS_FONT.render("Back", True, color)
        text_language = FPS_FONT.render("Language:", True, color)
        text_fullscreen = FPS_FONT.render("Fullscreen:", True, color)
        text_fps = FPS_FONT.render("Show FPS:", True, color)
        text_coords = FPS_FONT.render("Coordinates:", True, color)

        state_language = FPS_FONT.render(options.languages[options.language], True, color)
        if options.fullscreen:
            state_fullscreen = FPS_FONT.render("Yes", True, color)
        else:
            state_fullscreen = FPS_FONT.render("No", True, color)
        if options.fps:
            state_fps = FPS_FONT.render("Yes", True, color)
        else:
            state_fps = FPS_FONT.render("No", True, color)
        if options.coords:
            state_coords = FPS_FONT.render("Yes", True, color)
        else:
            state_coords = FPS_FONT.render("No", True, color)

        btn_back = pygame.Rect(50, 50, 100, 50)

        rect_language_text = pygame.Rect(100, 150, 150, 30)
        btn_language_left = pygame.Rect(250, 150, 30, 30)
        rect_language_state = pygame.Rect(280, 150, 120, 30)
        btn_language_right = pygame.Rect(400, 150, 30, 30)

        rect_fullscreen_text = pygame.Rect(100, 250, 150, 30)
        btn_fullscreen_left = pygame.Rect(250, 250, 30, 30)
        rect_fullscreen_state = pygame.Rect(280, 250, 120, 30)
        btn_fullscreen_right = pygame.Rect(400, 250, 30, 30)

        rect_fps_text = pygame.Rect(100, 350, 150, 30)
        btn_fps_left = pygame.Rect(250, 350, 30, 30)
        rect_fps_state = pygame.Rect(280, 350, 120, 30)
        btn_fps_right = pygame.Rect(400, 350, 30, 30)

        rect_coords_text = pygame.Rect(100, 450, 150, 30)
        btn_coords_left = pygame.Rect(250, 450, 30, 30)
        rect_coords_state = pygame.Rect(280, 450, 120, 30)
        btn_coords_right = pygame.Rect(400, 450, 30, 30)

        screen.blit(back_button[0], btn_back)
        screen.blit(left_arrow_button[0], btn_language_left)
        screen.blit(right_arrow_button[0], btn_language_right)
        screen.blit(left_arrow_button[0], btn_fullscreen_left)
        screen.blit(right_arrow_button[0], btn_fullscreen_right)
        screen.blit(left_arrow_button[0], btn_fps_left)
        screen.blit(right_arrow_button[0], btn_fps_right)
        screen.blit(left_arrow_button[0], btn_coords_left)
        screen.blit(right_arrow_button[0], btn_coords_right)

        if btn_back.collidepoint((mx, my)):
            screen.blit(back_button[1], btn_back)
            if click:
                options.save()
                return

        if btn_language_left.collidepoint((mx, my)):
            screen.blit(left_arrow_button[1], btn_language_left)
            if click:
                options.update_language(-1)
        if btn_language_right.collidepoint((mx, my)):
            screen.blit(right_arrow_button[1], btn_language_right)
            if click:
                options.update_language(1)

        if btn_fullscreen_left.collidepoint((mx, my)):
            screen.blit(left_arrow_button[1], btn_fullscreen_left)
            if click:
                options.update_fullscreen()
                if options.fullscreen:
                    screen = pygame.display.set_mode(size, pygame.SCALED | pygame.FULLSCREEN)
                else:
                    pygame.display.quit()
                    pygame.display.get_init()
                    screen = pygame.display.set_mode(size, pygame.SCALED)
        if btn_fullscreen_right.collidepoint((mx, my)):
            screen.blit(right_arrow_button[1], btn_fullscreen_right)
            if click:
                options.update_fullscreen()
                if options.fullscreen:
                    screen = pygame.display.set_mode(size, pygame.SCALED | pygame.FULLSCREEN)
                else:
                    pygame.display.quit()
                    pygame.display.get_init()
                    screen = pygame.display.set_mode(size, pygame.SCALED)

        if btn_fps_left.collidepoint((mx, my)):
            screen.blit(left_arrow_button[1], btn_fps_left)
            if click:
                options.update_fps()
        if btn_fps_right.collidepoint((mx, my)):
            screen.blit(right_arrow_button[1], btn_fps_right)
            if click:
                options.update_fps()

        if btn_coords_left.collidepoint((mx, my)):
            screen.blit(left_arrow_button[1], btn_coords_left)
            if click:
                options.update_coords()
        if btn_coords_right.collidepoint((mx, my)):
            screen.blit(right_arrow_button[1], btn_coords_right)
            if click:
                options.update_coords()

        a, b = btn_back.center
        btn_center = (a + 10, b)
        text_rect = text_back.get_rect(center=btn_center)
        screen.blit(text_back, text_rect)

        a, b = rect_language_text.center
        btn_center = (a, b)
        text_rect = text_language.get_rect(center=btn_center)
        screen.blit(text_language, text_rect)

        a, b = rect_language_state.center
        btn_center = (a, b)
        text_rect = state_language.get_rect(center=btn_center)
        screen.blit(state_language, text_rect)

        a, b = rect_fullscreen_text.center
        btn_center = (a, b)
        text_rect = text_fullscreen.get_rect(center=btn_center)
        screen.blit(text_fullscreen, text_rect)

        a, b = rect_fullscreen_state.center
        btn_center = (a, b)
        text_rect = state_fullscreen.get_rect(center=btn_center)
        screen.blit(state_fullscreen, text_rect)

        a, b = rect_fps_text.center
        btn_center = (a, b)
        text_rect = text_fps.get_rect(center=btn_center)
        screen.blit(text_fps, text_rect)

        a, b = rect_fps_state.center
        btn_center = (a, b)
        text_rect = state_fps.get_rect(center=btn_center)
        screen.blit(state_fps, text_rect)

        a, b = rect_coords_text.center
        btn_center = (a, b)
        text_rect = text_coords.get_rect(center=btn_center)
        screen.blit(text_coords, text_rect)

        a, b = rect_coords_state.center
        btn_center = (a, b)
        text_rect = state_coords.get_rect(center=btn_center)
        screen.blit(state_coords, text_rect)


        #screen.blit(text_language, (200, 200))

        #pygame.draw.rect(screen, (0, 0, 0), rect_language_state)

        pygame.display.flip()

        clock.tick(60)


def esc_menu():
    open = True
    bg = pygame.image.load('images/Menu/bg.jpg').convert()
    button = [pygame.image.load('images/Menu/button1.png').convert_alpha(),
              pygame.image.load('images/Menu/button2.png').convert_alpha()]
    x = 0
    global screen
    while open:
        click = False

        FPS_FONT = pygame.font.SysFont("franklingothicmedium", 60)
        color = pygame.Color("black")

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        rel_x = x % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < size[0]:
            screen.blit(bg, (rel_x, 0))
        x -= 1

        mx, my = pygame.mouse.get_pos()

        text_start = FPS_FONT.render("Resume", True, color)
        text_options = FPS_FONT.render("Options", True, color)
        text_exit = FPS_FONT.render("Quit", True, color)

        btn_start = pygame.Rect(450, 300, 400, 100)
        btn_options = pygame.Rect(450, 420, 400, 100)
        btn_exit = pygame.Rect(450, 540, 400, 100)

        screen.blit(button[0], btn_start)
        screen.blit(button[0], btn_options)
        screen.blit(button[0], btn_exit)

        if btn_start.collidepoint((mx, my)):
            screen.blit(button[1], btn_start)
            if click:
                return
        if btn_options.collidepoint((mx, my)):
            screen.blit(button[1], btn_options)
            if click:
                options_menu()
        if btn_exit.collidepoint((mx, my)):
            screen.blit(button[1], btn_exit)
            if click:
                os.execl(sys.executable, sys.executable, *sys.argv)
                #pygame.quit()
                #sys.exit()

        a, b = btn_start.center
        btn_center = (a, b - 15)
        text_rect = text_start.get_rect(center=btn_center)
        screen.blit(text_start, text_rect)

        a, b = btn_options.center
        btn_center = (a, b - 15)
        text_rect = text_options.get_rect(center=btn_center)
        screen.blit(text_options, text_rect)

        a, b = btn_exit.center
        btn_center = (a, b - 15)
        text_rect = text_exit.get_rect(center=btn_center)
        screen.blit(text_exit, text_rect)

        pygame.display.flip()

        clock.tick(60)



def play(game_save):
    if game_save is None:
        world = WorldGenerator(world_size, world_size).get_world()
        player = Player(2000, 2000)
        drop_map = []
    else:
        world = game_save[0]#copy.deepcopy(game_save[0])
        player = Player(2000, 2000)
        player.x = int(game_save[1][0])
        player.y = int(game_save[1][1])
        player.health = int(game_save[1][2])
        player.inventory = game_save[1][3]
        player.inventory_full = game_save[1][4]
        drop_map = game_save[2]

    minimap = pygame.image.load(world_loader.create_temporary_map(world)).convert()
    minimap.set_alpha(220)
    minimap_head = pygame.image.load('images/Other/minimap_head.png').convert_alpha()
    inventory_image = [pygame.image.load('images/Inventory/inventory.jpg').convert(), pygame.image.load('images/Inventory/inventory_expanded.jpg').convert()]
    inventory_image_selected = pygame.image.load('images/Inventory/inventory_selected_slot.jpg').convert()

    inventory_font = pygame.font.SysFont("franklingothicmedium", 10)
    inventory_font_color = pygame.Color("white")
    inventory_selected_slot = 0

    FPS_FONT = pygame.font.SysFont("Verdana", 15)
    color = pygame.Color("white")


    global screen
    #screen = pygame.display.set_mode(size, pygame.SCALED)
    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    playing = True
    scroll = [0, 0]
    idle_animation_list = []
    idle_animation_list.append(player)


    def update_world_section():
        global world_section
        map_size = len(world)
        while playing:
            start_time = time.time()

            #temp_world = []

            #for x in range(int(player.x / 30) - 30, int(player.x / 30) + 30):
                #for y in range(int(player.y/30) - 30, int(player.y/30) + 30):
                    #if 0 <= x < map_size - 1 and 0 <= y < map_size - 1:
                        #temp_world.append(world[x][y])

            # world_section = temp_world[:]


            world_section = [world[x][y] for x in range(int(player.x / 30) - 30, int(player.x / 30) + 30) for y in range(int(player.y/30) - 30, int(player.y/30) + 30) if 0 <= x < map_size - 1 and 0 <= y < map_size - 1 ]

            time.sleep(Game_Tick*5)
            #print("--- Update world: %s seconds ---" % (time.time() - start_time))


    def draw_worldold():
        global world_section_entities
        temp_world_section_entities = []
        for i in world_section:
            screen.blit(image_resources[i.id][i.block_face], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]))
            #i.hitbox = pygame.Rect((i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]), (Cube_Size, Cube_Size))
            if i.entity.id != 0:
                temp_world_section_entities.append(i)
        world_section_entities = temp_world_section_entities[:]

###################################### TEST #######################################################

    def draw_world():
        for i in world_section:
            screen.blit(image_resources[i.id][i.block_face], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]))


    def draw_world_backload_handler():
        while game_running:
            if not game_paused:
                global world_section_entities
                temp_world_section_entities = []
                for i in world_section:
                    if i.entity.id != 0:
                        temp_world_section_entities.append(i)
                world_section_entities = temp_world_section_entities[:]
            time.sleep(0.1)




    draw_world_backload = threading.Thread(target=draw_world_backload_handler)
    draw_world_backload.daemon = True
    draw_world_backload.start()
###################################################################################################



    def entities_update_handler():
        while game_running:
            if not game_paused:
                entity_remover()
                for i in world_section_entities:
                    if i.entity.id != 0:
                        i.entity.update(game_days)
                        i.entity.hitbox = pygame.Rect((i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]), (Cube_Size, Cube_Size))

            time.sleep(0.01)

    ##### Making light a surface before using it ########## (Still not sure if runs faster or not lol)
    light = image_resources[600][0]
    light_width, light_height = light.get_size()
    light2 = pygame.Surface(light.get_size(), pygame.SRCALPHA)
    light2.blit(light, (0, 0))
    #############################
    def draw_entities():
        mouse_x, mouse_y = mouse_position

        if night_value > 0:
            night_filter.fill((night_value, night_value, night_value))
        for i in world_section_entities:
            if i.entity.id != 0:
                if i.x == mouse_x and i.y == mouse_y:
                    # Draw Marker
                    screen.blit(image_resources[601][0], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1]))
                #print(image_resources[i.entity.id][i.entity.entity_face], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1] - image_resources[i.entity.id][i.entity.entity_face].get_height() + Cube_Size))
                screen.blit(image_resources[i.entity.id][i.entity.entity_face], (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1] - image_resources[i.entity.id][i.entity.entity_face].get_height() + Cube_Size))
                if i.entity.health < i.entity.max_health:
                    # Draw grey back
                    pygame.draw.rect(screen, (30, 30, 30), (i.x * Cube_Size - scroll[0] - 2, i.y * Cube_Size - scroll[1] + Cube_Size + 10 - 2, 30 + 4, 5 + 4))
                    # Draw life Green/Red
                    if i.entity.health >= i.entity.max_health/2:
                        pygame.draw.rect(screen, (127, 255, 0), (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1] + Cube_Size + 10, i.entity.health / 3.3, 5))
                    else:
                        pygame.draw.rect(screen, (255, 0, 0), (i.x * Cube_Size - scroll[0], i.y * Cube_Size - scroll[1] + Cube_Size + 10, i.entity.health / 3.3, 5))

                if night_value > 0:
                    night_filter.blit(light2, (i.x * Cube_Size - scroll[0] - light_width / 2, i.y * Cube_Size - scroll[1] - light_height / 2))



    def draw_drops():
        for i in drop_map_section:
            screen.blit(image_resources[i.id][i.face], (i.x - scroll[0], i.y - scroll[1] - image_resources[i.id][i.face].get_height() + Cube_Size))

    fps_reads_day = []
    fps_reads_night = []
    def show_fps(window, clock):
        if night_value > 0:
            fps_reads_night.append(int(clock.get_fps()))
        else:
            fps_reads_day.append(int(clock.get_fps()))
        if options.fps:
            fps_overlay = FPS_FONT.render(str(int(clock.get_fps())), True, color)
            window.blit(fps_overlay, (1240, 0))
        if options.coords:
            coors_overlay = FPS_FONT.render(str("Coordinates :" + str((int(player.x / Cube_Size), int(player.y / Cube_Size)))), True, color)
            window.blit(coors_overlay, (5, 0))



    def entity_remover():
        for i in entities_to_remove:
            x, y = i
            entity = world[x][y].entity
            if entity.id != 0:
                #print(entity.drop_list.pop(0))
                if entity.drop_list.pop(0):
                    for a in entity.drop_list:
                        for i in range(entity.entity_face + 1):
                            rand_x = random.randint(-30, 30)
                            rand_y = random.randint(-30, 30)
                            print(entity.x * Cube_Size + rand_x, entity.y * Cube_Size + rand_y, a, 1, game_days)
                            drop_map.append(Drop(entity.x * Cube_Size + rand_x, entity.y * Cube_Size + rand_y, a, 1, game_days))
                else:
                    print("wtf")
                    for i in entity.drop_list:
                        rand_x = random.randint(-30, 30)
                        rand_y = random.randint(-30, 30)
                        drop_map.append(Drop(entity.x * Cube_Size + rand_x, entity.y * Cube_Size + rand_y, i, 1, game_days))
                if entity.drop:
                    pass
                entity.destroy()

        entities_to_remove.clear()


    def collision_checker(x, y):
        map_size = len(world)
        if world[int(x / 30)][int(y / 30)].entity.collision:
            pass
        elif world[int(x/30)][int(y/30)].collision:
            pass
        elif int(x/30) < 25 or int(y/30) < 20 or int(x/30) > map_size - 25 or int(y/30) > map_size - 20:
            pass
        else:
            player.move(x, y)
            return True

        return False



    def block_face_checker():
        map_size = len(world)
        for x in range(map_size-1):
            for y in range(map_size-1):
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
        while game_running:
            if not game_paused:
                #Remove uncollected drops
                for x in reversed(drop_map):
                    if game_days - x.creation_day > 1:
                        drop_map.remove(x)

            time.sleep(10)


    def drop_manager():
        #global drop_map
        global drop_map_section
        while game_running:
            if not game_paused:
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
        while game_running:
            if not game_paused:
                # Move drops to player
                for i in drop_map_section:
                    if player.has_space_for_drop((i.id, i.quantity)):
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
                                if player.add_to_inventory((i.id, i.quantity)):
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
            if not game_paused:
                if timer >= 1440:
                    game_days += 1
                    timer = 0
                elif 1320 < timer < 1380:
                    if night_value <= 120:
                        night_value += 2
                elif 360 < timer < 420:
                    night_value -= 2

                timer += 1
            time.sleep(0.01)#time.sleep(1)


    def player_movement_handler():
        previous_run_time = time.time()
        time.time() - previous_run_time

        while game_running:
            if not game_paused:
                delay = time.time() - previous_run_time
                adjust_delay = player.speed * (delay - (Game_Tick / 15)) / (Game_Tick / 15)
                previous_run_time = time.time()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_a] and keys[pygame.K_w]:
                    if not collision_checker(player.x - int(player.speed * 90 / 100) - adjust_delay, player.y - int(player.speed * 90 / 100) - adjust_delay):
                        collision_checker(player.x - int(player.speed * 90 / 100) - adjust_delay, player.y)
                        collision_checker(player.x, player.y - int(player.speed * 90 / 100) - adjust_delay)
                elif keys[pygame.K_a] and keys[pygame.K_s]:
                    if not collision_checker(player.x - int(player.speed * 90 / 100) - adjust_delay, player.y + int(player.speed * 90 / 100) + adjust_delay):
                        collision_checker(player.x - int(player.speed * 90 / 100) - adjust_delay, player.y)
                        collision_checker(player.x, player.y + int(player.speed * 90 / 100) + adjust_delay)
                elif keys[pygame.K_d] and keys[pygame.K_w]:
                    if not collision_checker(player.x + int(player.speed * 90 / 100) + adjust_delay, player.y - int(player.speed * 90 / 100) - adjust_delay):
                        collision_checker(player.x + int(player.speed * 90 / 100) + adjust_delay, player.y)
                        collision_checker(player.x, player.y - int(player.speed * 90 / 100) - adjust_delay)
                elif keys[pygame.K_d] and keys[pygame.K_s]:
                    if not collision_checker(player.x + int(player.speed * 90 / 100) + adjust_delay, player.y + int(player.speed * 90 / 100) + adjust_delay):
                        collision_checker(player.x + int(player.speed * 90 / 100) + adjust_delay, player.y)
                        collision_checker(player.x, player.y + int(player.speed * 90 / 100) + adjust_delay)

                elif keys[pygame.K_a]:
                    collision_checker(player.x - player.speed - adjust_delay, player.y)
                elif keys[pygame.K_d]:
                    collision_checker(player.x + player.speed + adjust_delay, player.y)
                elif keys[pygame.K_w]:
                    collision_checker(player.x, player.y - player.speed - adjust_delay)
                elif keys[pygame.K_s]:
                    collision_checker(player.x, player.y + player.speed + adjust_delay)

            time.sleep(Game_Tick/15)
            #print(pygame.time.get_ticks() - start_time)


    def mouse_movement_handler():
        global mouse_position
        while game_running:
            if not game_paused:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                block_x = int((mouse_x * (1 / 30)) + (scroll[0] * (1 / 30)))
                block_y = int((mouse_y * (1 / 30)) + (scroll[1] * (1 / 30)))
                mouse_position = (block_x, block_y)

            time.sleep(0.01)


    def mouse_clicker_handler():
        while game_running:
            if not game_paused:
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

    def idle_annimations_handler():
        idx = 0
        while game_running:
            if not game_paused:
                for i in idle_animation_list:
                    if i.last_move < time.time():
                        if idx >= len(i.images_idle) - 1:
                            idx = 0
                        else:
                            i.image = i.images_idle[idx]
                            idx += 1

            time.sleep(0.08)




    idle_annimations = threading.Thread(target=idle_annimations_handler)
    idle_annimations.daemon = True
    idle_annimations.start()

    entities_update = threading.Thread(target=entities_update_handler)
    entities_update.daemon = True
    entities_update.start()

    player_movement = threading.Thread(target=player_movement_handler)
    player_movement.daemon = True
    player_movement.start()

    mouse_movement = threading.Thread(target=mouse_movement_handler)
    mouse_movement.daemon = True
    mouse_movement.start()

    mouse_clicker = threading.Thread(target=mouse_clicker_handler)
    mouse_clicker.daemon = True
    mouse_clicker.start()

    update_visible_world = threading.Thread(target=update_world_section)
    update_visible_world.daemon = True
    update_visible_world.start()

    drop_timeout = threading.Thread(target=drop_timeout_remover)
    drop_timeout.daemon = True
    drop_timeout.start()

    drop_man = threading.Thread(target=drop_manager)
    drop_man.daemon = True
    drop_man.start()

    drop_col_man = threading.Thread(target=drop_collection_manager)
    drop_col_man.daemon = True
    drop_col_man.start()

    time_handler = threading.Thread(target=time_handler)
    time_handler.daemon = True
    time_handler.start()


    block_face_checker()

    button_pressed = False

    minimap_open = False
    inventory_open = False
    last_time_esc_pressed = 0

    #pygame.display.toggle_fullscreen()

    # -------- Main Program Loop -----------
    while playing:

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_F2:
                    if options.fullscreen:
                        options.update_fullscreen()
                        screen = pygame.display.set_mode(size, pygame.SCALED | pygame.FULLSCREEN)
                    else:
                        options.update_fullscreen()
                        screen = pygame.display.set_mode(size, pygame.SCALED)
                if e.key == pygame.K_ESCAPE:
                    print(time.time() - last_time_esc_pressed)
                    if time.time() - last_time_esc_pressed > 2:
                        last_time_esc_pressed = time.time()
                        print("MAX FPS DAY: " + str(max(fps_reads_day)))
                        print("MIN FPS DAY: " + str(min(fps_reads_day)))
                        print("AVERAGE FPS DAY: " + str(sum(fps_reads_day) / len(fps_reads_day)))
                        print("MAX FPS NIGHT: " + str(max(fps_reads_night)))
                        print("MIN FPS NIGHT: " + str(min(fps_reads_night)))
                        print("AVERAGE FPS NIGHT: " + str(sum(fps_reads_night) / len(fps_reads_night)))
                        world_loader.save(world, player, drop_map)
                        esc_menu()
                if e.key == pygame.K_m:
                    if minimap_open:
                        minimap_open = False
                    else:
                        minimap_open = True
                if e.key == pygame.K_e:
                    if inventory_open:
                        inventory_open = False
                    else:
                        inventory_open = True
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 4:  #Scroll wheel
                    inventory_selected_slot -= 1
                    if inventory_selected_slot < 0:
                        inventory_selected_slot = 7
                elif e.button == 5:  #Scroll wheel
                    inventory_selected_slot += 1
                    if inventory_selected_slot > 7:
                        inventory_selected_slot = 0
            if e.type == pygame.QUIT:
                global game_running
                world_loader.save(world, player, drop_map)
                playing = False
                game_running = False
                pygame.quit()
                exit()
                break

        #screen.fill('white')

        start_time = time.time()
        screen_width, screen_height = screen.get_size()
        true_scroll[0] += (player.x - true_scroll[0] - (screen_width / 2)) / 20
        true_scroll[1] += (player.y - true_scroll[1] - (screen_height / 2)) / 20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        #print(scroll)
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
        screen.blit(player.get_image(), rect)
        pygame.draw.rect(screen, RED, rect, 1)
        #print("--- Player: %s seconds ---" % (time.time() - start_time))
        #screen.blit(player.image, (player.x - scroll[0], player.y - scroll[1]))
        start_time = time.time()
        show_fps(screen, clock)
        #print("--- FPS: %s seconds ---" % (time.time() - start_time))

        if night_value > 0:
            start_time = time.time()
            screen.blit(night_filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
            #screen.blit(night_filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
            #screen.blit(night_filter, (0, 0), special_flags=pygame.BLEND_SUB)
            #print("--- Night: %s seconds ---" % (time.time() - start_time))

        if minimap_open:
            screen.blit(minimap, (0, 0))
            screen.blit(minimap_head, (int(player.x / Cube_Size), int(player.y / Cube_Size)))

        #print(player.inventory)

        screen.blit(inventory_image[0], (850, 30))
        #print(player.inventory)

        for idx, i in enumerate(player.inventory):
            if idx < 8:
                if idx == inventory_selected_slot:
                    screen.blit(inventory_image_selected, (850 + idx * 50, 30))
                    if i is None:
                        player.hand_image = ""
                    else:
                        player.hand_image = image_resources[i[0]][0]
                if i != None:
                    screen.blit(image_resources[i[0]][0], (860 + idx * 50, 40))
                    quantity = inventory_font.render(str(i[1]), True, inventory_font_color)
                    screen.blit(quantity, (857 + idx * 50, 35))

            else:
                break
        if inventory_open:
            screen.blit(inventory_image[1], (850, 85))
            for idx, i in enumerate(player.inventory):
                if 16 > idx >= 8:
                    if idx == inventory_selected_slot:
                        if i is None:
                            player.hand_image = ""
                        else:
                            player.hand_image = image_resources[i[0]][0]
                    if i != None:
                        screen.blit(image_resources[i[0]][0], (860 + (idx - 8) * 50, 40 + 50))
                        quantity = inventory_font.render(str(i[1]), True, inventory_font_color)
                        screen.blit(quantity, (857 + (idx - 8) * 50, 35 + 50))
                if 24 > idx >= 16:
                    if idx == inventory_selected_slot:
                        if i is None:
                            player.hand_image = ""
                        else:
                            player.hand_image = image_resources[i[0]][0]
                    if i != None:
                        screen.blit(image_resources[i[0]][0], (860 + (idx - 16) * 50, 40 + 100))
                        quantity = inventory_font.render(str(i[1]), True, inventory_font_color)
                        screen.blit(quantity, (857 + (idx - 16) * 50, 35 + 100))
                if 32 > idx >= 24:
                    if idx == inventory_selected_slot:
                        if i is None:
                            player.hand_image = ""
                        else:
                            player.hand_image = image_resources[i[0]][0]
                    if i != None:
                        screen.blit(image_resources[i[0]][0], (860 + (idx - 24) * 50, 40 + 150))
                        quantity = inventory_font.render(str(i[1]), True, inventory_font_color)
                        screen.blit(quantity, (857 + (idx - 24) * 50, 35 + 150))


        pygame.display.flip()

        clock.tick(120)


main_menu()

#play()

pygame.quit()
game_running = False
