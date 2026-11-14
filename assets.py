import pygame


def load_assets():
    assets = {}
    #difinicao imagens
    assets["carro_jogador"] = pygame.image.load('assets/img/carro_jogador.png').convert_alpha()
    assets["carro_amarelo"] = pygame.image.load('assets/img/carro_amarelo.png').convert_alpha()
    assets["carro_branco"] = pygame.image.load('assets/img/carro_branco.png').convert_alpha()
    assets["carro_roxo"] = pygame.image.load('assets/img/carro_roxo.png').convert_alpha()
    assets["carro_vermelho"] = pygame.image.load('assets/img/carro_vermelho.png').convert_alpha()
    assets["fundo_com_pista"] = pygame.image.load('assets/img/fundo_com_pista.png').convert()

    # sons
    assets["boom_sound"] = pygame.mixer.Sound('assets/snd/expl3.wav')
    assets["destroy_sound"] = pygame.mixer.Sound('assets/snd/expl6.wav')

    return assets
