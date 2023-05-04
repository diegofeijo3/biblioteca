#Cadastro de Usuario

import tela_usuario


cadastro = {}

#Cadastro
def cadastrar():
    print("Cadastro\n")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input ("Digite sua senha: ")
    cadastro[email] = {'nome' : nome, 'senha' : senha}

#Login do usuario cadastrado
def login():
    print("Login\n")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    if email in cadastro and senha == cadastro[email]['senha']:
        print("Logado com sucesso!")
        print("Bem Vindo", cadastro[email]['nome'])
        tela_usuario.opc_usuario()
    else:
        print("Email ou senha incorretos. Tente novamente")