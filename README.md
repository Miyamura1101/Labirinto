# Labirinto SQL - Jogo Educativo de Detetive

Um jogo educativo em Python para ensinar lógica e resolução de problemas estilo SQL, usando uma narrativa de detetive. O objetivo é explorar salas, resolver enigmas e coletar chaves para finalmente abrir a saída da mansão.

---

## 🎯 Objetivo do Jogo

- Comece dentro de uma mansão, representada por uma matriz de salas (`.txt`).  
- Cada sala possui enigmas (`E`) que representam puzzles de detetive.  
- Ao resolver um enigma, você coleta uma chave e a posição do enigma se transforma em uma porta liberada (`L`).  
- Algumas portas (`L`) conectam diferentes salas, criando caminhos bifurcados.  
- O objetivo final é coletar **3 chaves** para abrir a saída (`X`) e concluir o jogo.  

---

## 📦 Pré-requisitos / Instalação

1. **Python 3.9+** (recomendado)  
2. Instale dependências via pip:

```bash
pip install colorama
```
# 🕹 Como Jogar
1. Abra o terminal e execute - python src/main.py

2. Use as teclas para mover o personagem:

| Tecla | Movimento |
| ----- | --------- |
| `w`   | Cima      |
| `s`   | Baixo     |
| `a`   | Esquerda  |
| `d`   | Direita   |

3. Símbolos do jogo:

| Símbolo | Significado                                      |
| ------- | ------------------------------------------------ |
| `P`     | Posição inicial do jogador                       |
| `E`     | Enigma / puzzle detetive                         |
| `L`     | Porta liberada / enigma resolvido                |
| `K`     | Chave coletada (opcional, pode marcar extras)    |
| `D`     | Dicas disponíveis na sala                        |
| `X`     | Saída da mansão (requer 3 chaves para abrir)     |
| `#`     | Parede / espaço bloqueado                        |
| `.`     | Caminho livre para andar                         |


4. Quando você entra em um 'E':

- Será apresentada uma pergunta estilo detetive, por exemplo:

- "O roubo aconteceu no Museu no dia 2025-09-10. Descubra quem estava no Museu nesse dia."

- Digite a resposta correta (nomes separados por vírgula).

- Ao acertar, a posição se transforma em 'L' e você coleta uma chave.

- Algumas portas liberadas (L) podem transportar você para outra sala.

5. Para abrir a saída (X):
- É necessário coletar 3 chaves.
- Ao tentar passar por X sem as 3 chaves, você será impedido.
