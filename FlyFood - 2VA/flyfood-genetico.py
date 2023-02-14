# -*- coding: utf-8 -*-
# geram aleatoriamente um número inteiro dentro de um intervalo.
from random import randint
# gera ou manipula dados aleatoriamente.
import random, time
# aleatorizar a ordem
from sklearn.utils import shuffle
# Utilizado para gerar todas as possíveis permutações.
from itertools import permutations


# função que lê o arquivo input e transforma ele num dicionário, onde as chaves são as letras..
# ... e os valores de cada chave é a linha e coluna da matriz;
def gera_grafo(file):
    points = {}
    i, j =  map(int, file.readline().split(' '))
    for l in range(i):
        line = file.readline().split(' ')
        if len(line)==j:
            for colun in range(len(line)):
                if line[colun].find("\n")!= -1:
                    line[colun] = line[colun][-2]
                if line[colun] not in '0' :
                    points[line[colun]] = (l, colun)
    return points

# a função abaixo gera a população inicial. Recebendo o tamanho da população desejada e recebe também..
# ... as chaves do dicionário - pontos de entrega - por meio da permutação;
def populacao_inicial(pontos_food, pop_tamanho):
    populacao = []
    permutation = shuffle(list(permutations(pontos_food)))
    for i in range(pop_tamanho):
        populacao.append(list(permutation[i]))
    return populacao

# a função lambda abaixo faz apenas um sorteio na permutação;
def rank_rota(population):
    population.sort(key=lambda x: x[0])
    return population


# a função abaixo pega a lista de chaves do dicionário e adiciona R. Após, uso o metódo abs que retorna..
# ... o valor absoluto das coordenadas com o dicionário completo e com a rota dentro de um while. 
# Por fim, deleto a rota inicial e a final.
# O custo da rota é feito por meio da distância cartesiana;
def fitness_rota(coordenadas, rota):
    c = 0
    rota_custo = 0
    rota.append('R')
    rota.insert(0, 'R')

    while c < len(rota)-1:
        rota_custo += abs(coordenadas[rota[c]][1] - coordenadas[rota[c+1]][1]) + abs(coordenadas[rota[c]][0] - coordenadas[rota[c+1]][0])
        c += 1

    del(rota[0], rota[-1])
    return rota_custo

# a função abaixo faz a seleção por torneio do modelo mais adptável. Recebe o dicionário, também uma lista de
# populações das várias permutações que fizemos acima e retorna a melhor permutação. Sendo o que possui o 
# o menor percurso; 
def selection(coordenadas, populacao, m, k):
    melho_adap = []
    torneio = []
    for i in range(m):
        participantes = random.sample(populacao, k)
        for j in participantes:
            torneio.append((fitness_rota(coordenadas, j), j))
        campeao = rank_rota(torneio)[0][1]
        melho_adap.append(campeao)
    return melho_adap

# abaixo na função pegamos duas permutações partimos ao meio e depois juntamos os dois pedaços novamente.
# 
def crossover(parent1, parent2):  #PMX
    interrupcao = randint(1, len(parent1)-1)
    backup = parent2[:]
    filhos = []
    for filho in range(2):
        for point in range(interrupcao):
            if parent1[point] != parent2[point]:
                temp = parent2[point]
                parent2[point] = parent1[point]
                for ponto_mudanca in range(point+1, len(parent2)):
                    if parent2[point] == parent2[ponto_mudanca]:
                        parent2[ponto_mudanca] = temp
                        break
        filhos.append(parent2)
        parent2 = parent1
        parent1 = backup
    return filhos  

# A função abaixo recebe uma sequencia das chaves permutada e troca a posição 
def mutation(rota):
    if random.random() < 0.05:
        ponto_mutacao = randint(0, len(rota)-2)
        backup = rota[ponto_mutacao]
        rota[ponto_mutacao] = rota[ponto_mutacao+1]
        rota[ponto_mutacao+1] = backup
        return rota

# Na última função criei uma lista chamada população removendo o R e crio a população com a populacao inicial.
# Abaixo crei uma variável custo, que contém o custo mais baixo

def algoritmo_genetico(coordenadas, pop_tamanho, numero_geracao=10):
    populacao = [i for i in coordenadas.keys() if i!= 'R']
    p = populacao_inicial(populacao, pop_tamanho)

    custo_baixo = float('inf')
    lc_list = []
    geracao = 0
    # pegará sempre os 20 melhores
    while geracao < numero_geracao:
        s = selection(coordenadas, p, 20, 5)
        p = []
        for k in range(50):
            p1 = random.choice(s)
            p2 = random.choice(s)
            f1, f2 = crossover(p1, p2)
            mutation(f1)
            mutation(f2)
            p.append(f1)
            p.append(f2)

        geracao+=1
        solucao = selection(coordenadas, p, 1, 100)[0]

        if fitness_rota(coordenadas, solucao) < custo_baixo:
            custo_baixo = fitness_rota(coordenadas, solucao)
            lc_list.append(str(custo_baixo))

    return solucao, lc_list

# no metódo main onde digo o tamanho da população
if __name__ == '__main__':
    TamanhoPopulacao = 100

    inicio = time.time()

    coordenadas = gera_grafo(open('input', 'r'))
    resultado = algoritmo_genetico(coordenadas, TamanhoPopulacao)

    print('Melhor solução encontrada: {} \nTempo gasto: {:.2f} segundos'.format(' '.join(resultado[0]), time.time()-inicio))


###### OBSERVAÇÕES DO ALGORITMO ######
# Seleção por torneio;
# Critério de parada = atingir 10 gerações;
# A cada geração os 20 melhores serão pegos;
# Taxa do crossover = 0.05
# Tem uma coisa ruim no algoritmo genético, ele não é determinístico então sempre dará um valor diferente..
# ... se ele fosse estocástico sempre daria o mesmo valor;
# "Dois pontos de corte são selecionados aleatoriamente em ambas estruturas dos cromossomos pais, em seguida a 
# sequência de genes delimitada em um cromossomo pai é mapeando para o outro cromossomo formando um cromossomo 
# descendente";
# tamanho da população = 100.
