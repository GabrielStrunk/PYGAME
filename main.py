import pygame
from assets import load_assets
from game_screen import game_screen
from init_screen import init_screen
from gameover_screen import gameover_screen
from config import largura, altura, TELA_INICIAL, TELA_JOGO, TELA_FIM, SAIR, carros_jogador

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
tela = TELA_INICIAL
carro_escolhido = carros_jogador[0]   # sera trocado pela escolha na tela inicial
tempo_partida = 0                     # tempo da ultima partida, em segundos
while tela != SAIR:
    if tela == TELA_INICIAL:
        # a tela inicial devolve duas coisas: a proxima tela e o carro escolhido
        tela, carro_escolhido = init_screen(window, assets)
    elif tela == TELA_JOGO:
        # o jogo devolve duas coisas: a proxima tela e o tempo que o jogador durou
        tela, tempo_partida = game_screen(window, assets, carro_escolhido)
    elif tela == TELA_FIM:
        # game over: devolve TELA_JOGO (jogar de novo, com o mesmo carro) ou SAIR (sair)
        tela = gameover_screen(window, assets, tempo_partida)
    else:
        tela = SAIR

pygame.quit()

