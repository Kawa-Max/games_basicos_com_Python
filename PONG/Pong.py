from random import randint
import pygame

pygame.init()

altura = 400
largura = 600

dimensao = largura, altura
tela = pygame.display.set_mode(dimensao)
ret_tela = tela.get_rect()
pygame.display.set_caption('PONG 1.0')

tamanho_player_padrao_x = 15
tamanho_player_padrao_y = 50

velocidade_player = 15
vel_bola = 10

controle_y = 0

controle_bola_x = vel_bola
controle_bola_y = 0

bolaX = largura/2
bolaY = altura/2

p1_x = 570
p1_y = (altura / 2) - (tamanho_player_padrao_y / 2)

p2_x = 20
p2_y = (altura / 2) - (tamanho_player_padrao_y / 2)

pontos_p1 = 0
pontos_p2 = 0
fonte_padrao = pygame.font.SysFont('Times', 15, True, True)


def cores(cor=0):
    branco = 255, 255, 255
    preto = 0, 0, 0
    vermelho = 255, 0, 0
    verde = 0, 255, 0

    if cor == 1:
        return preto
    elif cor == 2:
        return branco
    elif cor == 3:
        return vermelho
    elif cor == 4:
        return verde


def linhas(tela):

    linha_do_chao = pygame.draw.line(tela, (cores(2)), (5, 393), (595, 393), 5)
    linha_do_teto = pygame.draw.line(tela, (cores(2)), (5, 7), (595, 7), 5)

    linha_do_lado_1 = pygame.draw.line(tela, (cores(2)), (5, 5), (5, 395), 5)
    linha_do_lado_2 = pygame.draw.line(tela, (cores(2)), (595, 5), (595, 395), 5)

    linha_do_meio = pygame.draw.line(tela, (cores(2)), (300, 5), (300, 395), 5)


while True:

    tela.fill(cores(1))
    pygame.time.delay(50)

    mensagem_ponto = f'Pontos JOGADOR 1: {pontos_p1}'
    texto_formatado_J1 = fonte_padrao.render(mensagem_ponto, True, (0, 155, 155))

    mensagem_ponto = f'Pontos JOGADOR 2: {pontos_p2}'
    texto_formatado_J2 = fonte_padrao.render(mensagem_ponto, True, (0, 80, 255))

    for click in pygame.event.get():

        if click.type == pygame.QUIT:
            pygame.quit()
            exit()

    bola = pygame.draw.rect(tela, cores(4), (bolaX, bolaY, 15, 15))

    player1 = pygame.draw.rect(tela, (cores(2)), (p1_x, p1_y, tamanho_player_padrao_x, tamanho_player_padrao_y))
    player2 = pygame.draw.rect(tela, (cores(2)), (p2_x, p2_y, tamanho_player_padrao_x, tamanho_player_padrao_y))

    linhas(tela)

    movendo = pygame.key.get_pressed()

    if movendo[pygame.K_UP]:
        if player1.collidepoint(570, 10):
            pass
        else:
            controle_y = -velocidade_player

            p1_y += controle_y

    elif movendo[pygame.K_DOWN]:
        if player1.collidepoint(570, 385):
            pass
        else:
            controle_y = velocidade_player

            p1_y += controle_y

    if movendo[pygame.K_w]:
        if player2.collidepoint(20, 10):
            pass

        else:
            controle_y = -velocidade_player
            p2_y += controle_y

    elif movendo[pygame.K_s]:
        if player2.collidepoint(20, 385):
            pass

        else:
            controle_y = velocidade_player
            p2_y += controle_y

    if player1.colliderect(bola):
        s = randint(1, 2)

        if s == 1:

            controle_bola_x = -vel_bola
            controle_bola_y = vel_bola

        else:
            controle_bola_x = -vel_bola
            controle_bola_y = -vel_bola

    elif player2.colliderect(bola):
        s = randint(1, 2)

        if s == 1:

            controle_bola_x = vel_bola
            controle_bola_y = -vel_bola

        else:
            controle_bola_x = vel_bola
            controle_bola_y = +vel_bola

    if bolaY == 20:
        controle_bola_y = vel_bola
        print('colidiu y 0')

    if bolaY > (altura - 30):
        controle_bola_y = -vel_bola
        print('colidiu y 400')

    if bolaX > (largura - 20):

        bolaX = largura/2
        bolaY = altura/2

        s = randint(1, 2)

        if s == 1:

            controle_bola_x = -vel_bola

        else:
            controle_bola_x = vel_bola

        pontos_p1 += 1

    if bolaX == 20:

        bolaX = largura/2
        bolaY = altura/2

        s = randint(1, 2)

        if s == 1:

            controle_bola_x = -vel_bola

        else:
            controle_bola_x = vel_bola

        pontos_p2 += 1

    bolaX += controle_bola_x
    bolaY += controle_bola_y

    tela.blit(texto_formatado_J1, (50, 40))
    tela.blit(texto_formatado_J2, (400, 40))

    pygame.display.update()

