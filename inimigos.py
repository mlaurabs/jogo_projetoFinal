import pygame
from config import *
global frames, spt_wdt, spt_hgt, direita, esquerda, cima, anim_frame, anim_time, anim_pos_x, anim_pos_y,screen

anim_pos_x = 200 # x inicial
anim_pos_y = 400 # y inicial

# importa textura personagem

def sheets_inimigo_1():
    global frames, spt_wdt, spt_hgt, direita, esquerda, cima, anim_frame, anim_time, anim_pos_x, anim_pos_y, screen
    # animacao 
    direita = []  # vetor de imagens - sentido direita
    esquerda = []  # vetor de imagens - sentido esquerda
    cima = []  # vetor de imagens - sentido cima
    baixo = []  # vetor de imagens - baixo
    anim_frame = 1
    anim_time = 0  # variavel para controle do tempo da animação

    #anim_pos_x()
    #anim_pos_y()
    
    frames = pygame.draw.rect(screen,('red'), (anim_pos_x, anim_pos_y, 100, 100))
    spt_wdt = frames.get_width()
    spt_hgt = frames.get_height()

# logica da movimentacao
def inimigoColisao(): # modificar
    inimigo = pygame.Rect(anim_pos_x, anim_pos_y, 100, 100)
    return inimigo

def animacao_inimigo_1():
    global direita, esquerda, cima, baixo, sentido, frames, anim_pos_x, anim_pos_y, spt_wdt, spt_hgt, anim_frame, anim_time, old_x, old_y, dt

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

   
   pygame.draw.rect(screen, (255, 0, 0), (anim_pos_x, anim_pos_y, 50, 50))
 
