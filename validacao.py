import banco

# Controller - A validação
def validar_login(usuario_digitado, senha_digitado):
    usuario_BD = banco.model_usuario()
    senha_BD = banco.model_senha()
    if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
        print ("Pode entrar")
    else:
        print("Usuário ou senha inválido")
