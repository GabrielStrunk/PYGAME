import pygame 
from config import largura, altura , FPS, largura_carro, altura_carro, velocidade_carro, aceleracao_carro
#inicializacao do jogo 
pygame.init()
pygame.mixer.init()
#criacao da tela e dimencoes 
window = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('jogo corrida')

#inicializacao da musica de fundo 
pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)