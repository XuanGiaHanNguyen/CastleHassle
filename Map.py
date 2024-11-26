import pygame

World_Data =[
[14,0,5,6,3,0,0,0,0,11],
[1,2,0,0,0,15,0,0,0,10],
[15,0,0,0,0,0,0,0,3,1],
[15,0,3,2,0,0,0,0,0,0],
[0,0,0,0,3,2,0,0,0,0],
[0,0,0,0,0,0,8,0,3,1],
[3,2,0,0,0,0,8,0,12,0],
[0,0,0,0,0,3,1,2,0,13],
[0,0,0,0,0,0,0,0,0,0],
[1,1,2,4,4,4,4,4,3,1]
]


class World():
    def __init__(self,World_Data, tile_size,screen):
        self.enemy_group = pygame.sprite.Group

        one = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/castleMid.png')
        two = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/castleRight.png')
        three = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/castleLeft.png')
        ten = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/door_openMid.png')
        eleven = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/door_openTop.png')

        self.tile_group =[]
        row_count = 0
        for row in World_Data:
            col_count = 0
            for tile  in row:
                if tile == 1:
                    A = pygame.transform.scale(one,(tile_size,tile_size))
                    A_rect = A.get_rect()
                    A_rect.x = col_count*tile_size
                    A_rect.y = row_count * tile_size
                    tiles = (A,A_rect)
                    self.tile_group.append(tiles)
                if tile == 2:
                    B = pygame.transform.scale(two,(tile_size,tile_size))
                    B_rect = B.get_rect()
                    B_rect.x = col_count*tile_size
                    B_rect.y = row_count * tile_size
                    tiles = (B,B_rect)
                    self.tile_group.append(tiles)
                if tile == 3:
                    C = pygame.transform.scale(three,(tile_size,tile_size))
                    C_rect = C.get_rect()
                    C_rect.x = col_count*tile_size
                    C_rect.y = row_count * tile_size
                    tiles = (C,C_rect)
                    self.tile_group.append(tiles)
                if tile == 4:
                    lava = Lava(col_count*(tile_size-1.3), row_count * tile_size+14,tile_size)
                    lava_group.add(lava)

                if tile == 10:
                    J = pygame.transform.scale(ten,(tile_size,tile_size))
                    J_rect = J.get_rect()
                    J_rect.x = col_count*tile_size
                    J_rect.y = row_count * tile_size
                    tiles = (J,J_rect)
                    self.tile_group.append(tiles)
                if tile == 11:
                    K = pygame.transform.scale(eleven,(tile_size,tile_size))
                    K_rect = K.get_rect()
                    K_rect.x = col_count*tile_size
                    K_rect.y = row_count * tile_size
                    tiles = (K,K_rect)
                    self.tile_group.append(tiles)

                col_count += 1
            row_count += 1

    def draw(self,screen):
        for tiles in self.tile_group:
            screen.blit(tiles[0],tiles[1])

class Lava(pygame.sprite.Sprite):
    def __init__(self,x,y,tile_size):
        pygame.sprite.Sprite.__init__(self)

        #must have self.image
        self.image = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/liquidLavaTop_mid.png')
        self.lava = pygame.transform.scale(self.image,(tile_size, tile_size // 2))
        self.rect = self.lava.get_rect()
        self.rect.x = x
        self.rect.y = y

lava_group = pygame.sprite.Group()

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self,screen):

        action = False

        screen.blit(self.image,self.rect)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked is False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] is False:
            self.clicked = False

        return action

class Guide():
    def __init__(self,x,y,screen,Button):
        self.IsGuide = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Guide_screen.png")
        self.GotIt = pygame.image.load("/Users/han/PycharmProjects/Castle Hassle /Buttons/Got_It.png")
        self.got_it = pygame.transform.scale(self.GotIt, (200, 85))
        self.is_guide = pygame.transform.scale(self.IsGuide, (500, 470))

        self.rect = self.is_guide.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

        self.got_it_button = Button(200,435,self.got_it)

    def draw(self,screen):
        screen.blit(self.is_guide, self.rect)

        return self.got_it_button.draw(screen)







