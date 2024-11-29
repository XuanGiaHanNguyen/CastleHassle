import pygame
import Map
from Map import World_Data, lava_group, door1_group, door2_group, gold_group, bronze_group, key_group,box_group, secret_group
from Map import Button
from Map import Guide
import Assets
from Assets import Data
import pickle


pygame.init()
Clock = pygame.time.Clock()
fps = 60

#Create_screen
ScreenX = 600
ScreenY = 600
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Castle Hassle")

restart = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Replay.png")
restart_but = pygame.transform.scale(restart,(395,180))

rest = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Rett.png")
rest_but = pygame.transform.scale(rest,(350,110))

bg = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Set/bg_castle.png")
back = pygame.transform.scale(bg,(600,600))

Title = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Title.png")
title = pygame.transform.scale(Title,(440,270))

play = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Play.png")
play_but = pygame.transform.scale(play,(300,100))

guide = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Guide.png")
guide_but = pygame.transform.scale(guide,(320,100))

re = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Return.png")
re_but = pygame.transform.scale(re,(330,120))

exit1 = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Exit.png")
exit_but1 = pygame.transform.scale(exit1,(320,100))

you_die = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/U fell!.png")
Dead = pygame.transform.scale(you_die,(395,430))

you_win = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Winner.png")
Win = pygame.transform.scale(you_win,(395,430))

you_fool = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Secret/FOOL.png")
Fool = pygame.transform.scale(you_fool,(395,430))

keied = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Secret/Key-ed.png")
Keied = pygame.transform.scale(keied,(395,430))

tile_size = 60
game_over = 0
is_menu = True
is_guide = False
score = 0

import Character

world = Map.World(World_Data,tile_size,screen)
world.enemy_group = pygame.sprite.Group
character = Character.Character(30,500)
asset = Assets.Assets(Data,tile_size,screen)

ret_button = Map.Button(140,360,re_but)
restart_button = Map.Button(135,320,restart_but)
return_button = Map.Button(130,220,rest_but)
play_button = Map.Button(150,265,play_but)
guide_button = Map.Button(160,365,guide_but)
exit_button1 = Map.Button(166,465,exit_but1)

#return_button = Map.Button(140,360,restart_but)

guide = Map.Guide(60,100,screen,Map.Button)


#Loop_for_running#
running = True

while running is True:

    Clock.tick(fps)

    screen.blit(back,(0,0))

    if is_menu is True:

        screen.blit(title,(80,5))
        if Button.draw(play_button,screen) is True:
            is_menu = False

        if Button.draw(guide_button,screen) is True:
            is_guide = True

        if Button.draw(exit_button1, screen) is True:
            running = False

    if is_guide is True:
        if guide.draw(screen) is True:
            is_menu = True
            is_guide = False
            running = True


    if is_menu is False:

        world.draw(screen)
        asset.draw(screen)
        lava_group.draw(screen)
        door1_group.draw(screen)
        door2_group.draw(screen)
        bronze_group.draw(screen)
        gold_group.draw(screen)
        key_group.draw(screen)
        box_group.draw(screen)
        secret_group.draw(screen)

        character.display_score(10,10,screen)

        game_over = character.update(screen,ScreenY,world.tile_group,game_over)

        if game_over == 1:
            screen.blit(Dead,(105,80))

            Action = Button.draw(restart_button,screen)
            Action2 = Button.draw(return_button, screen)

            if Action is True:
                character.restart(30,500)
                game_over = 0
                world.reset_coins(Map.World_Data,tile_size,gold_group,bronze_group)

            if Action2 is True:
                is_menu = True
                is_guide = False
                character.restart(30, 500)
                game_over = 0
                world.reset_coins(Map.World_Data, tile_size, gold_group, bronze_group)

        if game_over == 2:
            screen.blit(Win, (105, 80))
            Action = Button.draw(ret_button, screen)

            if Action is True:
                is_menu = True
                is_guide = False
                character.restart(30, 500)
                game_over = 0
                world.reset_coins(Map.World_Data, tile_size, gold_group, bronze_group)

        if game_over == 3:
            screen.blit(Fool, (105, 80))
            Action = Button.draw(ret_button, screen)

            if Action is True:
                is_menu = True
                is_guide = False
                character.restart(30, 500)
                game_over = 0
                world.reset_coins(Map.World_Data, tile_size, gold_group, bronze_group)

        if game_over == 4:
            screen.blit(Keied, (105, 80))
            Action = Button.draw(ret_button, screen)

            if Action is True:
                is_menu = True
                is_guide = False
                character.restart(30, 500)
                game_over = 0
                world.reset_coins(Map.World_Data, tile_size, gold_group, bronze_group)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
