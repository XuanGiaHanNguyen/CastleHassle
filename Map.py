import pygame

World_Data =[
[14,6,0,0,3,0,0,0,0,11],
[1,2,0,0,0,15,0,0,0,10],
[15,0,6,5,0,0,0,0,3,1],
[15,0,3,2,0,5,0,0,0,0],
[0,0,0,0,3,2,0,0,5,6],
[7,6,0,0,0,0,0,0,3,1],
[3,2,0,0,0,5,6,0,12,0],
[0,0,0,0,3,2,0,0,13,0],
[0,0,5,0,0,0,0,0,0,8],
[1,1,2,4,4,4,4,4,3,1]
]

class World():
    def __init__(self,World_Data, tile_size,screen):
        self.enemy_group = pygame.sprite.Group

        one = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/castleMid.png')
        two = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/castleRight.png')
        three = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/castleLeft.png')

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
                    lava = Lava(col_count * (tile_size - 1.3), row_count * tile_size + 14, tile_size)
                    lava_group.add(lava)

                if tile == 10:
                    door1 = Door1(col_count*(tile_size)-5, row_count * tile_size-10,tile_size)
                    door1_group.add(door1)

                if tile == 5:
                    bronze = BronzeCoin(col_count * tile_size, row_count * tile_size, tile_size)
                    bronze_group.add(bronze)

                if tile == 6:
                    gold = GoldCoin(col_count*tile_size, row_count * tile_size,tile_size)
                    gold_group.add(gold)

                if tile == 11:
                    door2 = Door2(col_count * tile_size-5, row_count * tile_size-10, tile_size)
                    door2_group.add(door2)

                if tile == 7:
                    secret = Secret(col_count*tile_size, row_count * tile_size,tile_size/2)
                    secret_group.add(secret)

                if tile == 8:
                    box = Box(col_count * tile_size, row_count * tile_size, tile_size/2)
                    box_group.add(box)
                    key = Key(col_count * tile_size, row_count * tile_size, tile_size/2)
                    key_group.add(key)

                col_count += 1
            row_count += 1

    def draw(self,screen):
        for tiles in self.tile_group:
            screen.blit(tiles[0],tiles[1])

    def reset_coins(self,World_Data, tile_size,gold_group, bronze_group):
        gold_group.empty()
        bronze_group.empty()
        row_count = 0

        for row in World_Data:
            col_count = 0
            for tile in row:
                if tile == 5:
                    bronze = BronzeCoin(col_count * tile_size, row_count * tile_size, tile_size)
                    bronze_group.add(bronze)

                if tile == 6:
                    gold = GoldCoin(col_count*tile_size, row_count * tile_size,tile_size)
                    gold_group.add(gold)

                col_count += 1
            row_count += 1



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
        self.is_guide = pygame.transform.scale(self.IsGuide, (500, 410))

        self.rect = self.is_guide.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

        self.got_it_button = Button(200,400,self.got_it)

    def draw(self,screen):
        screen.blit(self.is_guide, self.rect)

        return self.got_it_button.draw(screen)

class Door1(pygame.sprite.Sprite):
    def __init__(self,x,y,tile_size):
        pygame.sprite.Sprite.__init__(self)

        #must have self.image
        self.image = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/door_openMid.png')
        self.door1 = pygame.transform.scale(self.image,(tile_size, tile_size))
        self.rect = self.door1.get_rect()
        self.rect.x = x
        self.rect.y = y

door1_group = pygame.sprite.Group()

class Door2(pygame.sprite.Sprite):
    def __init__(self,x,y,tile_size):
        pygame.sprite.Sprite.__init__(self)

        #must have self.image
        self.image = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/door_openTop.png')
        self.door2 = pygame.transform.scale(self.image,(tile_size, tile_size))
        self.rect = self.door2.get_rect()
        self.rect.x = x
        self.rect.y = y

door2_group = pygame.sprite.Group()

class GoldCoin(pygame.sprite.Sprite):
    def __init__(self,x,y,tile_size):
        pygame.sprite.Sprite.__init__(self)

        #must have self.image
        self.image = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/coinGold.png')
        self.gold = pygame.transform.scale(self.image,(tile_size/2, tile_size/2))
        self.rect = self.gold.get_rect()
        self.rect.x = x
        self.rect.y = y

gold_group = pygame.sprite.Group()

class BronzeCoin(pygame.sprite.Sprite):
    def __init__(self,x,y,tile_size):
        pygame.sprite.Sprite.__init__(self)

        #must have self.image
        self.image = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/coinBronze.png')
        self.bronze = pygame.transform.scale(self.image,(tile_size/2, tile_size/2))
        self.rect = self.bronze.get_rect()
        self.rect.x = x
        self.rect.y = y

bronze_group = pygame.sprite.Group()
####
class Box(pygame.sprite.Sprite):
    def __init__(self,x,y,tile_size):
        pygame.sprite.Sprite.__init__(self)

        #must have self.image
        self.image = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Secret/boxAlt.png')
        self.image = pygame.transform.scale(self.image, (tile_size + 30, tile_size + 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

box_group = pygame.sprite.Group()

class Key(pygame.sprite.Sprite):
    def __init__(self,x,y,tile_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Secret/keyRed.png')
        self.image = pygame.transform.scale(self.image, (tile_size + 30, tile_size + 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

key_group = pygame.sprite.Group()

class Secret(pygame.sprite.Sprite):
    def __init__(self,x,y,tile_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Secret/lock_blue.png')
        self.image = pygame.transform.scale(self.image,(tile_size+30,tile_size+30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

secret_group = pygame.sprite.Group()


