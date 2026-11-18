from pathlib import Path


# Caminhos sempre relativos a esta pasta, mesmo abrindo o jogo por outro lugar.
base_dir = Path(__file__).resolve().parent
pasta_assets = base_dir / "assets"

# Dimensoes da janela e taxa de quadros.
altura = 900
largura = 700
FPS = 30

# Dimensoes dos carros.
altura_carro = 80
largura_carro = 50

# Velocidades em pixels por frame.
velocidade_inicial = 5
velocidade_jogador = 8

# Intervalo inicial entre os obstaculos, em milissegundos.
intervalo_inicial_menor = 800
intervalo_inicial_maior = 2000

# Aumento da dificuldade.
tempo_entre_aumentos = 5000
aumento_velocidade = 1
reducao_intervalo = 100
intervalo_minimo = 300
tempo_invensibilidade = 2000
vidas_iniciais = 2

# Cores.
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Arquivo do recorde, em segundos.
arquivo_recorde = str(base_dir / "recorde.txt")

# Chaves dos carros no dicionario assets.
carros_jogador = ["mustang", "ferrari", "carroca"]

# Estados dentro da partida.
FIM = 0
JOGANDO = 1
EXPLODINDO = 2

# Estados do gerente de telas.
TELA_INICIAL = 0
TELA_JOGO = 1
TELA_FIM = 2
SAIR = 3

# Limites da pista.
pista_esquerda = 152
pista_direita = 550

# Itens da pista: oleo, lama e turbo.
intervalo_item_menor = 3000
intervalo_item_maior = 6000
tempo_efeito = 3000
tremida_oleo = 6
largura_item = 60
altura_item = 60

# Troca de fundo e musica: 30.000 milissegundos = 30 segundos.
intervalo_cenario = 30_000
volume_musica = 0.4  # De 0.0 (sem som) a 1.0 (volume maximo).

# Ordem dos cenarios: normal -> noite -> inferno -> normal.
# Cada par contem a chave do fundo em assets e o caminho da musica.
cenarios = [
    (
        "fundo_com_pista",
        str(pasta_assets / "snd" / "tgfcoder-FrozenJam-SeamlessLoop.ogg"),
    ),
    (
        "fundo_com_pista_noite",
        str(pasta_assets / "snd" / "audiofundonoite.mp3"),
    ),
    (
        "fundo_com_pista_inferno",
        str(pasta_assets / "snd" / "audioinferno2.mp3"),
    ),
]
