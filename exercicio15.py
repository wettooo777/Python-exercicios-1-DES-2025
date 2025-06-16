#Exercício 15 – Validação de Idade para Cadastro
#Peça a idade do usuário e diga se ele pode se cadastrar em um site:
#Permitido: 13 anos ou mais
idade = int(input("Digite sua idade: "))
if idade >= 13:
    print("Aprovado")
else:
    print("Negado")