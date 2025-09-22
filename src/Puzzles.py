import os
import json
import random

class PuzzleSQL:
    def __init__(self, pergunta, query_correta, resposta_esperada):
        self.pergunta = pergunta
        self.query_correta = query_correta
        self.resposta_esperada = resposta_esperada
        self.resolvido = False

    def carregar_puzzles(caminho_json):
        with open(caminho_json, 'r', encoding="utf-8") as arquivo:
            puzzles = json.load(arquivo)
        return puzzles

    def escolher_puzzle(dificuldade):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(base_dir, "perguntas", f"perguntas_{dificuldade}.json")
        puzzles = PuzzleSQL.carregar_puzzles(caminho)
        return random.choice(puzzles)

    def validar_resposta(resposta_jogador, resposta_esperada):
    
        resposta_lista = [x.strip().lower() for x in resposta_jogador.split(",") if x.strip()]

        if resposta_esperada and isinstance(resposta_esperada[0], list):
            esperado_flat = [str(item[0]).strip().lower() for item in resposta_esperada if item]
        else:
            esperado_flat = [str(x).strip().lower() for x in resposta_esperada]

        return sorted(resposta_lista) == sorted(esperado_flat)
