import pygame
import random

mapa = []

interCol = [0, 5, 10, 15, 20, 25, 29]
posKeys = []

# importar sheets mapa 1
def sheets_mapa_1():
    global textura1, textura2, textura3, bau, tocha, tesouro, key, fundo
    
    textura1 = pygame.image.load("images/texture1.png") # A
    textura2 = pygame.image.load("images/textura2.png") # B
    fundo = pygame.image.load("images/fundoEscuro.png") # E
    textura3 = pygame.transform.scale(pygame.image.load("images/tijolo.png"), (32,32)) # c
    tocha = pygame.image.load("images/Tocha.png")
    tesouro = pygame.image.load("images/Tesouro.png")
    key = pygame.image.load("images/key.png")
    tesouro = pygame.transform.scale(tesouro, (80, 60))
    key = pygame.transform.scale(key, (32, 32))

# gerando o mapa 1
def escoheAleatorio(linha, coluna):
    #coluna
    coluna.append(random.randint(1, 4))
    coluna.append(random.randint(6, 9))
    coluna.append(random.randint(11, 14))
    coluna.append(random.randint(16, 19))
    coluna.append(random.randint(21, 24))
    coluna.append(random.randint(26, 28))
    #linha
    linha.append(random.randint(2, 8))
    linha.append(random.randint(15, 19))
    aux = random.randint(0, 1)
    i = linha[aux]
    aux = random.randint(0, 5)
    j = coluna[aux]
    return [i,j]

def getKey():
    return key

def mapa_1():
    
    interCol = [0, 5, 10, 15, 20, 25, 29]
    
    for i in range(20):
        linha = []
        for j in range(30):
            if(i < 2):
                linha.append('E')
            else:
                if (j % 2 == 0):
                    linha.append('A')
                elif (j % 2 != 0):
                    linha.append('B')
                if (j in interCol):
                    if (i <= 8 and i > 1):
                        linha.append('C')
                    if(i >= 15):
                        linha.append('C')

        mapa.append(linha)
    
    # outras configurações do mapa - posicionando os blocos em lugares específicos
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

    # interCol = [0, 5, 10, 15, 20, 25, 29]
    aux = [0,0]
    row = 0
    col = 0
    for x in range(5): # espalhando as chaves aleatoriamente entre os trechos escolhidos
        print(x)
        linha = []
        coluna = []
        pos = escoheAleatorio(linha, coluna)
        row = pos[0]
        col = pos[1]
        if(mapa[row][col] == "C"):
            print(f"row = {row}  col = {col}")
            while(mapa[row][col] == "C"):
                pos = escoheAleatorio(linha, coluna)
                row = pos[0]
                col = pos[1]
                if(mapa[row][col] != "C"):
                    mapa[row][col] += "K"
        else:
            mapa[row][col] += "K"
# desenha mapa na tela     
def draw_mapa(screen):
    global mapa
    
    screen.fill((255, 255, 255))
   
    for i in range(20):
        for j in range(30):
            if(mapa[i][j] == 'E'):
                screen.blit(fundo, ((j * 32), (i * 32)))
            elif (mapa[i][j] == 'A'):
                screen.blit(textura1, ((j * 32), (i * 32)))
            elif (mapa[i][j] == 'B'):
                screen.blit(textura2, ((j * 32), (i * 32)))
            elif (mapa[i][j] == 'C'):
                screen.blit(textura3, ((j * 32), (i * 32)))
            elif('K' in mapa[i][j]):
                screen.blit(textura1, ((j * 32), (i * 32)))
                screen.blit(key, ((j * 32), (i * 32)))
    screen.blit(tesouro, (850, 570))




