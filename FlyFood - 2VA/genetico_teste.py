# -*- coding: utf-8 -*-
from random import randint
import random, time
from sklearn.utils import shuffle
from itertools import permutations


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

def populacao_inicial(pontos_food, pop_tamanho):
    populacao = []
    permutation = shuffle(list(permutations(pontos_food)))
    for i in range(pop_tamanho):
        populacao.append(list(permutation[i]))
    return populacao


def rank_rota(population):
    population.sort(key=lambda x: x[0])
    return population

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

def mutation(rota):
    if random.random() < 0.05:
        ponto_mutacao = randint(0, len(rota)-2)
        backup = rota[ponto_mutacao]
        rota[ponto_mutacao] = rota[ponto_mutacao+1]
        rota[ponto_mutacao+1] = backup
        return rota

def algoritmo_genetico(coordenadas, pop_tamanho, numero_geracao=10):
    populacao = [i for i in coordenadas.keys() if i!= 'R']
    p = populacao_inicial(populacao, pop_tamanho)

    custo_baixo = float('inf')
    lc_list = []
    geracao = 0

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

if __name__ == '__main__':
    TamanhoPopulacao = 100

    inicio = time.time()

    coordenadas = gera_grafo(open('input', 'r'))
    resultado = algoritmo_genetico(coordenadas, TamanhoPopulacao)

    print('Melhor solução encontrada: {} | {}\nTempo gasto: {:.2f} segundos'.format(' '.join(resultado[0]),' '.join(resultado[1]), time.time()-inicio))

    