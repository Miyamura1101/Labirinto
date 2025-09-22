import os
import random
from Puzzles import PuzzleSQL
from Sala import Sala


class Jogo:
    def __init__(self, salas):
        self.salas = salas
        self.sala_atual = salas[0]  # Começa na sala 01
        self.jogador_pos = self.sala_atual.posicao_jogador
        self.chaves_coletadas = 0

    def processar_enigma(self):
        if self.chaves_coletadas == 0:
            dificuldade = "faceis"
        elif self.chaves_coletadas == 1:
            dificuldade = "medias"
        else:
            dificuldade = "dificeis"

        puzzle = PuzzleSQL.escolher_puzzle(dificuldade)

        print("\n=== ENIGMA SQL ===")
        print(puzzle["pergunta"])

        resposta_jogador = input("Digite sua resposta (separe itens por vírgula):\n> ")

        correto = PuzzleSQL.validar_resposta(resposta_jogador, puzzle["resposta_esperada"])
        if correto:
            mensagem = "✅ Enigma resolvido!"
  
            i_atual, j_atual = self.jogador_pos
            self.sala_atual.grid[i_atual][j_atual] = 'L'
        
            outras_posicoes = []
            for sala in self.salas:
                if sala != self.sala_atual:
                    for pos in sala.enigmas:
                        i, j = pos
                        if sala.grid[i][j] == 'E':
                            outras_posicoes.append((sala, pos))
            
            if outras_posicoes:
                nova_sala, nova_pos = random.choice(outras_posicoes)
                i_nova, j_nova = nova_pos

                sala_antiga = self.sala_atual
                sala_antiga.portas[(i_atual, j_atual)] = (nova_sala, (i_nova, j_nova))

                self.sala_atual = nova_sala
                self.jogador_pos = nova_pos

                nova_sala.portas[(i_nova, j_nova)] = (sala_antiga, (i_atual, j_atual))
                
                # Marca a posição de destino como 'L'
                self.sala_atual.grid[i_nova][j_nova] = 'L'
    
                mensagem += " Você se moveu para outra pista na sala e a porta foi liberada!"
            return mensagem
        else:
            return "❌ Resposta incorreta."

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
            input(self.processar_enigma())
        elif celula == "D":
            return "Você encontrou uma DICA!"
        elif celula == "K":
            self.chaves_coletadas += 1
            # marca a chave como coletada
            self.sala_atual.grid[i][j] = "."
            return f"Você coletou uma CHAVE! Total = {self.chaves_coletadas}"
        elif celula == "L":
            destino = self.sala_atual.portas.get((i, j))
            if destino:
                sala_destino, pos_destino = destino
                self.sala_atual = sala_destino
                self.jogador_pos = pos_destino
                return f"🚪 Você entrou na sala {sala_destino.nome}!"
            else:
                return "Esta porta ainda está trancada. Resolva um enigma para liberá-la."
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