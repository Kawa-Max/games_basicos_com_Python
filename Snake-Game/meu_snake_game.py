import pygame
from random import randint
from sys import exit

# ---------------------- COMANDOS BASICOS DO PYGAME PARA OS AUDIOS -------------------------------------------------

pygame.init()

pygame.mixer.init()

pygame.mixer.music.set_volume(0.2)  # AJUSTAR VOLUME DO AUDIO DE FUNDO
pygame.mixer.music.load('audios/fundo.mp3')
pygame.mixer.music.play(-1)

colision = pygame.mixer.Sound('audios/barulho_colisao.wav')
game_over = pygame.mixer.Sound('audios/Game_Over_.mp3')
game_over.set_volume(0.5)  # AJUSTAR VOLUME DO GAME-OVER

# ---------------------- CONFIGURACÕES BASICAS DA TELA E VELOCIDADES(ETC) ---------------------------------------

largura_da_tela = 800
altura_da_tela = 700

pos_x_maca = randint(50, 750)
pos_y_maca = randint(50, 650)

posicao_cobra_x = int(largura_da_tela / 2)
posicao_cobra_y = int(altura_da_tela / 2)

velocidade = 10

controle_x = velocidade
controle_y = 0

display = pygame.display.set_mode((largura_da_tela, altura_da_tela))  # CRIA UMA TELA EXECULTAVEL
pygame.display.set_caption('Meu Game')  # DA UM NOME A TELA

texto_fonte_padrao = pygame.font.SysFont('arial', 32, True)

pontos = 0

corpo_cobra = []
tamanho_cobra = 1

morreu = False


# ---------------------- FUNÇÃO DE REINICIAR O JOGO -------------------------------------------------
def reiniciar_jogo():
    global tamanho_cobra, posicao_cobra_x, posicao_cobra_y, corpo_cobra, cabeca_da_cobra, pos_x_maca, pos_y_maca
    global morreu, pontos, velocidade

    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.load('audios/fundo.mp3')
    pygame.mixer.music.play(-1)

    game_over.stop()

    pontos = 0
    tamanho_cobra = 1
    velocidade = 10
    posicao_cobra_x = int(largura_da_tela / 2)
    posicao_cobra_y = int(altura_da_tela / 2)
    corpo_cobra = []
    cabeca_da_cobra = []
    pos_x_maca = randint(30, 600)
    pos_y_maca = randint(30, 460)
    morreu = False


# ---------------------- FUNÇÃO DE CRESCER A COBRA -------------------------------------------------
def aumentando_a_cobra(corpo):
    for posXeY in corpo:
        pygame.draw.rect(display, (255, 255, 0), (posXeY[0], posXeY[1], 40, 40))


# ---------------------- LOOP PRINCIPAL DO JOGO -------------------------------------------------

while True:

    pygame.time.delay(50)
    display.fill((198, 236, 182))

    # ---------------------- TEXTO DE PONTOS -------------------------------------------------

    txt_ponto = f'Pontos: {pontos}'
    formato_ponto = texto_fonte_padrao.render(txt_ponto, False, (0, 0, 0))

    # ------------------------ EVENTOS E MOVIMENTOS COM MAS TECLAS--------------------------------------------

    for evento in pygame.event.get():

        sair = pygame.key.get_pressed()

        if evento.type == pygame.QUIT or sair[pygame.K_0]:
            pygame.quit()
            exit()

    mover = pygame.key.get_pressed()

    if mover[pygame.K_UP] or mover[pygame.K_w]:

        if controle_y == velocidade:
            pass

        else:
            controle_y = -velocidade
            controle_x = 0

    elif mover[pygame.K_DOWN] or mover[pygame.K_s]:

        if controle_y == -velocidade:
            pass

        else:
            controle_y = velocidade
            controle_x = 0

    elif mover[pygame.K_LEFT] or mover[pygame.K_a]:

        if controle_x == velocidade:
            pass

        else:
            controle_x = -velocidade
            controle_y = 0

    elif mover[pygame.K_RIGHT] or mover[pygame.K_d]:

        if controle_x == -velocidade:
            pass

        else:
            controle_x = velocidade
            controle_y = 0

    posicao_cobra_x += controle_x
    posicao_cobra_y += controle_y

    # -------------------------- OBJETOS DA TELA -------------------------------------------

    cobra = pygame.draw.rect(display, (255, 255, 0), (posicao_cobra_x, posicao_cobra_y, 40, 40))
    maca = pygame.draw.rect(display, (255, 0, 0), (pos_x_maca, pos_y_maca, 25, 25))

    chao = pygame.draw.rect(display, (150, 75, 0), (0, 680, 800, 20))
    teto = pygame.draw.rect(display, (150, 75, 0), (0, 0, 800, 20))
    lado1 = pygame.draw.rect(display, (150, 75, 0), (0, 10, 20, 680))
    lado2 = pygame.draw.rect(display, (150, 75, 0), (780, 10, 20, 680))

    linha_chao = pygame.draw.line(display, (0, 145, 0), (11, 680), (789, 680), 20)
    linha_teto = pygame.draw.line(display, (0, 145, 0), (11, 17), (791, 17), 20)

    linha_lado_1 = pygame.draw.line(display, (0, 145, 0), (20, 15), (20, 685), 20)
    linha_lado_2 = pygame.draw.line(display, (0, 145, 0), (781, 20), (781, 690), 20)

    barra_1 = pygame.draw.rect(display, (0, 145, 0), (210, 190, 20, 200))
    barra_2 = pygame.draw.rect(display, (0, 145, 0), (590, 190, 20, 200))
    barra_3 = pygame.draw.rect(display, (0, 145, 0), (655, 490, 20, 200))
    barra_4 = pygame.draw.rect(display, (0, 145, 0), (155, 490, 20, 200))

    # ------------------------- COLISÃO COM A MAÇA ------------------------------------------------

    if cobra.colliderect(maca):
        colision.play()
        pontos += 10
        tamanho_cobra += 1

        pos_x_maca = randint(50, 750)
        pos_y_maca = randint(50, 650)

    # ------------------------- GERANDO O CORPO DA COBRA ------------------------------------------------

    cabeca_da_cobra = [posicao_cobra_x, posicao_cobra_y]
    corpo_cobra.append(cabeca_da_cobra)

    aumentando_a_cobra(corpo_cobra)

    # ------------------------- COLISÃO COM OBSTACULOS E O CORPO DA COBRA ---------------------------------------------

    if cobra.colliderect(chao) or cobra.colliderect(teto) or cobra.colliderect(lado1) or cobra.colliderect(lado2) or \
            cobra.colliderect(barra_1) or cobra.colliderect(barra_2) or cobra.colliderect(barra_3) or \
            cobra.colliderect(barra_4) or corpo_cobra.count(cabeca_da_cobra) > 1:

        #   ----------------------------- CONF. DE TELA APÓS COLISÃO---------------------------------------------

        pygame.mixer.music.unload()

        game_over.play()

        if velocidade > 10:
            velocidade = 10

        morreu = True

        fonte_tela_morreu = pygame.font.SysFont('arial', 25, True, True)
        fonte_tela_sair = pygame.font.SysFont('arial', 15, True, True)

        mensagem_morreu = "GAME OVER. PRESSIONE 'R' PARA REINICIAR O GAME"
        mensagem_sair = "Para sair, clique no dígito '0'"

        texto_formatado_morreu = fonte_tela_morreu.render(mensagem_morreu, False, (255, 0, 0))

        texto_formatado_sair = fonte_tela_sair.render(mensagem_sair, True, (128, 128, 128))

        tamanho_texto_morreu = texto_formatado_morreu.get_rect()
        tamanho_texto_sair = texto_formatado_sair.get_rect()

        # ----------------------------- LOOP TELA REINICIAR GAME ---------------------------------------------

        while morreu:

            display.fill((0, 0, 255))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                opc_jogador = pygame.key.get_pressed()

                if opc_jogador[pygame.K_r]:
                    reiniciar_jogo()

                if opc_jogador[pygame.K_0]:
                    pygame.quit()
                    exit()

            tamanho_texto_morreu.center = (largura_da_tela // 2, altura_da_tela // 2)
            display.blit(texto_formatado_morreu, tamanho_texto_morreu)

            tamanho_texto_sair.center = (largura_da_tela // 2 + 40, altura_da_tela // 2 + 40)
            display.blit(texto_formatado_sair, tamanho_texto_sair)

            pygame.display.update()

    # -----------------------------COLISÃO MAÇA COM OS OBSTACULOS---------------------------------------------

    if maca.colliderect(barra_1) or maca.colliderect(barra_2) or maca.colliderect(barra_3) or \
            maca.colliderect(barra_4):
        pos_x_maca = randint(50, 750)
        pos_y_maca = randint(50, 650)

    if len(corpo_cobra) > tamanho_cobra:
        del corpo_cobra[0]

    display.blit(formato_ponto, (30, 40))
    pygame.display.update()
