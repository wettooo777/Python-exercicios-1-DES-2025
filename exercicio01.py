# Gabriel está acompanhando o desempenho de dois cursos online que lançou: Python Básico e JavaScript Essencial.
# Ele quer saber qual curso teve mais avaliações no último mês.

# Crie um programa que receba o número de avaliações de cada curso e exiba qual teve mais.
# Caso as quantidades sejam iguais, exiba uma mensagem dizendo que houve empate.
curso1 = int(input("Digite os votos totais do curso1:"))
curso2 = int(input("Digite os votos totais do curso2:"))

if curso1 > curso2:
    print("Curso1 tem mais votos!!!")
elif curso1 < curso2:
    print("Curso2 tem mais votos!!!")
else:
    print("Empate")