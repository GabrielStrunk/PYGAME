import pygame
import random
from sprites import Jogador, Obstaculo, Explosao
from config import largura, FPS, velocidade_inicial, FIM, JOGANDO, EXPLODINDO, intervalo_inicial_menor, tempo_invensibilidade, intervalo_inicial_maior, tempo_entre_aumentos, aumento_velocidade, reducao_intervalo, intervalo_minimo, vidas_iniciais, velocidade_jogador, VERMELHO, AMARELO, TELA_FIM, SAIR


def game_screen(window, assets, carro_escolhido):
    # Tela do jogo. Roda ate o jogo acabar e devolve (return) DUAS coisas:
    #   1) a proxima tela: TELA_FIM (as vidas acabaram) ou SAIR (fechou a janela)
    #   2) o tempo da partida, em segundos (para a tela de game over e o recorde)

    #variavel para ajuste de velocidade
    clock = pygame.time.Clock()
    #criacao dos grupos de sprites
    grupo_todos = pygame.sprite.Group()
    grupo_obstaculos = pygame.sprite.Group()
    #criacao do jogador
    jogador = Jogador(assets, carro_escolhido)
    grupo_todos.add(jogador)

    # controle de tempo para criar obstaculos
    hora_ultimo_obstaculo = pygame.time.get_ticks()        # hora da última criação
    espera_obstaculo = intervalo_inicial_menor   # espera sorteada (em ms)

    # controle da dificuldade (valores que MUDAM durante o jogo)
    velocidade_obstaculos = velocidade_inicial          # comeca com a velocidade do config
    reducao_total = 0                            # quanto o intervalo ja diminuiu no total
    hora_ultimo_aumento = pygame.time.get_ticks()     # hora do ultimo aumento de dificuldade
    #cria o dicionario key_down para exitar bug de morrer com o botao apertado 
    teclas_apertadas = {}
    vidas = vidas_iniciais   # comeca com 2 vidas
    hora_inicio = pygame.time.get_ticks()   # hora em que o jogo comecou (para o contador de tempo)
    tempo_partida = 0                       # segundos sobrevividos (para de contar quando as vidas acabam)

    proxima_tela = SAIR   # para onde ir quando o loop acabar
 
    estado = JOGANDO
    inicio = 0 
    while estado != FIM:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = FIM
                proxima_tela = SAIR        # fechou a janela: sai do jogo

            if estado == JOGANDO:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    teclas_apertadas[event.key] = True
                    if event.key == pygame.K_LEFT:
                        jogador.velocidade_x -= velocidade_jogador
                    if event.key == pygame.K_RIGHT:
                        jogador.velocidade_x += velocidade_jogador
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in teclas_apertadas and teclas_apertadas[event.key]:
                        if event.key == pygame.K_LEFT:
                            jogador.velocidade_x += velocidade_jogador
                        if event.key == pygame.K_RIGHT:
                            jogador.velocidade_x -= velocidade_jogador

        #pega o momento de agr
        agora = pygame.time.get_ticks()

        # ----- aumenta a dificuldade de tempos em tempos
        if agora - hora_ultimo_aumento > tempo_entre_aumentos:
            velocidade_obstaculos += aumento_velocidade    # obstaculos descem mais rapido
            reducao_total += reducao_intervalo        # obstaculos aparecem com mais frequencia
            hora_ultimo_aumento = agora                    # reinicia o cronometro

        # ----- cria um novo obstaculo quando passar o intervalo
        if agora - hora_ultimo_obstaculo > espera_obstaculo:
            #criacao do obsjeto obstaculo
            obstaculo = Obstaculo(assets, velocidade_obstaculos)
            grupo_todos.add(obstaculo)
            grupo_obstaculos.add(obstaculo)
            hora_ultimo_obstaculo = agora                          # anota a hora desta criação

            # sorteia a próxima espera, sem deixar ficar menor que o minimo
            menor = intervalo_inicial_menor - reducao_total
            maior = intervalo_inicial_maior - reducao_total
            if menor < intervalo_minimo:
                menor = intervalo_minimo
            if maior < intervalo_minimo:
                maior = intervalo_minimo
            espera_obstaculo = random.randint(menor, maior)

        #atualiza todas as sprites
        grupo_todos.update()

        # ----- colisao entre o jogador e os obstaculos
        if estado == JOGANDO:
            # o True faz o obstaculo que bateu sumir

            colisoes = pygame.sprite.spritecollide(jogador, grupo_obstaculos, True)
            if len(colisoes) > 0 and (pygame.time.get_ticks() - inicio >= tempo_invensibilidade):
                assets['som_batida'].play()
                jogador.kill()                 # o carro do jogador some
                vidas -= 1                     # perde uma vida
                # explosao no lugar onde o carro estava
                explosao = Explosao(jogador.rect.center, assets)
                grupo_todos.add(explosao)
                estado = EXPLODINDO
                teclas_apertadas = {}                 # evita o bug da tecla segurada (v17)
                hora_explosao = pygame.time.get_ticks()
                duracao_explosao = explosao.tempo_por_quadro * len(explosao.animacao_explosao) + 400

        elif estado == EXPLODINDO:
            # espera a explosao terminar
            if agora - hora_explosao > duracao_explosao:
                if vidas == 0:
                    estado = FIM               # acabaram as vidas: fim de jogo
                    proxima_tela = TELA_FIM        # vai para a tela de game over
                else:
                    estado = JOGANDO            # ainda tem vida: carro novo
                    inicio = pygame.time.get_ticks()
                    jogador = Jogador(assets, carro_escolhido)
                    grupo_todos.add(jogador)

        #desenhando o fundo do jogo
        window.blit(assets['fundo_com_pista'], (0, 0))

        #escrevendo/desenhando o jogador
        grupo_todos.draw(window)

        # ----- contador de tempo (em cima, no meio)
        # so conta enquanto ainda tem vida: na ultima explosao o tempo fica parado
        if vidas > 0:
            tempo_partida = (agora - hora_inicio) // 1000   # ms -> segundos inteiros
        minutos = tempo_partida // 60
        segundos = tempo_partida % 60
        texto = assets["fonte"].render("{:02d}:{:02d}".format(minutos, segundos), True, AMARELO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 10)
        window.blit(texto, texto_rect)

        # ----- contador de vidas (em cima, na esquerda)
        texto = assets["fonte"].render(chr(9829) * vidas, True, VERMELHO)
        texto_rect = texto.get_rect()
        texto_rect.topleft = (10, 10)
        window.blit(texto, texto_rect)

        pygame.display.update()

    return proxima_tela, tempo_partida
