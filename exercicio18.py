#Exercício 18 – Cálculo de Nota com Peso
#Receba duas notas e seus respectivos pesos. Calcule a média ponderada.
#Fórmula: (nota1 × peso1 + nota2 × peso2) / (peso1 + peso2)
nota1 = float(input("Digite a 1ª nota: "))
peso1 = float(input("Digite o peso da 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
peso2 = float(input("Digite o peso da 2ª nota: "))
media_ponderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
print(f"A média ponderada é: {media_ponderada:.2f}")