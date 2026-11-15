import pygame
from assets import load_assets
from game_screen import game_screen
from init_screen import init_screen
from config import largura, altura, INIT, GAME, OVER, QUIT, carros_jogador

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

#impostar assets (carrega uma vez so, e entrega para as telas)
assets = load_assets()

# ===== Gerente de telas =====
# Cada tela roda ate acabar e devolve qual e a proxima tela.
tela = INIT
carro_escolhido = carros_jogador[0]   # sera trocado pela escolha na tela inicial
while tela != QUIT:
    if tela == INIT:
        # a tela inicial devolve duas coisas: a proxima tela e o carro escolhido
        tela, carro_escolhido = init_screen(window, assets)
    elif tela == GAME:
        tela = game_screen(window, assets, carro_escolhido)
    elif tela == OVER:
        # a tela de game over ainda nao existe: por enquanto, volta para o inicio
        tela = INIT
    else:
        tela = QUIT

pygame.quit()
