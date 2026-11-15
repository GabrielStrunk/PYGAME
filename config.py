#declaracao de variaveis 

altura  = 900
largura = 700
FPS = 30 

altura_carro = 80
largura_carro = 50

# velocidades (em pixels por frame)
velocidade_inicial = 5       # velocidade com que os obstaculos comecam descendo
velocidade_jogador = 8       # quanto o carro do jogador anda para o lado ao segurar a seta

# espera entre um obstaculo e outro no comeco do jogo: sorteada entre esses dois valores (ms)
intervalo_inicial_menor = 800
intervalo_inicial_maior = 2000

# dificuldade: a cada tempo_entre_aumentos ms o jogo fica mais dificil
tempo_entre_aumentos = 5000   # de quanto em quanto tempo aumenta (ms)
aumento_velocidade = 1        # quanto a velocidade dos obstaculos sobe a cada aumento
reducao_intervalo = 100       # quanto o intervalo entre obstaculos diminui a cada aumento (ms)
intervalo_minimo = 300        # o intervalo nunca fica menor que isso (ms)

vidas_iniciais = 2

# cores
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# arquivo onde o recorde (maior tempo, em segundos) fica salvo
arquivo_recorde = 'recorde.txt'

# os 3 carros que o jogador pode escolher na tela inicial (chaves do dicionario assets)
# para trocar um carro, e so trocar o nome aqui
carros_jogador = ["mustang", "ferrari", "carroca"]

# estados DENTRO do jogo (usados no game_screen)
FIM = 0
JOGANDO = 1
EXPLODINDO = 2

# estados das TELAS (usados no main.py, o gerente)
TELA_INICIAL = 0
TELA_JOGO = 1
TELA_FIM = 2
SAIR = 3


#definindo as dimensoes da pista em si 

pista_esquerda = 152 
pista_direita  = 550 

