import pygame
import random
from sprites import Jogador, Obstaculo, Explosion
from config import largura, FPS, velocidade_carro, DONE, PLAYING, EXPLODING, intervalo_tempo1, intervalo_tempo2, tempo_entre_aumentos, aumento_velocidade, reducao_intervalo, intervalo_minimo, vidas_iniciais, VERMELHO, AMARELO, OVER, QUIT


def game_screen(window, assets, carro_escolhido):
    # Tela do jogo. Roda ate o jogo acabar e devolve (return) a proxima tela:
    #   OVER -> as vidas acabaram (vai para a tela de game over)
    #   QUIT -> o jogador fechou a janela

    #variavel para ajuste de velocidade
    clock = pygame.time.Clock()
    #criacao dos grupos de sprites
    all_sprites = pygame.sprite.Group()
    obstaculos_sprites = pygame.sprite.Group()
    #criacao do jogador
    jogador = Jogador(assets, carro_escolhido)
    all_sprites.add(jogador)

    # controle de tempo para criar obstaculos
    ultimo_obstaculo = pygame.time.get_ticks()        # hora da última criação
    intervalo_obstaculo = intervalo_tempo1   # espera sorteada (em ms)

    # controle da dificuldade (valores que MUDAM durante o jogo)
    velocidade_atual = velocidade_carro          # comeca com a velocidade do config
    reducao_total = 0                            # quanto o intervalo ja diminuiu no total
    ultimo_aumento = pygame.time.get_ticks()     # hora do ultimo aumento de dificuldade

    keys_down = {}
    vidas = vidas_iniciais   # comeca com 2 vidas
    inicio_jogo = pygame.time.get_ticks()   # hora em que o jogo comecou (para o contador de tempo)

    proxima_tela = QUIT   # para onde ir quando o loop acabar

    state = PLAYING
    while state != DONE:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                proxima_tela = QUIT        # fechou a janela: sai do jogo

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

        # ----- aumenta a dificuldade de tempos em tempos
        if agora - ultimo_aumento > tempo_entre_aumentos:
            velocidade_atual += aumento_velocidade    # obstaculos descem mais rapido
            reducao_total += reducao_intervalo        # obstaculos aparecem com mais frequencia
            ultimo_aumento = agora                    # reinicia o cronometro

        # ----- cria um novo obstaculo quando passar o intervalo
        if agora - ultimo_obstaculo > intervalo_obstaculo:
            #criacao do obsjeto obstaculo
            obstaculo = Obstaculo(assets, velocidade_atual, carro_escolhido)
            all_sprites.add(obstaculo)
            obstaculos_sprites.add(obstaculo)
            ultimo_obstaculo = agora                          # anota a hora desta criação

            # sorteia a próxima espera, sem deixar ficar menor que o minimo
            menor = intervalo_tempo1 - reducao_total
            maior = intervalo_tempo2 - reducao_total
            if menor < intervalo_minimo:
                menor = intervalo_minimo
            if maior < intervalo_minimo:
                maior = intervalo_minimo
            intervalo_obstaculo = random.randint(menor, maior)

        #atualiza todas as sprites
        all_sprites.update()

        # ----- colisao entre o jogador e os obstaculos
        if state == PLAYING:
            # o True faz o obstaculo que bateu sumir
            hits = pygame.sprite.spritecollide(jogador, obstaculos_sprites, True)
            if len(hits) > 0:
                assets['boom_sound'].play()
                jogador.kill()                 # o carro do jogador some
                vidas -= 1                     # perde uma vida
                # explosao no lugar onde o carro estava
                explosao = Explosion(jogador.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}                 # evita o bug da tecla segurada (v17)
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400

        elif state == EXPLODING:
            # espera a explosao terminar
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if vidas == 0:
                    state = DONE               # acabaram as vidas: fim de jogo
                    proxima_tela = OVER        # vai para a tela de game over
                else:
                    state = PLAYING            # ainda tem vida: carro novo
                    jogador = Jogador(assets, carro_escolhido)
                    all_sprites.add(jogador)

        #desenhando o fundo do jogo
        window.blit(assets['fundo_com_pista'], (0, 0))

        #escrevendo/desenhando o jogador
        all_sprites.draw(window)

        # ----- contador de tempo (em cima, no meio)
        segundos_totais = (agora - inicio_jogo) // 1000   # ms -> segundos inteiros
        minutos = segundos_totais // 60
        segundos = segundos_totais % 60
        text_surface = assets["fonte"].render("{:02d}:{:02d}".format(minutos, segundos), True, AMARELO)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (largura / 2, 10)
        window.blit(text_surface, text_rect)

        # ----- contador de vidas (em cima, na esquerda)
        text_surface = assets["fonte"].render(chr(9829) * vidas, True, VERMELHO)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()

    return proxima_tela
