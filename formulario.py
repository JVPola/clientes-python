import validacao
# View - o que vai para o Usuário
def formulario_login():
    usuario_digitado = input("Informe o seu usuario: ")
    senha_digitado = input("Informe sua senha: ")
    validacao.validar_login(usuario_digitado, senha_digitado)

