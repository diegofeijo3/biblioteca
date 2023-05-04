#Tudo Relacionado aos Livros

livros = []

#Cadastro de livros
def cadastrar_livro():
    print ("----Cadastrar Livro----")
    nome_livro = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    codigo = input("Digite o código do livro: ")
    
    livro = {"nome": nome_livro, "autor": autor, "codigo": codigo, "alugado" : False}
    livros.append(livro)
    
    print("Livro cadastrado com sucesso!")

#Listar Livros cadastrados
def listar_livros():
    print("----Listar Livro----")
    if not livros:
        print("Não há livros cadastrados.")
        return
    
    print("Livros cadastrados:")
    for livro in livros:
        status = "Disponível" if not livro["alugado"] else "Alugado"
        print(f"Nome: {livro['nome']}, Autor: {livro['autor']}, Código: {livro['codigo']}, Status: {status}")

#Editar Livro cadastrado
def editar_livro():
    print("----Editar Livro----")
    codigo = input("Digite o código do livro: ")
    
    for livro in livros:
        if livro['codigo'] == codigo:
            nome_livro = input(f"Digite o novo nome para o livro '{livro['nome']}': ")
            autor = input(f"Digite o novo autor para o livro '{livro['nome']}': ")
            
            livro['nome'] = nome_livro
            livro['autor'] = autor
            
            print("Livro editado com sucesso!")
            return
    
    print("Livro não encontrado.")

#Exluir Livro
def excluir_livro():
    print("----Excluir Livro----")
    codigo = input("Digite o código do livro: ")
    
    for livro in livros:
        if livro['codigo'] == codigo:
            livros.remove(livro)
            print("Livro excluído com sucesso!")
            return
    
    print("Livro não encontrado.")

#Alugar Livro
def alugar_livro():
    print("----Alugar Livro----")
    codigo = input("Digite o código do livro a ser alugado: ")
    
    for livro in livros:
        if livro['codigo'] == codigo:
            if livro['alugado']:
                print("Livro já alugado.")
            else:
                livro['alugado'] = True
                print("Livro alugado com sucesso!")
            return
    
    print("Livro não encontrado.")

#Devolução de livro alugado
def devolver_livro():
    print("----Devolução de Livro----")
    codigo = input("Digite o código do livro a ser devolvido: ")
    
    for livro in livros:
        if livro['codigo'] == codigo:
            if livro['alugado']:
                livro['alugado'] = False
                print("Livro devolvido com sucesso!")
            else:
                print("Livro já está disponível.")
            return
    
    print("Livro não encontrado.")