class Grafo:
    def __init__(self):
        self.grafo_set = {}
        self.arestas = []

    def _add_aresta_set(self, origem, destino, custo):
        if not self.grafo_set.get(origem):
            self.grafo_set[origem] = []
        self.grafo_set[origem].append((destino, custo))
    
    def _add_aresta_list(self, aresta: tuple):
        """
        Adiciona as arestas ordenadas em uma lista para depois aplicar no algoritmo de Kruskal
        """
        indice = 0
        while indice < len(self.arestas) and self.arestas[indice][2] < aresta[2]:
            indice += 1

        # Insere na posição encontrada
        self.arestas.insert(indice, aresta)

    def add_aresta(self, origem, destino, custo: int) -> None:
        self._add_aresta_list((origem, destino, custo))

        # Como o grafo é bidirecional adiciona a aresta a-b e b-a
        self._add_aresta_set(origem, destino, custo)
        self._add_aresta_set(destino, origem, custo)
    
    def print(self):
        print(self.grafo_set)


    def is_ciclo(self, grupos, u, v) -> bool:
        # Verifica se forma um ciclo a partir do agrupamento dos vertices.
        # se eles estão no mesmo grupo forma um ciclo

        raiz_u = grupos[u]
        raiz_v = grupos[v]
        if raiz_u == raiz_v:
            return True  # Forma ciclo

        grupos[raiz_v] = raiz_u
        return False

    def kruscal(self):
        """
        1. Ordenar as arestas por peso.
        2. Inicialize a arvore como vazia.
        3. para cada aresta (u, v) em ordem crescente:
            a. Se adicionando (u, v) à arvore não forma ciclo
                i. Adicione (u, v) à arvore.
        4. Retorne a arvore.
        """
         
        arvore = Grafo()
        grupos = {vertice: vertice for vertice in self.grafo_set.keys()}
        num_vertices = len(grupos)
        num_arestas = 0
        custo_arvore = 0

        for aresta in self.arestas:
            u, v, custo = aresta

            # Se não gerar ciclo, adiciona a aresta na arvore
            if not self.is_ciclo(grupos, u, v):
                arvore.add_aresta(u, v, custo)
                num_arestas += 1
                custo_arvore += custo

            # Verifica se a arvore já está conectada
            if num_arestas == num_vertices - 1:
                break
        
        return arvore, custo_arvore

# Grafo de exemplo:
#    B - 4 - C 
#  /1 \      | 6\
# A     5    2   D
#  \3      \ | 2/
#    E - 2 - F

g = Grafo()
g.add_aresta("A", "B", 1)
g.add_aresta("A", "E", 3)
g.add_aresta("E", "F", 2)
g.add_aresta("B", "C", 4)
g.add_aresta("B", "F", 5)
g.add_aresta("C", "F", 2)
g.add_aresta("C", "D", 6)
g.add_aresta("F", "D", 2)

print("Grafo:")
g.print()

arvore, custo = g.kruscal()
print("Arvore geradora minima:")
arvore.print()
print("Custo:", custo)