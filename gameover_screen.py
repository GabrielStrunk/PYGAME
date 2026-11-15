import pygame
import os
from config import largura, FPS, AMARELO, BRANCO, VERMELHO, PRETO, arquivo_recorde, GAME, QUIT


def formatar_tempo(segundos_totais):
    # transforma segundos em texto "mm:ss" (ex.: 83 -> "01:23")
    minutos = segundos_totais // 60
    segundos = segundos_totais % 60
    return "{:02d}:{:02d}".format(minutos, segundos)


def gameover_screen(window, assets, tempo_partida):
    # Tela de game over: mostra o tempo e o recorde.
    # ENTER -> joga de novo (GAME) | ESC -> sai (QUIT)
    clock = pygame.time.Clock()

    # ----- le o recorde do arquivo (se ainda nao existe, o recorde e 0)
    recorde = 0
    if os.path.exists(arquivo_recorde):
        arquivo = open(arquivo_recorde, 'r')
        recorde = int(arquivo.read())   # o arquivo guarda texto: int() transforma em numero
        arquivo.close()

    # ----- se bateu o recorde (MAIOR tempo), salva o novo no arquivo
    novo_recorde = False
    if tempo_partida > recorde:
        recorde = tempo_partida
        arquivo = open(arquivo_recorde, 'w')   # 'w' apaga o que tinha e escreve de novo
        arquivo.write(str(recorde))            # write so aceita texto: str() transforma o numero
        arquivo.close()
        novo_recorde = True

    proxima_tela = QUIT
    running = True
    while running:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                proxima_tela = QUIT
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:     # ENTER
                    proxima_tela = GAME
                    running = False
                if event.key == pygame.K_ESCAPE:     # ESC
                    proxima_tela = QUIT
                    running = False

        # ----- Gera saidas
        window.fill(PRETO)

        text_surface = assets["fonte"].render("GAME OVER", True, VERMELHO)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (largura / 2, 200)
        window.blit(text_surface, text_rect)

        text_surface = assets["fonte"].render("SEU TEMPO: " + formatar_tempo(tempo_partida), True, BRANCO)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (largura / 2, 320)
        window.blit(text_surface, text_rect)

        text_surface = assets["fonte"].render("RECORDE: " + formatar_tempo(recorde), True, AMARELO)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (largura / 2, 390)
        window.blit(text_surface, text_rect)

        if novo_recorde:
            text_surface = assets["fonte"].render("NOVO RECORDE!", True, AMARELO)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (largura / 2, 460)
            window.blit(text_surface, text_rect)

        text_surface = assets["fonte"].render("ENTER: JOGAR DE NOVO", True, BRANCO)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (largura / 2, 620)
        window.blit(text_surface, text_rect)

        text_surface = assets["fonte"].render("ESC: SAIR", True, BRANCO)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (largura / 2, 690)
        window.blit(text_surface, text_rect)

        pygame.display.update()

    return proxima_tela
