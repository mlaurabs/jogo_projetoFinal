import pygame
from config import *

anim_pos_x = 500 # x inicial
anim_pos_y = 225 # y inicial

# importa textura personagem
def sheets_inimigo_1():
    global frames, spt_wdt, spt_hgt, direita, esquerda, cima, anim_frame, anim_time, anim_pos_x, anim_pos_y,screen
    
    # animacao 
    direita = []  # vetor de imagens - sentido direita
    esquerda = []  # vetor de imagens - sentido esquerda
    cima = []  # vetor de imagens - sentido cima
    baixo = []  # vetor de imagens - baixo
    anim_frame = 1
    anim_time = 0  # variavel para controle do tempo da animação

    anim_pos_x()
    anim_pos_y()
    
    frames = pygame.draw.rect(screen,('red'), (100, 100), (100,100))
   

# logica da movimentacao    
def animacao_inimigo_1():
    global direita, esquerda, cima, baixo, sentido, frames, anim_pos_x, anim_pos_y, spt_wdt, spt_hgt, anim_frame, anim_time, old_x, old_y, dt




# logia da colisao

                  
# desenha o personagem animado na tela                    
def draw_inimigo_1(screen):

   
   pygame.draw.rect(screen, (255, 0, 0), (anim_pos_x, anim_pos_y, 50, 50))
 
