import pygame
from sys import exit
from config import *

def variaveis_menu():
    global menu, jogo, opcoes_menu, selecionado_menu, estado_jogo, image
    menu = 0
    jogo = 1

    opcoes_menu = ['Novo Jogo','Continuar', 'Sair']
    selecionado_menu = 0
    
    estado_jogo = menu