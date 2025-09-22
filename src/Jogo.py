import os 
from Sala import Sala


class Jogo:
    def __init__(self, salas):
        self.salas = salas
        self.sala_atual = salas[0]  # Começa na sala 01
        self.jogador_pos = self.sala_atual.posicao_jogador
        self.chaves_coletadas = 0

    def mostrar(self):
        """Mostra a sala atual com a posição do jogador"""
        for i, linha in enumerate(self.sala_atual.grid):
            linha_str = ""
            for j, cel in enumerate(linha):
                if (i, j) == self.jogador_pos:
                    linha_str += "P "
                else:
                    linha_str += f"{cel} "
            print(linha_str.rstrip())
        print(f"Chaves coletadas: {self.chaves_coletadas}")
    
    def mover(self, direcao):
        """Move o jogador se possível"""
        dx, dy = 0, 0
        if direcao == "w": 
            dx, dy = -1, 0
        elif direcao == "s":
            dx, dy = 1, 0
        elif direcao == "a": 
            dx, dy = 0, -1
        elif direcao == "d": 
            dx, dy = 0, 1
        else:
            return "Comando inválido!"

        nova_pos = (self.jogador_pos[0] + dx, self.jogador_pos[1] + dy)
        i, j = nova_pos

        # checagem de limites do grid
        if i < 0 or j < 0 or i >= self.sala_atual.linhas or j >= self.sala_atual.colunas:
            return "Não pode sair dos limites!"

        # impede atravessar parede
        if self.sala_atual.grid[i][j] == "#":
            return "Bateu na parede!"

        # atualiza posição
        self.jogador_pos = nova_pos
        celula = self.sala_atual.grid[i][j]

        if celula == "E":
            return "Você encontrou um ENIGMA! Resolva para prosseguir."
        elif celula == "D":
            return "Você encontrou uma DICA!"
        elif celula == "K":
            self.chaves_coletadas += 1
            # marca a chave como coletada
            self.sala_atual.grid[i][j] = "."
            return f"Você coletou uma CHAVE! Total = {self.chaves_coletadas}"
        else:
            return "Andou para um espaço vazio."
    

    def jogar(self):
        print("=== Jogo SQL ===")
        print("Movimente-se com WASD, Q para sair.")
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            self.mostrar()
            comando = input("Digite comando (w/a/s/d/q): ").lower()
            if comando == "q":
                print("Saindo do jogo...")
                break
            resultado = self.mover(comando)
            print(resultado)