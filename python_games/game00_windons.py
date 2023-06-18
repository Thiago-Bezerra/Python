import pygame
from pygame.locals import QUIT
from sys import exit

pygame.init()


altura = 480
largura = 640


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
