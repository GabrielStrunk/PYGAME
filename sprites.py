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
    def __init__(self,assets,velocidade):
        pygame.sprite.Sprite.__init__(self)
        # lista com as 4 imagens possiveis dos obstaculos
        lista_cores_carros = [assets["carro_amarelo"], assets["carro_branco"], assets["carro_roxo"], assets["carro_vermelho"]]
        # sorteia uma das imagens da lista
        self.image = random.choice(lista_cores_carros)
        #get rect serve para pegar um "quadrado" com as posicoes 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(pista_esquerda, pista_direita-largura_carro)
        self.rect.y = -altura_carro
        self.speedy = velocidade   # recebe a velocidade atual do jogo

    def update(self):
        # Se o obstaculo passar fora da tela morre .
        self.rect.y += self.speedy
        if self.rect.top > altura:
            self.kill()


# classe da explosao (mesma do v15): troca de imagem a cada frame_ticks ms
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, assets):
        pygame.sprite.Sprite.__init__(self)

        # lista com as imagens da animacao
        self.explosion_anim = assets['explosion_anim']

        # comeca na primeira imagem, no lugar indicado
        self.frame = 0
        self.image = self.explosion_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        # hora em que a imagem atual foi mostrada
        self.last_update = pygame.time.get_ticks()
        # quanto tempo cada imagem fica na tela (ms)
        self.frame_ticks = 50

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        # ja esta na hora de trocar de imagem?
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1

            # acabaram as imagens: a explosao some
            if self.frame == len(self.explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

