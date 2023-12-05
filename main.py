"""
arquivo para iniciar o jogo
"""

import menu as mn

# verifica se o usuario deseja jogar novamente
def jogar_novamente():
    while True:
        jogar_novamente = input("\nDeseja jogar novamente (S/N)? ")
        if jogar_novamente.upper() == "S" or jogar_novamente.upper() == "N":
            if jogar_novamente.upper() == "S":
                print("")
                return 1
            else:
                return 0
        else:
            print("Ops, opção inválida! Digite novamente...")

if __name__ == "__main__":
    mn.exibir_menu()

    while True:
        if jogar_novamente() == 1:
            mn.exibir_menu()
        else:
            break