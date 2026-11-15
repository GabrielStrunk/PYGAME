import pygame 
from sprites import Jogador, Obstaculo
from assets import load_assets
import random
from config import largura, altura , FPS, largura_carro, altura_carro, velocidade_carro, aceleracao_carro, DONE,PLAYING,EXPLODING
#inicializacao do jogo 
pygame.init()
pygame.mixer.init()
#criacao da tela e dimencoes 
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo corrida')

#inicializacao da musica de fundo 
pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

#impostar assets
assets = load_assets()

#variavel para ajuste de velocidade

clock = pygame.time.Clock()
#criacao dos grupos de sprites
all_sprites = pygame.sprite.Group()
obstaculos_sprites = pygame.sprite.Group()
#criacao do jogador
jogador = Jogador(assets)
all_sprites.add(jogador)

obstaculo = Obstaculo(assets)
obstaculos_sprites.add(obstaculo)
all_sprites.add(obstaculo)

state = PLAYING
while state != DONE:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = DONE

    #atualiza todas as sprites
    all_sprites.update()

    #desenhando o fundo do jogo 
    window.blit(assets['fundo_com_pista'], (0, 0))

    #escrevendo/desenhando o jogador 
    all_sprites.draw(window)
    pygame.display.update()




pygame.quit()