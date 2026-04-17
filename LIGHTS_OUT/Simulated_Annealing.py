import random
import math
import time
from base import LightsOut, Contador

def heuristica(estado):
    #Conta quantas luzes estão acesas
    #Menos luzes acesas , mais próximo do objetivo
    return sum(estado)


def simulated_annealing(problema, temp_inicio=1000, alpha=0.95, temp_minima=0.001, limite_iteracoes=10000):
    contador = Contador()

    # Estado inicial
    estado_atual = problema.estado_inicial
    melhor_estado = estado_atual

    T = temp_inicio
    iteracoes = 0

    inicio = time.time()

    while T > temp_minima and iteracoes < limite_iteracoes:
        contador.soma()

        if problema.teste_objetivo(estado_atual):
            break

        # Escolhe uma ação aleatória (vizinho)
        acao = random.choice(problema.acoes(estado_atual))
        proximo_estado = problema.resultado(estado_atual, acao)

        # Calcula diferença de custo (heurística)
        delta = heuristica(proximo_estado) - heuristica(estado_atual)

        
        if delta < 0:
            estado_atual = proximo_estado

            if heuristica(estado_atual) < heuristica(melhor_estado):
                melhor_estado = estado_atual

        else:
            # Aceita com probabilidade
            probabilidade = math.exp(-delta / T)
            if random.random() < probabilidade:
                estado_atual = proximo_estado

        # Resfriamento
        T *= alpha
        iteracoes += 1

    fim = time.time()

    return {
        "estado_final": melhor_estado,
        "heuristica": heuristica(melhor_estado),
        "iteracoes": iteracoes,
        "nos_visitados": contador.contador,
        "tempo": fim - inicio
    }

#main
if __name__ == "__main__":
    t = time.time()
    print(" --Lights Out-- ")

    problema = LightsOut(20, 20)

    resultado = simulated_annealing(problema)

    print(f"Número de células: {problema.tam}")
    print(f"Estado final: {resultado['estado_final']}")
    print(f"Luzes acesas (heurística): {resultado['heuristica']}")
    print(f"Nós visitados: {resultado['nos_visitados']}")
    print(f"Iterações: {resultado['iteracoes']}")
    print(f"Tempo de execução: {resultado['tempo']:.4f}")