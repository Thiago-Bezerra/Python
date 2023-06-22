import pygame
from pygame.locals import QUIT
from sys import exit

pygame.init()


altura = 480
largura = 640

# DEFINIR O TAMANHO DA JANELA E O NOME DA JANELA DO JOGO
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")

# LOOP DA OCORRENCIA DO JOGO ENQUANTO ABERTO
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
