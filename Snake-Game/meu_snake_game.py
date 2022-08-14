import pygame
from sys import exit

pygame.init()

pygame.mixer.init()

largura_da_tela = 800
altura_da_tela = 700

velocidade = 10

posicao_cobra_x = int(largura_da_tela / 2)
posicao_cobra_y = int(altura_da_tela / 2)

controle_x = velocidade
controle_y = 0

display = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption('Meu Game')

texto_fonte_padrao = pygame.font.SysFont('arial', 32, True)

while True:

    pygame.time.delay(50)
    display.fill((255, 255, 255))

    for evento in pygame.event.get():

        sair = pygame.key.get_pressed()

        if evento.type == pygame.QUIT or sair[pygame.K_0]:
            pygame.quit()
            exit()

    mover = pygame.key.get_pressed()

    if mover[pygame.K_UP]:

        if controle_y == velocidade:
            pass

        else:
            controle_y = -velocidade
            controle_x = 0

    elif mover[pygame.K_DOWN]:

        if controle_y == -velocidade:
            pass

        else:
            controle_y = velocidade
            controle_x = 0

    elif mover[pygame.K_LEFT]:

        if controle_x == velocidade:
            pass

        else:
            controle_x = -velocidade
            controle_y = 0

    elif mover[pygame.K_RIGHT]:

        if controle_x == -velocidade:
            pass

        else:
            controle_x = velocidade
            controle_y = 0

    posicao_cobra_x += controle_x
    posicao_cobra_y += controle_y

    cobra = pygame.draw.rect(display, (255, 130, 40), (posicao_cobra_x, posicao_cobra_y, 30, 30))
    chao = pygame.draw.rect(display, (150, 75, 0), (0, 680, 800, 20))
    teto = pygame.draw.rect(display, (150, 75, 0), (0, 0, 800, 20))
    lado1 = pygame.draw.rect(display, (150, 75, 0), (0, 10, 20, 680))
    lado2 = pygame.draw.rect(display, (150, 75, 0), (780, 10, 20, 680))

    linha_chao = pygame.draw.line(display, (170, 150, 0), (11, 680), (789, 680), 20)
    linha_teto = pygame.draw.line(display, (170, 150, 0), (11, 17), (791, 17), 20)

    linha_lado_1 = pygame.draw.line(display, (170, 150, 0), (20, 15), (20, 685), 20)
    linha_lado_2 = pygame.draw.line(display, (170, 150, 0), (781, 20), (781, 690), 20)

    if cobra.colliderect(chao) or cobra.colliderect(teto) or cobra.colliderect(lado1) or cobra.colliderect(lado2):
        break

    pygame.display.update()

