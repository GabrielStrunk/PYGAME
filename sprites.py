from config import largura,altura,largura_carro,altura_carro, pista_esquerda, pista_direita
import pygame
import random
#definicao da classe do carro do jogador 
class Jogador (pygame.sprite.Sprite):
    def __init__(self, assets, carro_escolhido):
        pygame.sprite.Sprite.__init__(self)
        # usa a imagem do carro que o jogador escolheu na tela inicial
        self.image = assets[carro_escolhido]
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 10
        self.velocidade_x = 0


    def update(self):
        # Atualização da posição do carro 
        self.rect.x += self.velocidade_x
        # Mantem dentro da pista
        if self.rect.right > pista_direita:
            self.rect.right = pista_direita
        if self.rect.left < pista_esquerda:
            self.rect.left = pista_esquerda
        


class Obstaculo (pygame.sprite.Sprite):
    def __init__(self,assets,velocidade):
        pygame.sprite.Sprite.__init__(self)
       
        cores = ["carro_amarelo", "carro_branco", "carro_roxo", "carro_vermelho"]
        # sorteia uma das imagens da lista a parti do nome da cor
        self.image = assets[random.choice(cores)]
        #get rect serve para pegar um "quadrado" com as posicoes 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(pista_esquerda, pista_direita-largura_carro)
        self.rect.y = -altura_carro
        self.velocidade_y = velocidade   # recebe a velocidade atual do jogo

    def update(self):
        # Se o obstaculo passar fora da tela morre .
        self.rect.y += self.velocidade_y
        if self.rect.top > altura:
            self.kill()


# classe da explosao (mesma do v15): troca de imagem a cada tempo_por_quadro ms
class Explosao(pygame.sprite.Sprite):
    def __init__(self, centro, assets):
        pygame.sprite.Sprite.__init__(self)

        # lista com as imagens da animacao
        self.animacao_explosao = assets['animacao_explosao']

        # comeca na primeira imagem, no lugar indicado
        self.quadro = 0
        self.image = self.animacao_explosao[self.quadro]
        self.rect = self.image.get_rect()
        self.rect.center = centro

        # hora em que a imagem atual foi mostrada
        self.hora_ultima_troca = pygame.time.get_ticks()
        # quanto tempo cada imagem fica na tela (ms)
        self.tempo_por_quadro = 50

    def update(self):
        agora = pygame.time.get_ticks()
        tempo_passado = agora - self.hora_ultima_troca

        # ja esta na hora de trocar de imagem?
        if tempo_passado > self.tempo_por_quadro:
            self.hora_ultima_troca = agora
            self.quadro += 1

            # acabaram as imagens: a explosao some
            if self.quadro == len(self.animacao_explosao):
                self.kill()
            else:
                centro = self.rect.center
                self.image = self.animacao_explosao[self.quadro]
                self.rect = self.image.get_rect()
                self.rect.center = centro

