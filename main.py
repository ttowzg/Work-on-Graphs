from grafo_imagem import GrafoImagem
from dijkstra import Dijkstra

# Caminho para a imagem BMP
caminho_imagem = "0_floor.bmp"

# Criar instância da classe GrafoImagem
grafo_imagem = GrafoImagem(caminho_imagem)

# Mapear o grafo a partir da imagem (ignorando pixels pretos)
grafo_imagem.mapear_grafo()

# Escolher nós de origem e destino dentro dos limites da imagem
origem = (391, 283)
destino = (381, 357)

# Criar instância da classe Dijkstra
dijkstra = Dijkstra(grafo_imagem.grafo)

# Calcular caminho mínimo usando Dijkstra
caminho_minimo = dijkstra.calcular_caminho_minimo(origem, destino)

# Exibir o caminho mínimo
if caminho_minimo:
    print(f"Caminho mínimo de {origem} para {destino}: {caminho_minimo}")
else:
    print(f"Não há caminho possível de {origem} para {destino}")
