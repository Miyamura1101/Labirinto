import os

class Sala:
    def __init__(self, nome, grid):
        self.nome = nome
        self.grid = grid  # matriz (lista de listas de chars)
        self.linhas = len(grid)
        self.colunas = len(grid[0])
        self.posicao_jogador = self.encontrar('P')
        self.enigmas = self.encontrar_todos('E')
        self.dicas = self.encontrar_todos('D')
        self.chaves = self.encontrar_todos('K')

    def encontrar(self, simbolo):
        """Retorna a primeira posição (linha, coluna) de um símbolo"""
        for i, linha in enumerate(self.grid):
            for j, celula in enumerate(linha):
                if celula == simbolo:
                    return (i, j)
        return None

    def encontrar_todos(self, simbolo):
        """Retorna todas as posições de um símbolo"""
        posicoes = []
        for i, linha in enumerate(self.grid):
            for j, celula in enumerate(linha):
                if celula == simbolo:
                    posicoes.append((i, j))
        return posicoes
    
    def mostrar(self):  
        for linha in self.grid:
            print("".join(linha))
    
    def carregar_sala(caminho_arquivo):
        """Carrega uma sala a partir de um arquivo .txt"""
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = [list(linha.strip()) for linha in arquivo.readlines()]
        return Sala(os.path.basename(caminho_arquivo), linhas)

    def carregar_todas_salas(pasta="salas"):
        """Carrega todas as salas de uma pasta"""
        salas = []
        for nome_arquivo in sorted(os.listdir(pasta)):
            if nome_arquivo.endswith(".txt"):
                caminho = os.path.join(pasta, nome_arquivo)
                sala = Sala.carregar_sala(caminho)
                salas.append(sala)
        return salas