# Importando as bibliotecas que irei usar
import pygame
import os
import random
import neat

#  Dimensões da tela
largura = 500
altura = 700

#  Fonte & COR
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 40)
BRANCO = (255, 255, 255)

#  Imagens
IMAGEM_cano = pygame.transform.scale2x(pygame.image.load(os.path.join('img_ia', 'pipe.png')))
IMAGEM_chao = pygame.transform.scale2x(pygame.image.load(os.path.join('img_ia', 'base.png')))
IMAGEM_background = pygame.transform.scale2x(pygame.image.load(os.path.join('img_ia', 'bg.png')))
IMAGENS_bird = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('img_ia', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('img_ia', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('img_ia', 'bird3.png'))),
]
# IA
ia_jogando = True
geracao = 0


#  Objetos do game: Cano, chão e Pássaro
class Passaro:
    IMGS = IMAGENS_bird

    # animação da rotação
    rotacao_max = 25
    vel_rotacao = 20
    tempo_animacao = 5

    # Bird
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.vel = 0
        self.altura = self.y
        self.tempo = 0
        self.cont_imagem = 0
        self.imagem = self.IMGS[0]

    def pular(self):
        self.vel = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):

        # Calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo ** 2) + self.vel * self.tempo

        # Restringir o Deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # O angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.rotacao_max:
                self.angulo = self.rotacao_max

        else:
            if self.angulo > -90:
                self.angulo -= self.vel_rotacao

    def desenhar(self, tela):
        # Definir a imagem q vai usar
        self.cont_imagem += 1

        if self.cont_imagem < self.tempo_animacao:
            self.imagem = self.IMGS[0]
        elif self.cont_imagem < self.tempo_animacao * 2:
            self.imagem = self.IMGS[1]
        elif self.cont_imagem < self.tempo_animacao * 3:
            self.imagem = self.IMGS[2]
        elif self.cont_imagem < self.tempo_animacao * 4:
            self.imagem = self.IMGS[1]
        elif self.cont_imagem >= self.tempo_animacao * 4 + 1:
            self.imagem = self.IMGS[0]
            self.cont_imagem = 0

            # se o passaro cair, não bater as asas
        if self.angulo == -80:
            self.imagem = self.IMGS[1]
            self.cont_imagem = self.tempo_animacao * 2

            # definir a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_center_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center

        retangulo = imagem_rotacionada.get_rect(center=pos_center_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Cano:
    distancia = 200
    vel_cano = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_cano, False, True)
        self.CANO_BASE = IMAGEM_cano
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 350)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.distancia

    def mover(self):
        self.x -= self.vel_cano

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colisao(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if topo_ponto or base_ponto:
            return True
        else:
            return False


class Chao:
    vel_chao = 5
    largura_chao = IMAGEM_chao.get_width()
    imagem = IMAGEM_chao

    def __init__(self, y):
        self.y = y
        self.chao1 = 0
        self.chao2 = self.largura_chao

    def mover(self):
        self.chao1 -= self.vel_chao
        self.chao2 -= self.vel_chao

        if self.chao1 + self.largura_chao < 0:
            self.chao1 = self.chao2 + self.largura_chao

        if self.chao2 + self.largura_chao < 0:
            self.chao2 = self.chao1 + self.largura_chao

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.chao1, self.y))
        tela.blit(self.imagem, (self.chao2, self.y))


def desenhar_jogo(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_background, (0, 0))
    for bird in passaros:
        bird.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto = FONTE_PONTOS.render(f'Pontuação: {pontos}', 1, BRANCO)
    tela.blit(texto, (largura - 10 - texto.get_width(), 10))

    texto = FONTE_PONTOS.render(f'Geração: {geracao}', 1, BRANCO)
    tela.blit(texto, (10, 10))

    chao.desenhar(tela)
    pygame.display.update()


def main(genomas, config):

    global geracao

    geracao += 1

    if ia_jogando:
        redes = []
        list_genoma = []
        birds = []

        for _, genoma in genomas:
            rede = neat.nn.FeedForwardNetwork.create(genoma, config)
            redes.append(rede)
            genoma.fitness = 0
            list_genoma.append(genoma)
            birds.append(Passaro(210, 350))

    else:
        birds = [Passaro(210, 350)]

    piso = Chao(640)
    can = [Cano(700)]
    screem = pygame.display.set_mode((largura, altura))
    pontinhos = 0
    tick = pygame.time.Clock()

    run = True
    while run:
        tick.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if not ia_jogando:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        for passaro in birds:
                            passaro.pular()

        indice_cano = 0
        if len(birds) > 0:
            if len(can) > 1 and birds[0].x > (can[0]. x + can[0].CANO_TOPO.get_width()):
                indice_cano = 1

        else:
            run = False
            break

        for i, passaro in enumerate(birds):
            passaro.mover()
            list_genoma[i].fitness += 0.1
            output = redes[i].activate((passaro.y,
                                        abs(passaro.y - can[indice_cano].altura),
                                        abs(passaro.y - can[indice_cano].pos_base)))

            if output[0] > 0.5:
                passaro.pular()

        piso.mover()

        add_cano = False
        remover_canos = []

        for cano in can:
            for i, passaro in enumerate(birds):
                if cano.colisao(passaro):
                    birds.pop(i)
                    if ia_jogando:
                        list_genoma[i].fitness -= 1
                        list_genoma.pop(i)
                        redes.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    add_cano = True

            cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if add_cano:
            pontinhos += 1
            can.append(Cano(600))
            for genoma in list_genoma:
                genoma.fitness += 5

            if pontinhos >= 10:
                Cano.vel_cano += 0.2
            else:
                Cano.vel_cano = 5

        for cano in remover_canos:
            can.remove(cano)

        for i, passaro in enumerate(birds):
            if (passaro.y + passaro.imagem.get_height()) > piso.y or passaro.y < 0:
                birds.pop(i)
                if ia_jogando:
                    list_genoma.pop(i)
                    redes.pop(i)

        desenhar_jogo(screem, birds, can, piso, pontinhos)


def rodar(c_config):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                c_config)

    populacao = neat.Population(config)
    populacao.add_reporter(neat.StdOutReporter(True))
    populacao.add_reporter(neat.StatisticsReporter())

    if ia_jogando:
        populacao.run(main, 50)
    else:
        main(None, None)


caminho = os.path.dirname(__file__)
caminho_config = os.path.join(caminho, 'configIA.txt')
rodar(caminho_config)
