from base import LightsOut, Contador
from collections import deque # implementa filas 
import time

#Nó de busca
class No:
    def __init__(self, estado, pai=None, acao=None, custo=0):
        self.estado = estado
        self.pai   = pai
        self.acao  = acao
        self.custo = custo
 
    def caminho(self):
        nos, no = [], self
        while no.pai is not None:
            nos.append(no.acao)
            no = no.pai
        nos.reverse()
        return nos
    
#BFS (Busca em largura)
def bfs(problema: LightsOut, contador: Contador = None):

    if contador is None:
        contador = Contador()
 
    no_inicial = No(problema.estado_inicial)
 
    # Estado inicial é Objetivo ? 
    if problema.teste_objetivo(no_inicial.estado):
        return no_inicial
 
    fronteira = deque([no_inicial]) # fila         
    explorados = {no_inicial.estado}  # nós visitados       
    while fronteira:
        no_atual = fronteira.popleft()
        contador.soma()
 
        for acao in problema.acoes(no_atual.estado):
            novo_estado = problema.resultado(no_atual.estado, acao)
 
            if novo_estado in explorados:
                continue
 
            filho = No(
                estado=novo_estado,
                pai=no_atual,
                acao=acao,
                custo=no_atual.custo + problema.custo_passo(no_atual.estado, acao),
            )
 
            if problema.teste_objetivo(filho.estado):
                return filho
 
            explorados.add(novo_estado)
            fronteira.append(filho)
 
    return None  # sem solução
 
#main 
if __name__ == "__main__":
    t = time.time()
    print(" --Lights Out-- ")
    problema = LightsOut(4, 4)
    tam = problema.tam
    contador = Contador() 
    solucao = bfs(problema, contador)
 
    if solucao:
        
        acoes = solucao.caminho()
        print(f"Numero de células: {tam}")
        print(f"Quantidade de passo para solução {len(acoes)} .")
        print(f"Nós visitados: {contador.contador}")
        print(f"Ações realizadas entre linha e coluna {acoes}")
        print(f"Tempo de execução : {time.time()-t:.4f}")
        
    else:
        print("Sem solução.")
        print(f"Tempo de execução : {time.time()-t:.4f}")
    

   