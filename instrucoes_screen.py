"""Tela de instrucoes: explica os controles e os itens antes da partida."""
import pygame
from config import largura, altura, FPS, AMARELO, BRANCO, PRETO, TELA_JOGO, SAIR, vidas_iniciais, tempo_efeito


def escrever(window, fonte, frase, cor, centro_x, topo):
    """Escreve uma frase centralizada em centro_x, com o topo na altura topo."""
    texto = fonte.render(frase, True, cor)
    texto_rect = texto.get_rect()
    texto_rect.midtop = (centro_x, topo)
    window.blit(texto, texto_rect)


def instrucoes_screen(window, assets):
    """Mostra como jogar e espera o jogador apertar ENTER.

    Devolve TELA_JOGO (ENTER) ou SAIR (ESC ou fechar a janela).
    """
    clock = pygame.time.Clock()

    # cada item: chave da imagem no assets e o texto que explica o efeito
    itens = ["oleo", "lama", "turbo"]
    explicacoes = ["OLEO: O CARRO TREME", "LAMA: O CARRO FICA LENTO", "TURBO: O CARRO ACELERA"]

    proxima_tela = SAIR
    running = True
    while running:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                proxima_tela = SAIR
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    proxima_tela = SAIR
                    running = False
                if event.key == pygame.K_RETURN:
                    proxima_tela = TELA_JOGO
                    running = False

        # ----- Gera saidas
        window.fill(PRETO)
        fonte = assets["fonte"]
        pequena = assets["fonte_pequena"]

        escrever(window, fonte, "COMO JOGAR", AMARELO, largura / 2, 90)

        # controles
        escrever(window, pequena, "SETAS: MOVEM O CARRO", BRANCO, largura / 2, 220)
        escrever(window, pequena, "ESC: SAI DO JOGO", BRANCO, largura / 2, 260)

        # objetivo
        escrever(window, pequena, "DESVIE DOS CARROS!", AMARELO, largura / 2, 350)
        escrever(window, pequena, "VOCE TEM {} VIDAS".format(vidas_iniciais), AMARELO, largura / 2, 385)

        # itens: imagem a esquerda e explicacao a direita
        escrever(window, fonte, "ITENS", AMARELO, largura / 2, 460)
        for i in range(len(itens)):
            topo = 530 + i * 80
            img = assets[itens[i]]
            img_rect = img.get_rect()
            img_rect.topleft = (90, topo)
            window.blit(img, img_rect)

            texto = pequena.render(explicacoes[i], True, BRANCO)
            texto_rect = texto.get_rect()
            texto_rect.midleft = (img_rect.right + 30, img_rect.centery)
            window.blit(texto, texto_rect)

        escrever(window, pequena, "CADA EFEITO DURA {} SEGUNDOS".format(tempo_efeito // 1000), BRANCO, largura / 2, 770)

        escrever(window, fonte, "ENTER: COMECAR", AMARELO, largura / 2, altura - 80)

        pygame.display.update()

    return proxima_tela
