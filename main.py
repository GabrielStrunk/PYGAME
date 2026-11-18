import pygame

from assets import load_assets
from config import (
    altura,
    carros_jogador,
    cenarios,
    largura,
    SAIR,
    TELA_FIM,
    TELA_INICIAL,
    TELA_JOGO,
    volume_musica,
)
from game_screen import game_screen
from gameover_screen import gameover_screen
from init_screen import init_screen


def main():
    pygame.init()
    try:
        pygame.mixer.init()
        window = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("jogo corrida")

        # Carrega as imagens, fontes e efeitos uma unica vez.
        assets = load_assets()

        # Musica da tela inicial. A partida controla as proximas trocas.
        pygame.mixer.music.load(cenarios[0][1])
        pygame.mixer.music.set_volume(volume_musica)
        pygame.mixer.music.play(loops=-1)

        tela = TELA_INICIAL
        carro_escolhido = carros_jogador[0]
        tempo_partida = 0

        while tela != SAIR:
            if tela == TELA_INICIAL:
                tela, carro_escolhido = init_screen(window, assets)
            elif tela == TELA_JOGO:
                tela, tempo_partida = game_screen(window, assets, carro_escolhido)
            elif tela == TELA_FIM:
                tela = gameover_screen(window, assets, tempo_partida)
            else:
                tela = SAIR
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
