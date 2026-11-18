import pygame
from config import largura, altura, altura_carro,largura_carro, largura_item, altura_item, pasta_assets


def load_assets():
    assets = {}
    #difinicao imagens e fazendo a devida escala
    # ----- os 3 carros do jogador (PNG com fundo transparente: convert_alpha mantem a transparencia)
    assets["mustang"] = pygame.image.load(str(pasta_assets / 'img' / 'mustang.png')).convert_alpha()
    assets["mustang"] = pygame.transform.scale(assets["mustang"], (largura_carro, altura_carro))
    assets["ferrari"] = pygame.image.load(str(pasta_assets / 'img' / 'ferrari.png')).convert_alpha()
    assets["ferrari"] = pygame.transform.scale(assets["ferrari"], (largura_carro, altura_carro))
    assets["carroca"] = pygame.image.load(str(pasta_assets / 'img' / 'carroca.png')).convert_alpha()
    assets["carroca"] = pygame.transform.scale(assets["carroca"], (largura_carro, altura_carro))

    # ----- carros obstaculos
    assets["carro_amarelo"] = pygame.image.load(str(pasta_assets / 'img' / 'carro_amarelo.png')).convert_alpha()
    assets["carro_amarelo"] = pygame.transform.scale(assets["carro_amarelo"], (largura_carro, altura_carro))
    assets["carro_branco"] = pygame.image.load(str(pasta_assets / 'img' / 'carro_branco.png')).convert_alpha()
    assets["carro_branco"] = pygame.transform.scale(assets["carro_branco"], (largura_carro, altura_carro))
    assets["carro_roxo"] = pygame.image.load(str(pasta_assets / 'img' / 'carro_roxo.png')).convert_alpha()
    assets["carro_roxo"] = pygame.transform.scale(assets["carro_roxo"], (largura_carro, altura_carro))
    assets["carro_vermelho"] = pygame.image.load(str(pasta_assets / 'img' / 'carro_vermelho.png')).convert_alpha()
    assets["carro_vermelho"] = pygame.transform.scale(assets["carro_vermelho"], (largura_carro, altura_carro))
    assets["fundo_com_pista"] = pygame.image.load(str(pasta_assets / 'img' / 'fundo_com_pista.png')).convert()
    assets["fundo_com_pista"] = pygame.transform.scale(assets["fundo_com_pista"], (largura, altura))

    # novas pistas
    assets["fundo_com_pista_noite"] = pygame.image.load(str(pasta_assets / 'img' / 'fundo_com_pista_noite.png')).convert()
    assets["fundo_com_pista_noite"] = pygame.transform.scale(assets["fundo_com_pista_noite"], (largura, altura))

    assets["fundo_com_pista_inferno"] = pygame.image.load(str(pasta_assets / 'img' / 'fundo_com_pista_inferno.png')).convert()
    assets["fundo_com_pista_inferno"] = pygame.transform.scale(assets["fundo_com_pista_inferno"], (largura, altura))

    # fundo da tela inicial: a foto e quadrada, entao vira um quadrado da altura da tela
    # (nao estica para 700 x 900, senao a foto fica deformada)
    assets["fundo_inicio"] = pygame.image.load(str(pasta_assets / 'img' / 'humberto.jpg')).convert()
    assets["fundo_inicio"] = pygame.transform.scale(assets["fundo_inicio"], (altura, altura))

    # animacao da explosao (9 imagens numeradas de 00 a 08)
    animacao_explosao = []
    for i in range(9):
        filename = str(pasta_assets / 'img' / 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (32, 32))
        animacao_explosao.append(img)
    assets["animacao_explosao"] = animacao_explosao

    # fonte para escrever o tempo e as vidas (a mesma do v18)
    assets["fonte"] = pygame.font.Font(str(pasta_assets / 'font' / 'PressStart2P.ttf'), 28)

    # sons
    assets["som_batida"] = pygame.mixer.Sound(str(pasta_assets / 'snd' / 'expl3.wav'))
    assets["som_destruicao"] = pygame.mixer.Sound(str(pasta_assets / 'snd' / 'expl6.wav'))

    # As musicas ficam no config e sao tocadas por pygame.mixer.music.

    # itens da pista (poderzinho) (o nome da chave e o mesmo "tipo" usado na classe Item)
    assets["oleo"] = pygame.image.load(str(pasta_assets / 'img' / 'z_oleo.png')).convert_alpha()
    assets["oleo"] = pygame.transform.scale(assets["oleo"], (largura_item, altura_item))
    assets["lama"] = pygame.image.load(str(pasta_assets / 'img' / 'z_lama.png')).convert_alpha()
    assets["lama"] = pygame.transform.scale(assets["lama"], (largura_item, altura_item))
    assets["turbo"] = pygame.image.load(str(pasta_assets / 'img' / 'z_turbo.png')).convert_alpha()
    assets["turbo"] = pygame.transform.scale(assets["turbo"], (altura_item, altura_item))

    return assets
