import pygame
from pygame.locals import QUIT
from sys import exit
from random import randint

pygame.init()


altura = 480
largura = 640
eixo_x_obj1 = largura/2
eixo_y_obj1 = altura/2
eixo_x_obj2 = randint(40, 600)
eixo_y_obj2 = randint(50, 430)

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
        eixo_x_obj1 -= 20
    if pygame.key.get_pressed()[pygame.K_d]:
        eixo_x_obj1 += 20
    if pygame.key.get_pressed()[pygame.K_w]:
        eixo_y_obj1 -= 20
    if pygame.key.get_pressed()[pygame.K_s]:
        eixo_y_obj1 += 20

    obj1 = pygame.draw.rect(tela, (255, 0, 0), (eixo_x_obj1, eixo_y_obj1, 40,
                                                50))
    obj2 = pygame.draw.rect(tela, (255, 255, 100), (eixo_x_obj2, eixo_y_obj2,
                                                    40, 50))
    if obj1.colliderect(obj2):
        eixo_x_obj2 = randint(40, 600)
        eixo_y_obj2 = randint(50, 430)
    pygame.display.update()
