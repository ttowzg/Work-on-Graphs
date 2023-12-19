from PIL import Image


class GrafoImagem:
    def __init__(self, caminho_imagem):
        self.imagem = Image.open(caminho_imagem)
        self.largura, self.altura = self.imagem.size
        self.grafo = {}

    def mapear_grafo(self):
        for x in range(self.largura):
            for y in range(self.altura):
                cor_pixel = self.imagem.getpixel((x, y))

                # Verifica se o pixel não é preto
                if cor_pixel != (0, 0, 0):
                    no = (x, y)
                    vizinhos = []

                    # Adiciona arestas para nós vizinhos (movimentos em todas as direções)
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue  # Ignora o próprio nó
                            novo_x, novo_y = x + dx, y + dy
                            if 0 <= novo_x < self.largura and 0 <= novo_y < self.altura:
                                novo_cor_pixel = self.imagem.getpixel(
                                    (novo_x, novo_y))

                                # Verifica se o pixel vizinho não é preto
                                if novo_cor_pixel != (0, 0, 0):
                                    vizinhos.append((novo_x, novo_y))

                    self.grafo[no] = vizinhos
