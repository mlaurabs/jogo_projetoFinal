import pygame
from Player import *
from inimigos import *
from main import *
from mapa import *


# constantes
width = 32 * 30 # largura da tela
height = 32 * 20 # altura da tela

cor_barra_cheia = (0, 254, 0)
cor_barra_vazia = (255, 0, 0)

derrota = False

largura_barra = 200
altura_barra = 20
posicao_barra = [50, 20]
vida_maxima = 100

def barra_de_vida(screen):
    global estado_jogo, derrota
    vida_atual = vida_Atual()
    if vida_atual <= -1:
        estado_jogo = derrota
        draw_derrota(screen)
    else:
        pygame.draw.rect(screen, cor_barra_cheia, (posicao_barra[0], posicao_barra[1], largura_barra, altura_barra))
        largura_atual = int((vida_atual / vida_maxima) * largura_barra)
        pygame.draw.rect(screen, cor_barra_vazia, (posicao_barra[0] + largura_atual, posicao_barra[1], largura_barra - largura_atual, altura_barra))

def chaves(screen):
    qtdKeys = getQtdChaves() # pega a quantidade de chaves atualizada
    fonte = pygame.font.Font("Fonte.ttf", 36)
    texto = f"Chaves: {qtdKeys}/5"
    text = fonte.render(texto, True, (255, 192, 0))
    screen.blit(text, (720, 20))
    
def reiniciar_jogo(dt):
    
    anim_pos_x = 20 # x inicial
    anim_pos_y = 270 # y inicial
    
