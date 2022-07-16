usuario_digitado = input("Informe o seu usuario: ")
senha_digitado = input("Informe sua senha: ")

# Model - O que vem para o banco de dados (BD)
usuario_BD = "joao"
senha_BD = "123"

# Controller - A validação
if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
    print ("Pode entrar")
else:
    print("Usuário ou senha inválido")
