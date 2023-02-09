# Importando as bibliotecas que irei usar
import pygame
import os
import random

#  Dimensões da tela
largura = 500
altura = 800

#  Fonte
FONTE_PONTOS = pygame.font.SysFont('arial', 40)

#  Imagens
IMAGEM_cano = pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'pipe.png')))
IMAGEM_chao = pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'base.png')))
IMAGEM_background = pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'bg.png')))
IMAGENS_bird = [
    pygame.transform.scale2x(pygame.imagem.load(os.path.join('img', 'bird1.png'))),
    pygame.transform.scale2x(pygame.imagem.load(os.path.join('img', 'bird2.png'))),
    pygame.transform.scale2x(pygame.imagem.load(os.path.join('img', 'bird3.png'))),
]


#  Objetos do game: Cano, chão e Pássaro
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
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.distancia

    def mover(self):
        self.x = self.vel_cano

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
        self.chao1 = self.vel_chao
        self.chao2 = self.vel_chao

        if self.chao1 + self.largura_chao < 0:
            self.chao1 = self.largura_chao + self.chao2
            
        if self.chao2 + self.largura_chao < 0:
            self.chao2 = self.largura_chao + self.chao1

    def desenhar(self):



class Passaro:
    pass
