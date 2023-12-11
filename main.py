import pygame
from configuration import conta_chave, barra_de_vida, reiniciar_jogo
from mapa import *
from Player import *
from inimigos import *
from menu import *

pygame.init()

# a 
#_________________________Variaveis__________________________#
fonte_menu = pygame.font.Font("Fonte.ttf", 40)   
                                
menu = 0
jogo = 1
objetivo = 2
derrota = 3
vitoria = 4

width = 32 * 30 # largura da tela
height = 32 * 20 # altura da tela

opcoes_menu = ['Novo Jogo', 'Objetivo', 'Sair']

selecionado_menu = 0

estado_jogo = menu
selecionado = 0

anim_pos_x = 20 # x inicial
anim_pos_y = 500 # y inicial
#__________________________________________________________#


def load():
    global clock, mapa, texture1, texture2, texture3, bau, tocha, tesouro, key, direita, esquerda, cima, baixo, sentido, frames, spt_wdt, spt_hgt, jogador_rect, interCol  
    
  # frame por segundo
    clock = pygame.time.Clock()
    
    sheets_player()
    sheets_mapa_1()
    
    mapa_1()
        
def update(dt):
    global old_x, old_y, direita, esquerda, cima, baixo, sentido, frames, anim_pos_x, anim_pos_y, spt_wdt, spt_hgt, anim_frame, anim_time
    
    old_x = anim_pos_x
    old_y = anim_pos_y
    
    # animacao personagem principal  + colisão      
    animacao_player(dt)

    animacao_inimigo(dt)
    
def get_estado_jogo():
    return estado_jogo

def draw_screen(screen):
    global direita, esquerda, cima, baixo, sentido, frames, anim_pos_x, anim_pos_y, spt_wdt, spt_hgt, anim_frame
 
    draw_mapa(screen)
    draw_player(screen)
    draw_inimigo_1(screen)
    barra_de_vida(screen) # config
    conta_chave(screen)
    
def draw_objetivo(screen):
    image = pygame.image.load("Objetivo.png")
    image = pygame.transform.scale(image, (960, 660))
    screen.blit(image, (0, 0))
    fonte = pygame.font.Font("Fonte.ttf", 40) 
    texto = "Voltar"
    texto_surface = fonte.render(texto, True, (255, 192, 0))
    texto_retangulo = texto_surface.get_rect(center=(width -100, height -60))
    screen.blit(texto_surface, texto_retangulo) 

def processar_eventos_obj(eventos):
    global selecionado, estado_jogo, menu
    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            if selecionado == 0:
                estado_jogo = menu
                draw_menu(screen)

def draw_vitoria(screen):

    image = pygame.image.load("Ganhou.png")
    image = pygame.transform.scale(image, (960, 660))
    screen.blit(image, (0, 0))
    fonte = pygame.font.Font("Fonte.ttf", 30) 
    texto = "Ir para o menu"
    texto_surface = fonte.render(texto, True, (255, 255, 255))
    texto_retangulo = texto_surface.get_rect(center=(width -100, height -60))
    screen.blit(texto_surface, texto_retangulo) 

def processar_eventos_vit(eventos):
    global selecionado, estado_jogo, menu
    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            if selecionado == 0:
                estado_jogo = menu
                draw_menu(screen)

def draw_derrota(screen):

    image = pygame.image.load("Game_Over.png")
    image = pygame.transform.scale(image, (960, 660))
    screen.blit(image, (0, 0))
    fonte = pygame.font.Font("Fonte.ttf", 30) 
    texto = "Ir para o menu"
    texto_surface = fonte.render(texto, True, (255, 255, 255))
    texto_retangulo = texto_surface.get_rect(center=(width -800, height -60))
    screen.blit(texto_surface, texto_retangulo) 

def processar_eventos_der(eventos):
    global selecionado, estado_jogo, menu
    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            if selecionado == 0:
                estado_jogo = menu
                draw_menu(screen)
                    
def draw_menu(screen):
    
    image = pygame.image.load("Fundo_Menu.png")
    image = pygame.transform.scale(image, (960, 660))
    screen.blit(image, (0, 0))
    # opções do menu
    for i, opcao in enumerate(opcoes_menu):
        cor = (255, 192, 0) if i == selecionado_menu else (255, 255, 255)
        texto_surface = fonte_menu.render(opcao, True, cor)
        texto_rect = texto_surface.get_rect(center=(width // 2, height // 2.5 + i * 50))
        screen.blit(texto_surface, texto_rect)
    
def processar_eventos_menu(eventos):
    global estado_jogo, selecionado_menu, objetivo
    variaveis_menu()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                selecionado_menu = (selecionado_menu - 1) % len(opcoes_menu)
            elif evento.key == pygame.K_DOWN:
                selecionado_menu = (selecionado_menu + 1) % len(opcoes_menu)
            elif evento.key == pygame.K_RETURN:
                if selecionado_menu == 0:
                    estado_jogo = jogo
                elif selecionado_menu == 1:
                    estado_jogo = objetivo
                    draw_objetivo(screen)
                elif selecionado_menu == 2:
                    print("NOVO JOGO")
                    pygame.quit()
                    exit()

def main_loop(screen):
    global clock, estado_jogo
    
    while True:
        eventos = pygame.event.get()
        if estado_jogo == menu:
            processar_eventos_menu(eventos)
            draw_menu(screen)
        elif estado_jogo == objetivo:
            processar_eventos_obj(eventos)
            draw_objetivo(screen)
        elif estado_jogo == derrota:
            processar_eventos_der(eventos)
            draw_derrota(screen)
        elif estado_jogo == vitoria:
            processar_eventos_vit(eventos)
            draw_vitoria(screen)
        elif estado_jogo == jogo:
            for evento in eventos:
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    estado_jogo = menu

            # Restante da lógica do jogo aqui
            update(clock.get_time())
            
            draw_screen(screen)

        pygame.display.update()
        clock.tick(60)
        
pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()


