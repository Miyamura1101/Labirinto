import os
from Sala import Sala
from Jogo import Jogo
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_SALAS = os.path.join(BASE_DIR, "salas")

salas = Sala.carregar_todas_salas(PASTA_SALAS)

jogo = Jogo(salas)
jogo.jogar()

# jogo = Jogo(salas, tamanho=TAMANHO, cores=cores)

# if __name__ == "__main__":
#     jogo.jogar_pygame()