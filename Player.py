import pygame
from mapa import *
from inimigos import inimigoColisao

# animacao 
direita = []  # vetor de imagens - sentido direita
esquerda = []  # vetor de imagens - sentido esquerda
cima = []  # vetor de imagens - sentido cima
baixo = []  # vetor de imagens - baixo
anim_frame = 1
anim_time = 0  # variavel para controle do tempo da animação

anim_pos_x = 20 # x inicial
anim_pos_y = 270 # y inicial

sentido = "r"

# importa textura personagem
def sheets_player():
    global frames, spt_wdt, spt_hgt, direita, esquerda, cima, anim_frame, anim_time, anim_pos_x, anim_pos_y
    
    frames = pygame.image.load("images/joagador.png")
    spt_wdt = frames.get_width() / 4  # Largura de um sprite
    spt_hgt = frames.get_height() / 4  # Altura de um sprite
    
    # carrega as imagens da animação
    i = 3  # sentido para direita
    for j in range(4):
        tupla = (j * spt_wdt, i * spt_hgt)
        cima.append(tupla)
    print(cima)

    i = 2  # sentido para esquerda
    for j in range(4):
        tupla = (j * spt_wdt, i * spt_hgt)
        direita.append(tupla)
    print(direita)

    i = 1  # sentido para cima
    for j in range(4):
        tupla = (j * spt_wdt, i * spt_hgt)
        esquerda.append(tupla)
    print(esquerda)

    i = 0  # sentido para baixo
    for j in range(4):
        tupla = (j * spt_wdt, i * spt_hgt)
        baixo.append(tupla)
    print(baixo)

# logica da movimentacao + colisoes 
def animacao_player(dt):
    global direita, esquerda, cima, baixo, sentido, frames, anim_pos_x, anim_pos_y, spt_wdt, spt_hgt, anim_frame, anim_time, old_x, old_y
    
    old_x = anim_pos_x
    old_y = anim_pos_y

    # movimentos do personagem
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        sentido = "r"
        if (anim_pos_x > 910):  # não deixa passar da borda
            anim_pos_x = 905
        anim_pos_x = anim_pos_x + (0.1 * dt)  # movimenta o personagem
        anim_time = anim_time + dt  # incrementa o tempo usando dt
        if anim_time > 100:  # quando acumular mais de 100 ms
            anim_frame += 1  # avança para proximo frame
            if anim_frame > 3:  # loop da animação
                anim_frame = 0
            anim_time = 0  # reinicializa a contagem do tempo
    if keys[pygame.K_LEFT]:
        sentido = "l"
        if (anim_pos_x < 1):  # não deixa passar da borda
            anim_pos_x = 2
        anim_pos_x = anim_pos_x - (0.1 * dt)
        anim_time = anim_time + dt
        if anim_time > 100:
            anim_frame += 1
            if anim_frame > 3:
                anim_frame = 0
            anim_time = 0
    if keys[pygame.K_UP]:
        sentido = "u"
        if (anim_pos_y < 1):
            anim_pos_y = 2
        anim_pos_y = anim_pos_y - (0.1 * dt)
        anim_time = anim_time + dt
        if anim_time > 100:
            anim_frame += 1
            if anim_frame > 3:
                anim_frame = 0
            anim_time = 0
    if keys[pygame.K_DOWN]:
        sentido = "d"
        if (anim_pos_y > 580):
            anim_pos_y = 575
        anim_pos_y = anim_pos_y + (0.1 * dt)
        anim_time = anim_time + dt
        if anim_time > 100:
            anim_frame += 1
            if anim_frame > 3:
                anim_frame = 0
            anim_time = 0
        
    jogador_rect = pygame.Rect(anim_pos_x, anim_pos_y, spt_wdt, spt_hgt)
    jogador_rect = jogador_rect.inflate(-25, -20)
    textura3 = pygame.transform.scale(pygame.image.load("images/tijolo.png"), (22,22)) # c
    key = getKey()

    # verifica se o jogador está em contato com qualquer bloquinho "C"
    for i in range(20):
        for j in range(30):
            if (mapa[i][j] == 'C'):
                if jogador_rect.colliderect(textura3.get_rect(topleft=(j * 32, i * 32))):
                    anim_pos_x = old_x
                    anim_pos_y = old_y

    #inimigo = inimigoColisao() # modificar
    #inimigo = inimigo.inflate(-25, -20)
    # if collider_jogador.colliderect(collider_mapa):
    #if(pygame.Rect.colliderect(jogador_rect, inimigo)):
        #print("ola")
   
    # verifica se o jogador está em contato com a chave   
    for i in range(20):
        for j in range(30):
            if ('K' in mapa[i][j]):
                key_collide = key.get_rect(topleft=(j*32, i*32))
                if jogador_rect.colliderect(key_collide.inflate(-25, -20)):
                    print("encostei na chave")
                    #aumenta na contagem de chaves



# desenha o personagem animado na tela
def draw_player(screen):
    
    if (sentido == "r"):  # direita
        aux = direita[anim_frame]
        screen.blit(frames, (anim_pos_x, anim_pos_y),
                    (aux[0], aux[1], spt_wdt, spt_hgt))
    elif (sentido == "l"):  # esquerda
        aux = esquerda[anim_frame]
        screen.blit(frames, (anim_pos_x, anim_pos_y),
                    (aux[0], aux[1], spt_wdt, spt_hgt))
    elif (sentido == "u"):  # cima
        aux = cima[anim_frame]
        screen.blit(frames, (anim_pos_x, anim_pos_y),
                    (aux[0], aux[1], spt_wdt, spt_hgt))
    elif (sentido == "d"):  # baixo
        aux = baixo[anim_frame]
        screen.blit(frames, (anim_pos_x, anim_pos_y),
                    (aux[0], aux[1], spt_wdt, spt_hgt))