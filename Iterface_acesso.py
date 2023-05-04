import cadastro

import os

# Pagina inicial

opcao = 0
while(opcao != 3):
    print("--------Biblioteca----------")
    print("Opções")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair do Sistema")

    opcao = int(input("Digite a opção: "))
    os.system('cls||clear')
    if opcao == 1:
        cadastro.cadastrar()
        print("Cadastrado com sucesso")
    elif opcao == 2:
        cadastro.login()
    elif opcao == 3:
        print("Até a próxima!")
    else:
        print("Digite uma opção válida")

