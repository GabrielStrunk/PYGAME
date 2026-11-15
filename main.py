import pygame 
from sprites import Jogador, Obstaculo
from assets import load_assets
import random
from config import largura, altura , FPS, largura_carro, altura_carro, velocidade_carro, aceleracao_carro, DONE,PLAYING,EXPLODING, intervalo_tempo1,intervalo_tempo2
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

# controle de tempo para criar obstaculos
ultimo_obstaculo = pygame.time.get_ticks()        # hora da última criação
intervalo_obstaculo = intervalo_tempo1   # espera sorteada (em ms)



keys_down = {}

state = PLAYING
while state != DONE:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = DONE


        if state == PLAYING:
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                keys_down[event.key] = True
                if event.key == pygame.K_LEFT:
                    jogador.speedx -= 8
                if event.key == pygame.K_RIGHT:
                    jogador.speedx += 8
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        jogador.speedx += 8
                    if event.key == pygame.K_RIGHT:
                        jogador.speedx -= 8


    #pega o momento de agr 
    agora = pygame.time.get_ticks()
    if agora - ultimo_obstaculo > intervalo_obstaculo:
        #criacao do obsjeto obstaculo
        obstaculo = Obstaculo(assets)
        all_sprites.add(obstaculo)
        obstaculos_sprites.add(obstaculo)
        ultimo_obstaculo = agora                          # anota a hora desta criação
        intervalo_obstaculo = random.randint(intervalo_tempo1, intervalo_tempo2)   # sorteia a próxima espera

    #atualiza todas as sprites
    all_sprites.update()

    #desenhando o fundo do jogo 
    window.blit(assets['fundo_com_pista'], (0, 0))

    #escrevendo/desenhando o jogador 
    all_sprites.draw(window)
    pygame.display.update()




pygame.quit()