import pygame
from config import *

# bomba 1
bomba_v1 = pygame.image.load("images/Bomba.png")
inim_pos_x_v1 = 200  # x inicial
inim_pos_y_v1 = 400  # y inicial
sentido_x_v1 = 1
sentido_y_v1 = 1

# bomba 2
bomba_v2 = pygame.image.load("images/Bomba.png")
inim_pos_x_v2 = 400  # x inicial
inim_pos_y_v2 = 100  # y inicial
sentido_x_v2 = 1
sentido_y_v2 = 1

bomba_v1 = pygame.transform.scale(bomba_v1, (48, 48))
bomba_v2 = pygame.transform.scale(bomba_v2, (48, 48))
explosao = pygame.image.load("images/Explosão.png")

def sheets_inimigo_1():
    global frames, spt_wdt, spt_hgt, direita, esquerda, cima, inim_pos_x, inim_pos_y, screen, sentido, bomba_v1, bomba_v2


def getBomba_V1():
    return bomba_v1

def getBomba_V2():
    return bomba_v2

def animacao_inimigo(dt):
    global inim_pos_x_v1, inim_pos_y_v1, inim_pos_x_v2, inim_pos_y_v2, sentido_x_v1, sentido_y_v1, sentido_x_v2, sentido_y_v2

    # bomba 1
    if (sentido_x_v1 == 1):  # se ela estiver indo para direita (ida)
        inim_pos_x_v1 += 0.3 * dt
        if (inim_pos_x_v1 > 910):
            sentido_x_v1 = 2
    elif (sentido_x_v1 == 2):  # se ela estiver indo para esquerda (volta)
        inim_pos_x_v1 -= 0.3 * dt
        if (inim_pos_x_v1 < 1):
            sentido_x_v1 = 1

    if (sentido_y_v1 == 1):  # se ele estiver subindo
        inim_pos_y_v1 += 0.2 * dt
        if (inim_pos_y_v1 > 580):
            sentido_y_v1 = 2

    elif (sentido_y_v1 == 2):  # se ele estiver descendo
        inim_pos_y_v1 -= 0.2 * dt
        if (inim_pos_y_v1 < 1):
            sentido_y_v1 = 1

    # bomba 2
    if (sentido_x_v2 == 1):  # se ela estiver indo para direita (ida)
        inim_pos_x_v2 += 0.3 * dt
        if (inim_pos_x_v2 > 910):
            sentido_x_v2 = 2
    elif (sentido_x_v2 == 2):  # se ela estiver indo para esquerda (volta)
        inim_pos_x_v2 -= 0.3 * dt
        if (inim_pos_x_v2 < 1):
            sentido_x_v2 = 1

    if (sentido_y_v2 == 1):  # se ele estiver subindo
        inim_pos_y_v2 += 0.2 * dt
        if (inim_pos_y_v2 > 580):
            sentido_y_v2 = 2

    elif (sentido_y_v2 == 2):  # se ele estiver descendo
        inim_pos_y_v2 -= 0.2 * dt
        if (inim_pos_y_v2 < 1):
            sentido_y_v2 = 1

def getInimsPos():
    return [inim_pos_x_v1, inim_pos_y_v1, inim_pos_x_v2, inim_pos_y_v2]

# desenha o personagem animado na tela
def draw_inimigo_1(screen):
    global bomba_v1, bomba_v2
    screen.blit(bomba_v1, (inim_pos_x_v1, inim_pos_y_v1))
    screen.blit(bomba_v2, (inim_pos_x_v2, inim_pos_y_v2))
