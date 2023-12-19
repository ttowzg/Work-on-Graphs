import heapq


class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def calcular_caminho_minimo(self, origem, destino):
        heap = [(0, origem, [])]
        visitados = set()

        while heap:
            (custo, no_atual, caminho) = heapq.heappop(heap)

            if no_atual not in visitados:
                visitados.add(no_atual)
                caminho = caminho + [no_atual]

                if no_atual == destino:
                    return caminho

                for vizinho in self.grafo[no_atual]:
                    if vizinho not in visitados:
                        heapq.heappush(heap, (custo + 1, vizinho, caminho))
        return None
