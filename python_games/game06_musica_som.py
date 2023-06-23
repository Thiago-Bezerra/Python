import pygame
from pygame.locals import QUIT
from sys import exit
from random import randint

pygame.init()


pygame.mixer_music.set_volume(0.1)
musica_de_fundo = pygame.mixer_music.load('cpu_talk.mp3')
pygame.mixer_music.play(-1)
barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
# barulho_colisao.set_volume()
altura = 480
largura = 640
eixo_x_obj1 = largura/2
eixo_y_obj1 = altura/2
eixo_x_obj2 = randint(40, 600)
eixo_y_obj2 = randint(50, 430)

pontos = 0
# estil de fonte: tipo da fonte, tamanho da fonte, fonte em negrito e
# texto serrilhando
fonte = pygame.font.SysFont('arial', 40, True, False)


# DEFINIR O TAMANHO DA JANELA E O NOME DA JANELA DO JOGO
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()


# LOOP DA OCORRENCIA DO JOGO ENQUANTO ABERTO
while True:
    relogio.tick(20)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
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
        pontos += 1
        barulho_colisao.play()
    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()
