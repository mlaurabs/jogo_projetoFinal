import pygame
from sys import exit
from config import *

def variaveis_menu():
    global menu, jogo, opcoes_menu, selecionado_menu, estado_jogo, objetivo
    menu = 0
    objetivo = 1
    jogo = 2
    opcoes_menu = ['Novo Jogo','Objetivo', 'Sair']
    selecionado_menu = 0
    estado_jogo = menu