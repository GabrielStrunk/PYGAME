import pygame

from config import (
    altura,
    AMARELO,
    BRANCO,
    carros_jogador,
    FPS,
    largura,
    SAIR,
    TELA_JOGO,
)


def init_screen(window, assets):
    # Devolve a proxima tela e o carro escolhido.
    clock = pygame.time.Clock()

    imagens = []
    for chave in carros_jogador:
        img = assets[chave]
        img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
        imagens.append(img)

    proxima_tela = SAIR
    carro_escolhido = carros_jogador[0]
    teclas_carros = (pygame.K_1, pygame.K_2, pygame.K_3)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                proxima_tela = SAIR
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    proxima_tela = SAIR
                    running = False
                elif event.key in teclas_carros:
                    indice = teclas_carros.index(event.key)
                    carro_escolhido = carros_jogador[indice]
                    proxima_tela = TELA_JOGO
                    running = False
            if not running:
                break

        if not running:
            break

        # Centraliza a foto quadrada, recortando as sobras laterais.
        window.blit(assets["fundo_inicio"], ((largura - altura) / 2, 0))

        texto = assets["fonte"].render("CORRIDA", True, AMARELO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 120)
        window.blit(texto, texto_rect)

        texto = assets["fonte"].render("ESCOLHA SEU CARRO", True, BRANCO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 220)
        window.blit(texto, texto_rect)

        for i in range(3):
            centro_x = largura * (i + 1) / 4
            img_rect = imagens[i].get_rect()
            img_rect.center = (centro_x, altura / 2)
            window.blit(imagens[i], img_rect)

            texto = assets["fonte"].render(str(i + 1), True, AMARELO)
            texto_rect = texto.get_rect()
            texto_rect.midtop = (centro_x, img_rect.bottom + 20)
            window.blit(texto, texto_rect)

        texto = assets["fonte"].render("APERTE 1, 2 OU 3", True, BRANCO)
        texto_rect = texto.get_rect()
        texto_rect.midbottom = (largura / 2, altura - 120)
        window.blit(texto, texto_rect)

        pygame.display.update()

    return proxima_tela, carro_escolhido
