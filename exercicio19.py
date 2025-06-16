#Exercício 19 – Números em Ordem Crescente
#Peça três números e exiba-os em ordem crescente.
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))
numeros = [n1, n2, n3]
numeros.sort()
print("Números em ordem crescente:")
for numero in numeros:
    print(numero)