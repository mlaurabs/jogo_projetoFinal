import pygame
from config import *

inim_pos_x = 200 # x inicial
inim_pos_y = 400 # y inicial
sentido_x = 1
sentido_y = 1
# importa textura personagem

def sheets_inimigo_1():
    global frames, spt_wdt, spt_hgt, direita, esquerda, cima, inim_pos_x, inim_pos_y, screen, sentido


# logica da movimentacao
def inimigoColisao(): # modificar
    #inimigo = pygame.Rect(inim_pos_x, inim_pos_y, 100, 100)
    #return inimigo
    pass

def animacao_inimigo(dt):
    global inim_pos_x, inim_pos_y, sentido_x, sentido_y

    if (sentido_x == 1):  # se ela estiver indo para direita (ida)
        inim_pos_x += 0.3 * dt
        if (inim_pos_x > 910):
            sentido_x = 2
    elif (sentido_x == 2):  # se ela estiver indo para esquerda (volta)
        inim_pos_x -= 0.3 * dt
        if (inim_pos_x < 1):
            sentido_x = 1

    if(sentido_y == 1): # se ele estiver subindo
        inim_pos_y += 0.2 * dt
        if (inim_pos_y > 580):
            print("sentido a")
            print((inim_pos_y))
            sentido_y = 2

    elif(sentido_y == 2): # se ele estiver descendo
        inim_pos_y -= 0.2 * dt
        if (inim_pos_y < 1):
            print("sentido b")
            sentido_y = 1
            print((inim_pos_y))

# logia da colisao
"""
inimigo_rect = pygame.Rect(anim_pos_x, anim_pos_y, spt_wdt, spt_hgt)
    jogador_rect = jogador_rect.inflate(-25, -20)
    textura3 = pygame.transform.scale(pygame.image.load("images/tijolo.png"), (22,22)) # c
    key = pygame.image.load("images/key.png")

    
    # verifica se o jogador está em contato com qualquer bloquinho "C"
    for i in range(20):
        for j in range(30):
            if (mapa[i][j] == 'C'):
                if jogador_rect.colliderect(textura3.get_rect(topleft=(j * 32, i * 32))):
                    anim_pos_x = old_x
                    anim_pos_y = old_y
   
    # verifica se o jogador está em contato com a chave   
        if jogador_rect.colliderect(key.get_rect(topleft=(j * 32, i * 32))):
            anim_pos_x = old_x
            anim_pos_y = old_y
"""
                  
# desenha o personagem animado na tela                    
def draw_inimigo_1(screen):
   #pygame.draw.rect(screen, (255, 0, 0), (anim_pos_x, anim_pos_y, 50, 50))
   bomba = pygame.image.load("images/Bomba.png")
   bomba = pygame.transform.scale(bomba, (48, 48))
   screen.blit(bomba, (inim_pos_x, inim_pos_y))
 
