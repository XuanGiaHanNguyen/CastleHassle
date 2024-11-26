import pygame
import Map
from Map import World_Data, lava_group
from Map import Button
from Map import Guide
import Assets
from Assets import Data


pygame.init()
Clock = pygame.time.Clock()
fps = 60

#Create_screen
ScreenX = 600
ScreenY = 600
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Castle Hassle")

restart = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Replay.png")
restart_but = pygame.transform.scale(restart,(380,130))

bg = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Set/bg_castle.png")
back = pygame.transform.scale(bg,(600,600))

Title = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Title.png")
title = pygame.transform.scale(Title,(440,270))

play = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Play.png")
play_but = pygame.transform.scale(play,(250,100))

guide = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Guide.png")
guide_but = pygame.transform.scale(guide,(280,99))

exit = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Exit.png")
exit_but = pygame.transform.scale(exit,(280,100))

you_die = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/U_fell!.png")
Dead = pygame.transform.scale(you_die,(380,430))

#########
IsGuide = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Guide_screen.png")
is_guide = pygame.transform.scale(IsGuide,(530,530))

GotIt = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Got_It.png")
got_it = pygame.transform.scale(GotIt,(250,100))
#########

tile_size = 60
game_over = 0
is_menu = True
is_guide = False

import Character

world = Map.World(World_Data,tile_size,screen)
world.enemy_group = pygame.sprite.Group
character = Character.Character(30,500)
asset = Assets.Assets(Data,tile_size,screen)

restart_button = Map.Button(140,360,restart_but)
play_button = Map.Button(180,265,play_but)
guide_button = Map.Button(183,365,guide_but)
exit_button = Map.Button(189,465,exit_but)

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

        if Button.draw(exit_button, screen) is True:
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

        game_over = character.update(screen,ScreenY,world.tile_group,game_over)
        if game_over == 1:
            screen.blit(Dead,(110,80))
            Action = Button.draw(restart_button,screen)
            
            if Action is True:
                character.restart(30,500)
                game_over = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
