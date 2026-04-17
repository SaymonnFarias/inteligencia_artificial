import heapq
from base import LightsOut, Contador
import time

def heuristica(estado):
    #Conta quantas luzes estão acesas
    #Menos luzes acesas , mais próximo do objetivo
    return sum(estado)


def busca_gulosa(problema, contador):
    fronteira = []
    heapq.heappush(fronteira, (heuristica(problema.estado_inicial), problema.estado_inicial, []))

    explorados = set()

    while fronteira:
        h, estado, caminho = heapq.heappop(fronteira)

        contador.soma()

        if problema.teste_objetivo(estado):
            return caminho

        if estado in explorados:
            continue

        explorados.add(estado)

        for acao in problema.acoes(estado):
            novo_estado = problema.resultado(estado, acao)

            if novo_estado not in explorados:
                novo_caminho = caminho + [acao]
                heapq.heappush(
                    fronteira,
                    (heuristica(novo_estado), novo_estado, novo_caminho)
                )

    return None


# main
if __name__ == "__main__":
    t = time.time()
    print(" --Lights Out-- ")

    problema = LightsOut(4, 4)
    contador = Contador()

    solucao = busca_gulosa(problema, contador)

    if solucao:
        
        print(f"Número de células: {problema.tam}")
        print(f"Quantidade de passos para solução: {len(solucao)}")
        print(f"Nós visitados: {contador.contador}")
        print(f"Ações (linha, coluna): {solucao}")
        print(f"Tempo de execução: {time.time()-t:.4f}")
       
    else:
        print("Sem solução.")
        print(f"Tempo de execução: {time.time()-t:.4f}")