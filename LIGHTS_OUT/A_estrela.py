import heapq
from base import LightsOut, Contador
import time


def heuristica(estado, problema):
    """
    Cada clique afeta no máximo 5 células, logo nunca supera o custo real,
    assim garante um bom funcionamento do A*.
    """
    luzes_acesas = sum(estado)
    return -(-luzes_acesas // 5)  


# Nó de busca
class No:
    # slots serve para eficiência de memória
    __slots__ = ("estado", "acao", "pai", "custo_g", "custo_f")

    def __init__(self, estado, acao=None, pai=None, custo_g=0, custo_h=0):
        self.estado  = estado
        self.acao    = acao
        self.pai     = pai
        self.custo_g = custo_g            
        self.custo_f = custo_g + custo_h  

    # __lt__ para desempate no heap
    def __lt__(self, outro):
        return self.custo_f < outro.custo_f


def reconstruir_caminho(no):
    acoes = []
    while no.acao is not None:
        acoes.append(no.acao)
        no = no.pai
    acoes.reverse()
    return acoes


# Implementação do A* clássico (lista fechada)
def busca_a_estrela(problema, contador=None):

    estado_inicial = problema.estado_inicial
    no_raiz = No(
        estado=estado_inicial,
        custo_g=0,
        custo_h=heuristica(estado_inicial, problema),  
    )

    # Fronteira
    fronteira = [(no_raiz.custo_f, no_raiz)]          

    # Já visitados
    explorado = {}

    while fronteira:
        _, no_atual = heapq.heappop(fronteira)

        # Teste objetivo
        if problema.teste_objetivo(no_atual.estado):
            return reconstruir_caminho(no_atual), no_atual.custo_g


        g_anterior = explorado.get(no_atual.estado)
        if g_anterior is not None and g_anterior <= no_atual.custo_g:
            continue
        explorado[no_atual.estado] = no_atual.custo_g

        if contador:
            contador.soma()

        # Expansão
        for acao in problema.acoes(no_atual.estado):
            novo_estado = problema.resultado(no_atual.estado, acao)
            novo_g      = no_atual.custo_g + problema.custo_passo(no_atual.estado, acao)

            # Poda
            g_ante = explorado.get(novo_estado)
            if g_ante is not None and g_ante <= novo_g:
                continue

            novo_h  = heuristica(novo_estado, problema)
            novo_no = No(
                estado  = novo_estado,
                acao    = acao,
                pai     = no_atual,
                custo_g = novo_g,
                custo_h = novo_h,         
            )
            heapq.heappush(fronteira, (novo_no.custo_f, novo_no))

    return None, None  # sem solução


# Main
if __name__ == "__main__":
    t = time.time()
    print("--Lights Out--")
    problema = LightsOut(4, 4)
    tam = problema.tam
    contador = Contador()

    resultado = busca_a_estrela(problema, contador)    

    acoes, custo = resultado                           

    if acoes is not None:
        print(f"Número de células : {tam}")
        print(f"Passos para a solução : {custo}") #Quantidade de passos = custo  
        print(f"Nós visitados : {contador.contador}")
        print(f"Tempo de execução : {time.time() - t:.4f}s")
    else:
        print("Sem solução.")
        print(f"Tempo de execução : {time.time() - t:.4f}s")