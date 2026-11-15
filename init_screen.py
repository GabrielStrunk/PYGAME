import pygame
from config import largura, altura, FPS, AMARELO, BRANCO, carros_jogador, TELA_JOGO, SAIR


def init_screen(window, assets):
    # Tela inicial: o jogador escolhe um dos 3 carros com as teclas 1, 2 ou 3.
    # Devolve DUAS coisas: a proxima tela e o carro escolhido.
    clock = pygame.time.Clock()

    # ----- prepara as imagens dos 3 carros, maiores, so para mostrar na tela
    imagens = []
    for chave in carros_jogador:
        img = assets[chave]
        img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
        imagens.append(img)

    proxima_tela = SAIR
    carro_escolhido = carros_jogador[0]   # valor padrao, caso feche a janela

    running = True
    while running:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                proxima_tela = SAIR
                running = False

            if event.type == pygame.KEYDOWN:
                # cada tecla escolhe uma posicao da lista carros_jogador
                if event.key == pygame.K_1:
                    carro_escolhido = carros_jogador[0]
                    proxima_tela = TELA_JOGO
                    running = False
                if event.key == pygame.K_2:
                    carro_escolhido = carros_jogador[1]
                    proxima_tela = TELA_JOGO
                    running = False
                if event.key == pygame.K_3:
                    carro_escolhido = carros_jogador[2]
                    proxima_tela = TELA_JOGO
                    running = False

        # ----- Gera saidas
        # a foto tem 900 de largura e a tela 700: centraliza e as sobras dos lados ficam de fora
        window.blit(assets['fundo_inicio'], ((largura - altura) / 2, 0))

        # titulo
        texto = assets["fonte"].render("CORRIDA", True, AMARELO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 120)
        window.blit(texto, texto_rect)

        # instrucao
        texto = assets["fonte"].render("ESCOLHA SEU CARRO", True, BRANCO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 220)
        window.blit(texto, texto_rect)

        # os 3 carros lado a lado, com o numero embaixo de cada um
        for i in range(3):
            centro_x = largura * (i + 1) / 4      # 1/4, 2/4 e 3/4 da largura
            img_rect = imagens[i].get_rect()
            img_rect.center = (centro_x, altura / 2)
            window.blit(imagens[i], img_rect)

            texto = assets["fonte"].render(str(i + 1), True, AMARELO)
            texto_rect = texto.get_rect()
            texto_rect.midtop = (centro_x, img_rect.bottom + 20)
            window.blit(texto, texto_rect)

        # dica embaixo
        texto = assets["fonte"].render("APERTE 1, 2 OU 3", True, BRANCO)
        texto_rect = texto.get_rect()
        texto_rect.midbottom = (largura / 2, altura - 120)
        window.blit(texto, texto_rect)

        pygame.display.update()

    return proxima_tela, carro_escolhido
