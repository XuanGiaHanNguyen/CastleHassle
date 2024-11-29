import pygame

Data =[
[14,0,0,17,0,14,17,0,14,0],
[15,12,0,17,0,15,0,0,0,0],
[15,14,0,10,0,15,13,0,12,0],
[15,0,3,1,12,0,0,0,0,14],
[0,13,0,14,0,0,0,3,1,1],
[0,0,0,15,17,0,0,8,0,0],
[0,0,0,0,17,0,0,8,12,0],
[0,0,13,0,0,0,0,8,0,13],
[16,0,0,0,0,0,0,8,0,0],
[1,1,2,4,4,4,4,4,3,1]
]

class Assets():
    def __init__(self,Data, tile_size,screen):

        five = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/castleHalfLeft.png')
        six = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/castleHalfRight.png')
        seven = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/castleHalfMid.png')
        eight = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/ladder_mid.png')
        nine = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/fence.png')
        twelve = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/tochLit2.png')
        thirteen = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/window.png')
        fourteen = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/ropeAttached.png')
        fifteen = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/ropeVertical.png')
        sixteen = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/signRight.png')
        seventeen = pygame.image.load('/Users/han/PycharmProjects/Castle Hassle /Set/chain.png')

        self.tile_group =[]
        row_count = 0
        for row in Data:
            col_count = 0
            for tile  in row:

                if tile == 5:
                    E = pygame.transform.scale(five,(tile_size,tile_size))
                    E_rect = E.get_rect()
                    E_rect.x = col_count*tile_size
                    E_rect.y = row_count * tile_size
                    tiles = (E,E_rect)
                    self.tile_group.append(tiles)
                if tile == 6:
                    F = pygame.transform.scale(six,(tile_size,tile_size))
                    F_rect = F.get_rect()
                    F_rect.x = col_count*tile_size
                    F_rect.y = row_count * tile_size
                    tiles = (F,F_rect)
                    self.tile_group.append(tiles)
                if tile == 7:
                    G = pygame.transform.scale(seven,(tile_size,tile_size))
                    G_rect = G.get_rect()
                    G_rect.x = col_count*tile_size
                    G_rect.y = row_count * tile_size
                    tiles = (G,G_rect)
                    self.tile_group.append(tiles)
                if tile == 8:
                    H = pygame.transform.scale(eight,(tile_size,tile_size))
                    H_rect = H.get_rect()
                    H_rect.x = col_count*tile_size
                    H_rect.y = row_count * tile_size
                    tiles = (H,H_rect)
                    self.tile_group.append(tiles)
                if tile == 9:
                    I = pygame.transform.scale(nine,(tile_size,tile_size))
                    I_rect = I.get_rect()
                    I_rect.x = col_count*tile_size
                    I_rect.y = row_count * tile_size
                    tiles = (I,I_rect)
                    self.tile_group.append(tiles)

                if tile == 12:
                    L = pygame.transform.scale(twelve,(tile_size,tile_size))
                    L_rect = L.get_rect()
                    L_rect.x = col_count*tile_size
                    L_rect.y = row_count * tile_size
                    tiles = (L,L_rect)
                    self.tile_group.append(tiles)
                if tile == 13:
                    M = pygame.transform.scale(thirteen,(tile_size,tile_size))
                    M_rect = M.get_rect()
                    M_rect.x = col_count*tile_size
                    M_rect.y = row_count * tile_size
                    tiles = (M,M_rect)
                    self.tile_group.append(tiles)
                if tile == 14:
                    N = pygame.transform.scale(fourteen,(tile_size,tile_size))
                    N_rect = N.get_rect()
                    N_rect.x = col_count*tile_size
                    N_rect.y = row_count * tile_size
                    tiles = (N,N_rect)
                    self.tile_group.append(tiles)
                if tile == 15:
                    O = pygame.transform.scale(fifteen,(tile_size,tile_size))
                    O_rect = O.get_rect()
                    O_rect.x = col_count*tile_size
                    O_rect.y = row_count * tile_size
                    tiles = (O,O_rect)
                    self.tile_group.append(tiles)
                if tile == 16:
                    P = pygame.transform.scale(sixteen,(tile_size,tile_size))
                    P_rect = P.get_rect()
                    P_rect.x = col_count*tile_size
                    P_rect.y = row_count * tile_size
                    tiles = (P,P_rect)
                    self.tile_group.append(tiles)

                col_count += 1
            row_count += 1

    def draw(self,screen):
        for tiles in self.tile_group:
            screen.blit(tiles[0],tiles[1])
