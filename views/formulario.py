# View - o que vai para o usuário
def formulario_login():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitado = input("Informe sua senha: ")
    usuario_completo = [usuario_digitado, senha_digitado]
    return usuario_completo
    
def exibir_mensagem(texto):
    print("\n\n")
    print("============================")
    print(texto)
    print("============================")
    print("\n\n")

def menu():
    print("[1] - Para cadastrar cliente")
    print("[2] - para listar todos os clientes")
    print("[3] - Para sair")
    opcao = input("Digite a opção: ")
    return opcao

def cadastro_cliente():
    nome = input("Informe o Nome:")
    telefone = input("Informe o Telefone:")
    cliente = [nome,telefone]
    return cliente

