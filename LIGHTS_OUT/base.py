 
 
class LightsOut:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.tam = linhas * colunas
        self.estado_inicial = tuple([1] * self.tam)  # tudo aceso
        self.estado_objetivo = tuple([0] * self.tam)  # tudo apagado
    
    def acoes(self, estado):
        # Retorna todas as posições possíveis (i, j) como ações
        return [(i, j) for i in range(self.linhas) for j in range(self.colunas)]
 
    def resultado(self, estado, acao):
        i, j = acao
        # Converte a tupla 1D em matriz 2D mutável
        novo = [list(estado[r * self.colunas:(r + 1) * self.colunas]) for r in range(self.linhas)]
 
        direcoes = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
 
        for di, dj in direcoes:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.linhas and 0 <= nj < self.colunas:
                novo[ni][nj] ^= 1
 
        # Retorna como tupla 1D
        return tuple(c for row in novo for c in row)
 
    def teste_objetivo(self, estado):
        return estado == self.estado_objetivo
 
    def custo_passo(self, estado, acao):
        return 1
    
#conta o numero de nós que o algoritmo visita 
class Contador:
    def __init__(self):
        self.contador = 0
 
    def soma(self):
        self.contador += 1