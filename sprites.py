"""Classes dos sprites do jogo: Jogador, Obstaculo, Explosao e Item."""
from config import largura,altura,largura_carro,altura_carro, pista_esquerda, pista_direita, tempo_efeito, tremida_oleo, largura_item, altura_item
import pygame
import random
#definicao da classe do carro do jogador
class Jogador (pygame.sprite.Sprite):
    """Carro controlado pelo jogador com as setas.

    Fica sempre dentro dos limites da pista e pode estar sob o efeito
    de um item (oleo, lama ou turbo) por um tempo limitado.
    """
    def __init__(self, assets, carro_escolhido):
        """Cria o carro na parte de baixo da tela.

        assets: dicionario com as imagens carregadas.
        carro_escolhido: chave do carro escolhido na tela inicial.
        """
        pygame.sprite.Sprite.__init__(self)
        # usa a imagem do carro que o jogador escolheu na tela inicial
        self.image = assets[carro_escolhido]
        # mask: contorno da imagem, so com os pixels que nao sao transparentes
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 10
        self.velocidade_x = 0
        self.velocidade_y= 0

        # efeito do item que o carro pegou: "" (nenhum), "oleo", "lama" ou "turbo"
        self.efeito = ""
        self.hora_efeito = 0      # hora em que pegou o item (ms)

    def pegar_item (self, tipo):
        """Ativa o efeito do item pego ("oleo", "lama" ou "turbo") e marca a hora."""
        self.efeito = tipo
        self.hora_efeito = pygame.time.get_ticks()


    def update(self):
        """Move o carro conforme a velocidade e o efeito ativo, sem sair da pista."""
        # ----- o efeito acabou? (mesma ideia do tempo da explosao e do tiro da navinha)
        agora = pygame.time.get_ticks()
        if self.efeito != "" and agora - self.hora_efeito > tempo_efeito:
            self.efeito = ""

        # Atualização da posição do carro, dependendo do efeito
        if self.efeito == "lama":
            # na lama o carro anda pela metade
            self.rect.x += self.velocidade_x // 2
            self.rect.y += self.velocidade_y // 2
        elif self.efeito == "turbo":
            # no turbo o carro anda o dobro (fica dificil de controlar)
            self.rect.x += self.velocidade_x * 2
            self.rect.y += self.velocidade_y * 2
        else:
            self.rect.x += self.velocidade_x
            self.rect.y += self.velocidade_y

        if self.efeito == "oleo":
            self.rect.x += random.randint(-tremida_oleo, tremida_oleo)

        # Mantem dentro da pista
        if self.rect.right > pista_direita:
            self.rect.right = pista_direita
        if self.rect.left < pista_esquerda:
            self.rect.left = pista_esquerda

        #mantem o carro dentro da pista em relacoa a aultura 
        if self.rect.bottom > altura:
            self.rect.bottom = altura
        if self.rect.top < 0 :
            self.rect.top = 0 


        


class Obstaculo (pygame.sprite.Sprite):
    """Carro inimigo que nasce no topo da pista e desce ate sair da tela."""
    def __init__(self,assets,velocidade):
        """Sorteia a cor e a posicao do carro. velocidade: pixels por frame."""
        pygame.sprite.Sprite.__init__(self)
       
        cores = ["carro_amarelo", "carro_branco", "carro_roxo", "carro_vermelho"]
        # sorteia uma das imagens da lista a parti do nome da cor
        self.image = assets[random.choice(cores)]
        # mask: contorno da imagem, so com os pixels que nao sao transparentes
        self.mask = pygame.mask.from_surface(self.image)    
        #get rect serve para pegar um "quadrado" com as posicoes 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(pista_esquerda, pista_direita-largura_carro)
        self.rect.y = -altura_carro
        self.velocidade_y = velocidade   # recebe a velocidade atual do jogo

    def update(self):
        """Desce o obstaculo e o remove quando passa do fim da tela."""
        # Se o obstaculo passar fora da tela morre .
        self.rect.y += self.velocidade_y
        if self.rect.top > altura:
            self.kill()


# classe da explosao (mesma do v15): troca de imagem a cada tempo_por_quadro ms
class Explosao(pygame.sprite.Sprite):
    """Animacao de explosao mostrada quando o jogador bate."""
    def __init__(self, centro, assets):
        """Comeca a animacao na posicao centro (x, y)."""
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
        """Troca para a proxima imagem da animacao; some depois da ultima."""
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

    # item que fica no chao da pista (oleo, lama ou turbo) - funciona igual ao Obstaculo: nasce em cima e desce junto com a pista
class Item (pygame.sprite.Sprite):
    """Item no chao da pista (oleo, lama ou turbo) que muda o carro por um tempo."""
    def __init__(self, assets, velocidade):
        """Sorteia o tipo e a posicao do item. velocidade: pixels por frame."""
        pygame.sprite.Sprite.__init__(self)

        # sorteia o tipo do item; o tipo e tambem a chave da imagem no assets
        self.tipo = random.choice(["oleo", "lama", "turbo"])
        self.image = assets[self.tipo]
        # mask: contorno da imagem, so com os pixels que nao sao transparentes
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(pista_esquerda, pista_direita - largura_item)
        self.rect.y = -altura_item
        self.velocidade_y = velocidade

    def update(self):
        """Desce o item junto com a pista e o remove quando sai da tela."""
        self.rect.y += self.velocidade_y
        # passou do fim da tela: some
        if self.rect.top > altura:
            self.kill()

