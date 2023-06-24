import pygame
from pygame.locals import *
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
eixo_x_cobra = largura/2
eixo_y_cobra = altura/2

velocidade = 10
x_cotrole = 20
y_cotrole = 0

eixo_x_rato = randint(40, 600)
eixo_y_rato = randint(50, 430)

pontos = 0
# estil de fonte: tipo da fonte, tamanho da fonte, fonte em negrito e
# texto serrilhando
fonte = pygame.font.SysFont('arial', 40, True, False)


# DEFINIR O TAMANHO DA JANELA E O NOME DA JANELA DO JOGO
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

lista_cobra = []
comprimento_inicial = 4


def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (xey[0], xey[1], 20, 20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, eixo_x_cobra, eixo_y_cobra, lista_cobra, lista_cabeca_cobra, eixo_x_rato, eixo_y_rato, morreu
    pontos = 0
    comprimento_inicial = 4
    eixo_x_cobra = largura/2
    eixo_y_cobra = altura/2
    lista_cobra = []
    lista_cabeca_cobra = []
    eixo_x_rato = randint(40, 600)
    eixo_y_rato = randint(50, 430)
    morreu = False

# LOOP DA OCORRENCIA DO JOGO ENQUANTO ABERTO
while True:
    relogio.tick(20)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_cotrole == velocidade:
                    pass
                else:
                    x_cotrole = -velocidade
                    y_cotrole = 0
            if event.key == K_d:
                if x_cotrole == -velocidade:
                    pass
                else:
                    x_cotrole = velocidade
                    y_cotrole = 0
            if event.key == K_w:
                if y_cotrole == velocidade:
                    pass
                else:
                    x_cotrole = 0
                    y_cotrole = -velocidade
            if event.key == K_s:
                if y_cotrole == -velocidade:
                    pass
                else:
                    x_cotrole = 0
                    y_cotrole = velocidade
    eixo_x_cobra += x_cotrole
    eixo_y_cobra += y_cotrole
    '''
    if pygame.key.get_pressed()[pygame.K_a]:
        eixo_x_cobra -= 20
    if pygame.key.get_pressed()[pygame.K_d]:
        eixo_x_cobra += 20
    if pygame.key.get_pressed()[pygame.K_w]:
        eixo_y_cobra -= 20
    if pygame.key.get_pressed()[pygame.K_s]:
        eixo_y_cobra += 20
'''

    cobra = pygame.draw.rect(tela, (0, 255, 0), (eixo_x_cobra, eixo_y_cobra, 20, 20))
    rato = pygame.draw.rect(tela, (255, 0, 0), (eixo_x_rato, eixo_y_rato, 20, 20))
    if cobra.colliderect(rato):
        eixo_x_rato = randint(40, 600)
        eixo_y_rato = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial += 1
    lista_cabeca_cobra = []
    lista_cabeca_cobra.append(eixo_x_cobra)
    lista_cabeca_cobra.append(eixo_y_cobra)

    lista_cobra.append(lista_cabeca_cobra)
    if lista_cobra.count(lista_cabeca_cobra) > 1:
        fonte_over = pygame.font.SysFont('arial', 20, bold=True, italic=True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte_over.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()
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
            
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()


    if eixo_x_cobra > largura:
        eixo_x_cobra = 0
    if eixo_x_cobra < 0:
        eixo_x_cobra = largura
    if eixo_y_cobra > altura:
        eixo_y_cobra = 0
    if eixo_y_cobra < 0:
        eixo_y_cobra = altura
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()
