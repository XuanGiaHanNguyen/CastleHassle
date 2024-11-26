import pygame

from Map import lava_group

class Character():

    def __init__(self,x,y):
        self.restart(x,y)

    def update(self,screen,screenY,tile_group,game_over):
        dx = 0
        dy = 0
        walk_cooldown = 4

        if game_over == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                dx -= 3
                self.counter +=1
                self.direction = -1
            elif key[pygame.K_d]:
                dx += 3
                self.counter += 1
                self.direction = 1

            if key[pygame.K_SPACE] and self.jump is False and self.in_air is False:
                self.vel_y -= 9
                self.jump = True

            if key[pygame.K_SPACE] is False:
                self.jump = False

            if key[pygame.K_d] is False and key[pygame.K_a] is False:
                self.index = 0
                self.counter = 0
                if self.direction == 1:
                    self.char = self.img_r[self.index]
                if self.direction == -1:
                    self.char = self.img_l[self.index]


            if self.counter == walk_cooldown:
                self.index += 1
                if self.index >= len(self.img_r):
                    self.index =0
                if self.direction == 1:
                    self.char = self.img_r[self.index]
                if self.direction == -1:
                    self.char = self.img_l[self.index]
                self.counter = 0

            self.vel_y += 0.3
            if self.vel_y > 5.5:
                self.vel_y = 5.5

            self.in_air = True
            for tiles in tile_group:
                if tiles[1].colliderect(self.rect.x + dx, self.rect.y,self.width,self.height):
                    dx = 0

                if tiles[1].colliderect(self.rect.x, self.rect.y +dy,self.width,self.height):
                    if self.vel_y >0:
                        dy = tiles[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

                    elif self.vel_y <0:
                        dy = tiles[1].bottom - self.rect.top
                        self.vel_y = 0
                        self.in_air = True

            if pygame.sprite.spritecollide(self,lava_group,False):
                game_over = 1

        elif game_over ==1:
            self.char = self.image_dead
            self.rect.y -= 8


        dy += self.vel_y

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.top > screenY:  # If the character falls below the screen
            game_over = 1  # Trigger game-over state

        screen.blit(self.char,self.rect)

        return game_over

    def restart(self,x,y):

        self.img_r = []
        self.img_l = []
        self.index = 0
        self.counter = 0
        self.direction = 0


        for num in range(1, 10):
            img = pygame.image.load(f"/Users/han/PycharmProjects/Castle Hassle /Player/p3_walk0{num}.png")
            cha = pygame.transform.scale(img, (72, 97))
            che = pygame.transform.flip(cha, True, False)
            self.img_l.append(che)
            self.img_r.append(cha)
        for num in range(10, 12):
            img = pygame.image.load(f"/Users/han/PycharmProjects/Castle Hassle /Player/p3_walk{num}.png")
            cha = pygame.transform.scale(img, (72, 97))
            che = pygame.transform.flip(cha, True, False)
            self.img_r.append(cha)
            self.img_l.append(che)

        img = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Player/Dead.png")
        self.image_dead = pygame.transform.scale(img, (72, 87))

        self.char = self.img_r[self.index]
        self.rect = self.char.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jump = False
        self.width = self.char.get_width()
        self.height = self.char.get_height()
        self.is_air = False

