from config import largura,altura,largura_carro,altura_carro, pista_esquerda, pista_direita,velocidade_carro,largura_pista
import pygame
import random
#definicao da classe do carro do jogador 
class Jogador (pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets["carro_jogador"]
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 10
        self.speedx = 0


    def update(self):
        # Atualização da posição do carro 
        self.rect.x += self.speedx
        # Mantem dentro da pista
        if self.rect.right > pista_direita:
            self.rect.right = pista_direita
        if self.rect.left < pista_esquerda:
            self.rect.left = pista_esquerda
        


class Obstaculo (pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)
        # lista com as 4 imagens possiveis dos obstaculos
        lista_cores_carros = [assets["carro_amarelo"], assets["carro_branco"], assets["carro_roxo"], assets["carro_vermelho"]]
        # sorteia uma das imagens da lista
        self.image = random.choice(lista_cores_carros)
        #get rect serve para pegar um "quadrado" com as posicoes 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(pista_esquerda, pista_direita-largura_carro)
        self.rect.y = -altura_carro
        self.speedy = velocidade_carro

    def update(self):
        # Se o obstaculo passar fora da tela morre .
        self.rect.y += self.speedy
        if self.rect.top > altura:
            self.kill()

