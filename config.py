#declaracao de variaveis 

altura  = 900
largura = 700
FPS = 30 

altura_carro = 80
largura_carro = 50

velocidade_carro = 5
aceleracao_carro = 10

intervalo_tempo1 = 800
intervalo_tempo2 = 2000

# dificuldade: a cada tempo_entre_aumentos ms o jogo fica mais dificil
tempo_entre_aumentos = 5000   # de quanto em quanto tempo aumenta (ms)
aumento_velocidade = 1        # quanto a velocidade dos obstaculos sobe a cada aumento
reducao_intervalo = 100       # quanto o intervalo entre obstaculos diminui a cada aumento (ms)
intervalo_minimo = 300        # o intervalo nunca fica menor que isso (ms)

vidas_iniciais = 2

# cores
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

DONE = 0
PLAYING = 1
EXPLODING = 2


#definindo as dimensoes da pista em si 

pista_esquerda = 152 
pista_direita  = 550 


largura_pista = (pista_direita - pista_esquerda)/5