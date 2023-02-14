# Importação do mmódulo time
import time
# Função que calcula a distância entre dois pontos a e b
def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Funcão que calcula e retorna todas as permutações da lista
def perm(lista):
    # Se a lista estiver vazia, retorna lista vazia
    if len(lista) == 0:
        return []

    # Se só houver um ponto, retorna lista com esta única permutação trivial
    if len(lista) == 1:
        return [lista]
    
    # Lista vazia para as permutacoes
    permutacoes = [] # lista vazia que armazenará a permutação atual
  
    # Repete para cada elemento da lista: vamos calcular as permutações que
    # iniciam com o elemento i
    for i in range(len(lista)):
        # Escolhe o primeiro elemento
        primeiro = lista[i]

        # Determina a lista com o restante dos elementos
        restante = lista[:i] + lista[i+1:]

        # Gera as permutações com o primeiro elemento escolhido, fazendo a
        # permutação nos elementos restantes
        for p in perm(restante):
            permutacoes.append([primeiro] + p)

    return permutacoes



# Função que calcula a distância do trajeto
def calc_trajeto(trajeto, restaurante):
    # Distancia do restaurante ao primeiro ponto
    distancia = dist(restaurante, trajeto[0])

    # Soma distância entre os pontos
    for i in range(len(trajeto)-1):
        distancia += dist(trajeto[i], trajeto[i+1])

    # Retorna a soma com a distância do ultimo ponto ao restaurante
    return distancia + dist(trajeto[-1], restaurante)
inicio = time.perf_counter()


# Abre arquivo
arquivo = open("input.txt", mode="r")

# Le dimensões do mapa
dim = arquivo.readline().split()

# Converte para int
lin = int(dim[0])
col = int(dim[1])

mapa = [] # Inicializa o mapa como lista vazia


# Le linhas do arquivo
for i in range(lin):
    mapa.append(arquivo.readline().split())

restaurante = [0,0,0]
pontos = []


# Encontra o restaurante e os pontos de entrega no mapa
for i in range(lin):
    for j in range(col):
        if mapa[i][j] == 'R':
            restaurante = [i, j, mapa[i][j]]
        elif mapa[i][j] != '0':
            pontos.append([i, j, mapa[i][j]])


# Determina todos os possíveis trajetos
trajetos = perm(pontos)

# Determina um trajeto mínimo inicial
minimo = calc_trajeto(pontos, restaurante)
trajeto_minimo = pontos

# Entre todos os trajetos, determina o trajeto de distância minima
for trajeto in trajetos:
    if calc_trajeto(trajeto, restaurante) < minimo :
        minimo = calc_trajeto(trajeto, restaurante)
        trajeto_minimo = trajeto


# Concatena pontos na rota
rota = ""
for ponto in trajeto_minimo:
    rota += ponto[2] + " "


# Imprime a resposta
print(rota)
print(minimo)

# Imprime o valor flutuante de tempo de um contador de desempenho
fim = time.perf_counter()
print(f'Tempo gasto: {fim-inicio :.2f} segundos')

