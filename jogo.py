"""
Esse arquivo trata-se do jogo onde o usuário tentará adivinhar
a palavra com base no tema escolhido.
"""

import temas
import random

# essa funcao sorteia a palavra que o usuario devera adivinhar
def sortear_palavra(tema):
    palavra = temas.palavras[tema][(random.randrange(1, len(temas.palavras[tema]), 1)) - 1]

    informar_usuario(palavra)

"""
essa funcao informa quantas letras tem a palavra e numero de chances

o numero de chances é definido com base no seguinte calculo:

caso o tamanho da palavra seja ímpar, o numero de chances será o (tamanho + 1) /2
caso o tamanho da palavra seja par, o numero de chances será o tamanho /2 
"""
def informar_usuario(palavra):
    print("\n====================")
    print("INFORMAÇÕES")
    print("====================\n")
    print(f"Tamanho da palavra: {len(palavra)}")

    if len(palavra) % 2 != 0:
        chances = int((len(palavra) + 1) / 2)
    else:
        chances = int(len(palavra) / 2)

    print(f"Número de chances: {chances}\n")

    jogar(palavra, chances)

def jogar(palavra, chances):

    letras_usuario = [] # letras acertadas pelo usuário
    ganhou = False # variavel que informa se o usuário ganhou

    while True:
        tentativa = input("Adivinhe uma letra: ")
        letras_usuario.append(tentativa.lower())
        print("")
        if tentativa.lower() not in palavra.lower():
            chances -= 1
            print("Letra errada! Perdeu uma chance...")
        for letra in palavra:
            if letra.lower() in letras_usuario:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print(f"\nVocê tem {chances} chances\n")

        ganhou = True

        for letra in palavra:
            if letra.lower() not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f"Você ganhou, parabéns!!!! A palavra é {palavra}")
    else:
        print(f"Você perdeu! A palavra é {palavra}")

