import pygame
from Player import *
from inimigos import *
from mapa import *


# constantes
width = 32 * 30 # largura da tela
height = 32 * 20 # altura da tela

cor_barra_cheia = (0, 254, 0)
cor_barra_vazia = (255, 0, 0)

largura_barra = 200
altura_barra = 20
posicao_barra = [50, 20]
vida_maxima = 100
vida_atual = 100

def barra_de_vida(screen):
    vida_atual = getVidaAtual()
    pygame.draw.rect(screen, cor_barra_cheia, (posicao_barra[0], posicao_barra[1], largura_barra, altura_barra))
    largura_atual = int((vida_atual / vida_maxima) * largura_barra)
    pygame.draw.rect(screen, cor_barra_vazia, (posicao_barra[0] + largura_atual, posicao_barra[1], largura_barra - largura_atual, altura_barra))

    if vida_atual == -25:
        image = pygame.image.load("Objetivo.png")
        image = pygame.transform.scale(image, (960, 660))
        screen.blit(image, (0, 0))
        fonte = pygame.font.Font("Fonte.ttf", 40) 
        texto = "Voltar"
        texto_surface = fonte.render(texto, True, (255, 192, 0))
        texto_retangulo = texto_surface.get_rect(center=(width -100, height -60))
        screen.blit(texto_surface, texto_retangulo) 
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
    
