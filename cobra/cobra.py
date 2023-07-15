from time import sleep
import pygame
from sys import exit
from pygame.locals import *
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.3)
musica = pygame.mixer.music.load('cat.mp3')
pygame.mixer.music.play(-1)
colisao = pygame.mixer.Sound('smw_coin.wav')

largura = int(640)
altura = int(480)

lista_cobra = list()
comprimento_inicial = 5

x_cobra = largura / 2
y_cobra = altura / 2


velocidade = 8
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(40, 430)

pontos = 0

fonte = pygame.font.SysFont('arial', 40, True, True)

morreu = False



tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('meu jogo')
relogio = pygame.time.Clock()

def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:
        # xey = list() [x, y]
        # xey[0] = x
        # xey[1] = y
        pygame.draw.rect(tela, (0, 255, 0), (xey[0], xey[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura / 2
    y_cobra = altura / 2
    lista_cobra = list()
    lista_cabeca = list()
    x_maca = randint(40, 600)
    y_maca = randint(40, 430)
    morreu = False
    



while True:
    relogio.tick(40)
    tela.fill((255, 255, 255))
    mensagem = f'maças: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle


    if pygame.key.get_pressed()[K_p]:
        pygame.quit()
        exit()

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))


    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(40, 430)
        pontos += 1
        colisao.play()
        comprimento_inicial += 1

    lista_cabeca = list()
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)
    
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        msg = 'gamer over ! pressione a tecla "r" para jogar novamente!!'
        textof = fonte2.render(msg, True, (0, 0, 0))
        ret_texto = textof.get_rect()
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            if pygame.key.get_pressed()[K_p]:
                pygame.quit()
                exit()
            
            
            ret_texto.center = (largura // 2, altura // 2)
            tela.blit(textof, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0
    
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    
    tela.blit(texto_formatado, (400, 20))
    
    pygame.display.update()

