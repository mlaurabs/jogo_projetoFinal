import pygame

mapa = []

interCol = [0, 5, 10, 15, 20, 25, 29]

# importar sheets mapa 1
def sheets_mapa_1():
    global textura1, textura2, textura3, bau, tocha, tesouro, key
    
    textura1 = pygame.image.load("images/texture1.png") # A
    textura2 = pygame.image.load("images/textura2.png") # B
    textura3 = pygame.transform.scale(pygame.image.load("images/tijolo.png"), (32,32)) # c
    bau = pygame.image.load("images/bauDaMorte.png")
    tocha = pygame.image.load("images/foguinho.png")
    tesouro = pygame.image.load("images/tesouroFinal.png")
    key = pygame.image.load("images/key.png")
    key = pygame.transform.scale(key, (32, 32))

# gerando o mapa 1

def getKey():
    return key

def mapa_1():
    
    interCol = [0, 5, 10, 15, 20, 25, 29]
    
    for i in range(20):
        linha = []
        for j in range(30):
            if (j % 2 == 0):
                linha.append('A')
            elif (j % 2 != 0):
                linha.append('B')
            if (j in interCol):
                if (i <= 5 or i >= 15 ):
                    linha.append('C')

        mapa.append(linha)
    
    # outras configurações do mapa
    mapa[5][2] = 'C'
    mapa[5][3] = 'C'
    mapa[6][3] = 'C'
    mapa[7][3] = 'C'
    mapa[7][4] = 'C'

    mapa[15][2] = 'C'
    mapa[15][3] = 'C'
    mapa[16][3] = 'C'

    mapa[5][14] = 'C'
    mapa[5][12] = 'C'
    mapa[5][11] = 'C'
    mapa[5][10] = 'C'
    mapa[4][10] = 'C'
    mapa[3][10] = 'C'

    mapa[15][20] = 'C'
    mapa[15][21] = 'C'
    mapa[14][21] = 'C'
    mapa[13][21] = 'C'
    mapa[13][22] = 'C'

    mapa[2][5] += "K"
    
# desenha mapa na tela     
def draw_mapa(screen):
    global mapa
    
    screen.fill((255, 255, 255))
   
    for i in range(20):
        for j in range(30):
            if (mapa[i][j] == 'A'):
                screen.blit(textura1, ((j * 32), (i * 32)))
            elif (mapa[i][j] == 'B'):
                screen.blit(textura2, ((j * 32), (i * 32)))
            elif (mapa[i][j] == 'C'):
                screen.blit(textura3, ((j * 32), (i * 32)))
            elif('K' in mapa[i][j]):
                screen.blit(textura1, ((j * 32), (i * 32)))
                screen.blit(key, ((j * 32), (i * 32)))

    screen.blit(tesouro, (850, 220))

    


