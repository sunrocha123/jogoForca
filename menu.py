"""
Esse arquivo trata-se do MENU do jogo, onde o usuário pode selecionar o tema para que o programa sorteie
uma palavra para que possa adivinhar
"""

import jogo

def exibir_menu():
    print("============================")
    print("JOGO DA FORCA")
    print("============================\n")
    print("SELECIONE O TEMA:\n")
    temas = ["Estações do ano", "Meses do ano", "Animais", "Países Europeus", "Times brasileiros de futebol"]
    for palavra in temas:
        print(str(temas.index(palavra) + 1) + ". " + palavra)
    print("")

    selecionar_tema()

def selecionar_tema():
    while True:
        try:
            opcao_escolhida = int(input("Digite a opção escolhida: "))
        except ValueError:
            # mensagem caso o usuário digite algo diferente de um número
            print("Ops, opção inválida! Digite o número do tema :)\n")
        else:
            # verificar se o numero informado está dentro do range de 1 a 5
            if opcao_escolhida >= 1 and opcao_escolhida <= 5:
                if opcao_escolhida == 1:
                    tema = "estacoes_do_ano"
                elif opcao_escolhida == 2:
                    tema = "meses"
                elif opcao_escolhida == 3:
                    tema = "animais"
                elif opcao_escolhida == 4:
                    tema = "paises_europeus"
                else:
                    tema = "times_brasileiros"
                jogo.sortear_palavra(tema)
                break
            else:
                print("Ops, opção inválida! Digite novamente...")