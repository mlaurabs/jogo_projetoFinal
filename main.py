import pygame
from config import *
from mapa import *
from Player import *
from inimigos import *
from menu import *

pygame.init()


#_________________________Variaveis__________________________#
fonte_menu = pygame.font.Font("Fonte.ttf", 40)   
                                
menu = 0
jogo = 1

opcoes_menu = ['Novo Jogo','Continuar', 'Sair']
selecionado_menu = 0
estado_jogo = menu

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

    animacao_inimigo_1()
    
def draw_screen(screen):
    global direita, esquerda, cima, baixo, sentido, frames, anim_pos_x, anim_pos_y, spt_wdt, spt_hgt, anim_frame
 
    draw_mapa(screen)
    
    draw_player(screen)
    
    draw_inimigo_1(screen)
    
    barra_de_vida(screen) # config

def draw_menu(screen):
    
    image = pygame.image.load("Fundo_Menu.png")
    image = pygame.transform.scale(image, (960, 660))
    screen.blit(image, (0, 0))
    
    
    # opções do menu
    for i, opcao in enumerate(opcoes_menu):
        cor = (255, 192, 0) if i == selecionado_menu else (255, 255, 255)
        texto_surface = fonte_menu.render(opcao, True, cor)
        texto_rect = texto_surface.get_rect(center=(width // 2, height // 3 + i * 50))
        screen.blit(texto_surface, texto_rect)

def processar_eventos_menu(eventos):
    global estado_jogo, selecionado_menu

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
                    estado_jogo = jogo
                elif selecionado_menu == 2:
                    pygame.quit()
                    exit()

def main_loop(screen):
    global clock, estado_jogo
    while True:
        eventos = pygame.event.get()
        
        if estado_jogo == menu:
            processar_eventos_menu(eventos)
            draw_menu(screen)
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


