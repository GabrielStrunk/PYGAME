import pygame

from config import (
    AMARELO,
    arquivo_recorde,
    BRANCO,
    FPS,
    largura,
    PRETO,
    SAIR,
    TELA_JOGO,
    VERMELHO,
)


def formatar_tempo(segundos_totais):
    minutos = segundos_totais // 60
    segundos = segundos_totais % 60
    return "{:02d}:{:02d}".format(minutos, segundos)


def gameover_screen(window, assets, tempo_partida):
    clock = pygame.time.Clock()

    # Um arquivo inexistente, vazio ou invalido comeca com recorde zero.
    try:
        with open(arquivo_recorde, "r", encoding="utf-8") as arquivo:
            recorde = int(arquivo.read().strip() or "0")
    except (FileNotFoundError, ValueError):
        recorde = 0

    novo_recorde = tempo_partida > recorde
    if novo_recorde:
        recorde = tempo_partida
        with open(arquivo_recorde, "w", encoding="utf-8") as arquivo:
            arquivo.write(str(recorde))

    proxima_tela = SAIR
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                proxima_tela = SAIR
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    proxima_tela = TELA_JOGO
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    proxima_tela = SAIR
                    running = False
            if not running:
                break

        if not running:
            break

        window.fill(PRETO)

        texto = assets["fonte"].render("GAME OVER", True, VERMELHO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 200)
        window.blit(texto, texto_rect)

        texto = assets["fonte"].render("SEU TEMPO: " + formatar_tempo(tempo_partida), True, BRANCO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 320)
        window.blit(texto, texto_rect)

        texto = assets["fonte"].render("RECORDE: " + formatar_tempo(recorde), True, AMARELO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 390)
        window.blit(texto, texto_rect)

        if novo_recorde:
            texto = assets["fonte"].render("NOVO RECORDE!", True, AMARELO)
            texto_rect = texto.get_rect()
            texto_rect.midtop = (largura / 2, 460)
            window.blit(texto, texto_rect)

        texto = assets["fonte"].render("ENTER: JOGAR DE NOVO", True, BRANCO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 620)
        window.blit(texto, texto_rect)

        texto = assets["fonte"].render("ESC: SAIR", True, BRANCO)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (largura / 2, 690)
        window.blit(texto, texto_rect)

        pygame.display.update()

    return proxima_tela
