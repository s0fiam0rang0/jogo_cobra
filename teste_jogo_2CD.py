import pygame 
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Teste 2CD')

velocidade = 10
x_controle = velocidade
y_controle = 0

x_cobra = int(largura/2)
y_cobra = int(altura/2)
x_maca = randint(40, 600)
y_maca = randint(50, 430)
lista_cobra = []
comprimento_inicial = 5

pontos = 0

fonte_1 = pygame.font.SysFont('Comic Sans', 40, True, False)

som_colisao = pygame.mixer.Sound('smw_kick.wav')
som_colisao.set_volume(1)

tempo = pygame.time.Clock()

def comprimento_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 40, 40))


while True:
    tempo.tick(30)
    tela.fill((110,0,150))
    mensagem = f'Pontos:{pontos}'
    texto = fonte_1.render(mensagem, True, (255,255,255))
    

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

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra, 40, 40))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, 40, 40))

    if cobra.colliderect(maca):
        pontos = pontos + 1
        comprimento_inicial = comprimento_inicial + 1
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        som_colisao.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
       del lista_cobra[0]

    comprimento_cobra(lista_cobra)

    tela.blit(texto, (30, 20))
    
    pygame.display.update() 