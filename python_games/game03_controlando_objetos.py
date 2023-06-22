import pygame
from pygame.locals import QUIT
from sys import exit

pygame.init()


altura = 480
largura = 640
eixo_x = largura/2
eixo_y = altura/2


# DEFINIR O TAMANHO DA JANELA E O NOME DA JANELA DO JOGO
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()


# LOOP DA OCORRENCIA DO JOGO ENQUANTO ABERTO
while True:
    relogio.tick(20)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[pygame.K_a]:
        eixo_x -= 20
    if pygame.key.get_pressed()[pygame.K_d]:
        eixo_x += 20
    if pygame.key.get_pressed()[pygame.K_w]:
        eixo_y -= 20
    if pygame.key.get_pressed()[pygame.K_s]:
        eixo_y += 20

    pygame.draw.rect(tela, (255, 0, 0), (eixo_x, eixo_y, 40, 50))
    pygame.display.update()
