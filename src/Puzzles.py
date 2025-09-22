import json
import random
import sqlite3

class PuzzleSQL:
    def __init__(self, pergunta, query_correta, resposta_esperada):
        self.pergunta = pergunta
        self.query_correta = query_correta
        self.resposta_esperada = resposta_esperada
        self.resolvido = False
    