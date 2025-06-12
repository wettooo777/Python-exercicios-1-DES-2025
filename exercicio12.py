senha = input("Digite sua senha, que contenha pelo menos 8 digítos: ")

digitos = len(senha)

if digitos >= 8:
    print("Senha correta")
else:
    print("Senha incorreta")