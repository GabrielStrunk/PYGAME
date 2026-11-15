import pygame
from config import largura, altura, altura_carro,largura_carro


def load_assets():
    assets = {}
    #difinicao imagens e fazendo a devida escala 
    assets["carro_jogador"] = pygame.image.load('assets/img/carro_jogador.png').convert_alpha()
    assets["carro_jogador"] = pygame.transform.scale(assets["carro_jogador"], (largura_carro, altura_carro))
    assets["carro_amarelo"] = pygame.image.load('assets/img/carro_amarelo.png').convert_alpha()
    assets["carro_amarelo"] = pygame.transform.scale(assets["carro_amarelo"], (largura_carro, altura_carro))
    assets["carro_branco"] = pygame.image.load('assets/img/carro_branco.png').convert_alpha()
    assets["carro_branco"] = pygame.transform.scale(assets["carro_branco"], (largura_carro, altura_carro))
    assets["carro_roxo"] = pygame.image.load('assets/img/carro_roxo.png').convert_alpha()
    assets["carro_roxo"] = pygame.transform.scale(assets["carro_roxo"], (largura_carro, altura_carro))
    assets["carro_vermelho"] = pygame.image.load('assets/img/carro_vermelho.png').convert_alpha()
    assets["carro_vermelho"] = pygame.transform.scale(assets["carro_vermelho"], (largura_carro, altura_carro))
    assets["fundo_com_pista"] = pygame.image.load('assets/img/fundo_com_pista.png').convert()
    assets["fundo_com_pista"] = pygame.transform.scale(assets["fundo_com_pista"], (largura, altura))

    # animacao da explosao (9 imagens numeradas de 00 a 08)
    explosion_anim = []
    for i in range(9):
        filename = 'assets/img/regularExplosion0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    assets["explosion_anim"] = explosion_anim

    # fonte para escrever o tempo e as vidas (a mesma do v18)
    assets["fonte"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

    # sons
    assets["boom_sound"] = pygame.mixer.Sound('assets/snd/expl3.wav')
    assets["destroy_sound"] = pygame.mixer.Sound('assets/snd/expl6.wav')

    return assets
