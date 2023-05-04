import livro
import os


def opc_usuario():
    opcao = 0
    while opcao != 7:
        print("------Biblioteca------")
        print("1 - Cadastrar Livro")
        print("2 - Listar Livro")
        print("3 - Editar Livros")
        print("4 - Excluir Livro")
        print("5 - Locar Livro")
        print("6 - Devolução do Livro")        
        print("7 - Sair\n")
    
        opcao = int(input ("Digite a opção desejada: "))
        os.system('cls||clear')
        if opcao == 1:
            livro.cadastrar_livro()
            print ("Cadastrado com Sucesso!")
        elif opcao == 2:
            livro.listar_livros()
        elif opcao == 3:
            livro.editar_livro()
        elif opcao == 4:
            livro.excluir_livro()
        elif opcao == 5:
            livro.alugar_livro()
        elif opcao == 6:
            livro.devolver_livro
        elif opcao == 7:
            print("Deslogado")
        else:
            print("Digite uma opção válida")