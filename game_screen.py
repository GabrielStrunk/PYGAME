import pygame
import random
from sprites import Jogador, Obstaculo, Explosao, Item
from config import largura, FPS, velocidade_inicial, FIM, JOGANDO, EXPLODINDO, intervalo_inicial_menor, tempo_invensibilidade, intervalo_inicial_maior, tempo_entre_aumentos, aumento_velocidade, reducao_intervalo, intervalo_minimo, vidas_iniciais, velocidade_jogador, VERMELHO, AMARELO, TELA_FIM, SAIR
from config import intervalo_item_menor, intervalo_item_maior, BRANCO
from config import fundos_cenarios, musicas_cenarios, intervalo_cenario, volume_musica


def game_screen(window, assets, carro_escolhido):
    # Devolve a proxima tela e o tempo da partida, em segundos.
    clock = pygame.time.Clock()

    # Criacao dos grupos de sprites.
    grupo_todos = pygame.sprite.Group()
    grupo_obstaculos = pygame.sprite.Group()

    # Os itens sao desenhados antes dos carros para ficarem no chao.
    grupo_itens = pygame.sprite.Group()
    hora_ultimo_item = pygame.time.get_ticks()
    espera_item = random.randint(intervalo_item_menor, intervalo_item_maior)

    jogador = Jogador(assets, carro_escolhido)
    grupo_todos.add(jogador)

    # Controle de tempo para criar obstaculos.
    hora_ultimo_obstaculo = pygame.time.get_ticks()
    espera_obstaculo = intervalo_inicial_menor

    # Controle da dificuldade.
    velocidade_obstaculos = velocidade_inicial
    reducao_total = 0
    hora_ultimo_aumento = pygame.time.get_ticks()

    teclas_apertadas = {}
    vidas = vidas_iniciais
    tempo_partida = 0
    proxima_tela = SAIR

    # Cada nova partida comeca no fundo normal com Frozen Jam.
    cenario_atual = 0
    fundo_atual = assets[fundos_cenarios[cenario_atual]]
    pygame.mixer.music.load(musicas_cenarios[cenario_atual])
    pygame.mixer.music.set_volume(volume_musica)
    pygame.mixer.music.play(loops=-1)

    # O mesmo relogio controla o contador da partida e os cenarios.
    hora_inicio = pygame.time.get_ticks()
    estado = JOGANDO
    inicio = 0

    while estado != FIM:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = FIM
                proxima_tela = SAIR

            # ESC sai do jogo, inclusive durante uma explosao.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                estado = FIM
                proxima_tela = SAIR

            if estado == JOGANDO:
                if event.type == pygame.KEYDOWN:
                    teclas_apertadas[event.key] = True
                    if event.key == pygame.K_LEFT:
                        jogador.velocidade_x -= velocidade_jogador
                    if event.key == pygame.K_RIGHT:
                        jogador.velocidade_x += velocidade_jogador
                    if event.key == pygame.K_UP:
                        jogador.velocidade_y -= velocidade_jogador
                    if event.key == pygame.K_DOWN:
                        jogador.velocidade_y += velocidade_jogador

                if event.type == pygame.KEYUP:
                    if event.key in teclas_apertadas and teclas_apertadas[event.key]:
                        if event.key == pygame.K_LEFT:
                            jogador.velocidade_x += velocidade_jogador
                        if event.key == pygame.K_RIGHT:
                            jogador.velocidade_x -= velocidade_jogador
                        if event.key == pygame.K_UP:
                            jogador.velocidade_y += velocidade_jogador
                        if event.key == pygame.K_DOWN:
                            jogador.velocidade_y -= velocidade_jogador

        

        agora = pygame.time.get_ticks()

        # Troca fundo e musica juntos no intervalo definido no config.
        # Depois do inferno, volta ao normal e repete a sequencia.
        # Na ultima explosao, mantem o cenario, assim como o contador.
        if vidas > 0:
            novo_cenario = ((agora - hora_inicio) // intervalo_cenario) % len(fundos_cenarios)

            # So carrega a musica quando o cenario realmente muda.
            if novo_cenario != cenario_atual:
                cenario_atual = novo_cenario
                fundo_atual = assets[fundos_cenarios[cenario_atual]]
                pygame.mixer.music.load(musicas_cenarios[cenario_atual])
                pygame.mixer.music.set_volume(volume_musica)
                pygame.mixer.music.play(loops=-1)

        # Aumenta a dificuldade de tempos em tempos.
        if agora - hora_ultimo_aumento > tempo_entre_aumentos:
            velocidade_obstaculos += aumento_velocidade
            reducao_total += reducao_intervalo
            hora_ultimo_aumento = agora

        # Cria um novo obstaculo quando passar o intervalo.
        if agora - hora_ultimo_obstaculo > espera_obstaculo:
            obstaculo = Obstaculo(assets, velocidade_obstaculos)
            grupo_todos.add(obstaculo)
            grupo_obstaculos.add(obstaculo)
            hora_ultimo_obstaculo = agora

            menor = intervalo_inicial_menor - reducao_total
            maior = intervalo_inicial_maior - reducao_total
            if menor < intervalo_minimo:
                menor = intervalo_minimo
            if maior < intervalo_minimo:
                maior = intervalo_minimo
            espera_obstaculo = random.randint(menor, maior)

        # Cria um novo item (oleo, lama ou turbo).
        if agora - hora_ultimo_item > espera_item:
            item = Item(assets, velocidade_obstaculos)
            grupo_itens.add(item)
            hora_ultimo_item = agora
            espera_item = random.randint(intervalo_item_menor, intervalo_item_maior)

        grupo_todos.update()
        grupo_itens.update()

        if estado == JOGANDO:
            # collide_mask: so conta quando o desenho do carro encosta no desenho do item
            itens_pegos = pygame.sprite.spritecollide(jogador, grupo_itens, True, pygame.sprite.collide_mask)
            for item in itens_pegos:
                jogador.pegar_item(item.tipo)

        # Colisao entre o jogador e os obstaculos.
        if estado == JOGANDO:
            # collide_mask: so conta quando o desenho do carro encosta no desenho do obstaculo
            colisoes = pygame.sprite.spritecollide(jogador, grupo_obstaculos, True, pygame.sprite.collide_mask)
            if len(colisoes) > 0 and (pygame.time.get_ticks() - inicio >= tempo_invensibilidade):
                assets["som_batida"].play()
                jogador.kill()
                vidas -= 1

                explosao = Explosao(jogador.rect.center, assets)
                grupo_todos.add(explosao)
                estado = EXPLODINDO
                teclas_apertadas = {}
                hora_explosao = pygame.time.get_ticks()
                duracao_explosao = explosao.tempo_por_quadro * len(explosao.animacao_explosao) + 400

        elif estado == EXPLODINDO:
            if agora - hora_explosao > duracao_explosao:
                if vidas == 0:
                    estado = FIM
                    proxima_tela = TELA_FIM
                else:
                    estado = JOGANDO
                    inicio = pygame.time.get_ticks()
                    jogador = Jogador(assets, carro_escolhido)
                    grupo_todos.add(jogador)

        # Desenha o fundo do cenario atual.
        window.blit(fundo_atual, (0, 0))

        # Primeiro os itens no chao, depois os carros por cima.
        grupo_itens.draw(window)
        grupo_todos.draw(window)

        if jogador.efeito != "":
            texto = assets["fonte"].render(jogador.efeito.upper(), True, BRANCO)
            texto_rect = texto.get_rect()
            texto_rect.topright = (largura - 10, 10)
            window.blit(texto, texto_rect)

        # Contador de tempo: para quando as vidas acabam.
        if vidas > 0:
            tempo_partida = (agora - hora_inicio) // 1000
        minutos = tempo_partida // 60
        segundos = tempo_partida % 60
        texto = assets["fonte"].render("{:02d}:{:02d}".format(minutos, segundos), True, AMARELO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 10)
        window.blit(texto, texto_rect)

        # Contador de vidas.
        texto = assets["fonte"].render(chr(9829) * vidas, True, VERMELHO)
        texto_rect = texto.get_rect()
        texto_rect.topleft = (10, 10)
        window.blit(texto, texto_rect)

        pygame.display.update()

    return proxima_tela, tempo_partida
