from config import largura,altura,largura_carro,altura_carro, pista_esquerda, pista_direita
import pygame
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
        # Atualização da posição da nave
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > pista_direita:
            self.rect.right = pista_direita
        if self.rect.left < pista_esquerda:
            self.rect.left = pista_esquerda
        
