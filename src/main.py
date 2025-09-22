import os
from Sala import Sala
from Jogo import Jogo

# Caminho da pasta "salas" relativo a este arquivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_SALAS = os.path.join(BASE_DIR, "salas")

salas = Sala.carregar_todas_salas(PASTA_SALAS)
jogo = Jogo(salas)
jogo.jogar()