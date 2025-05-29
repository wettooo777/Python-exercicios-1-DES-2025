# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)
meta1 = int(input("Digite a meta1:"))
meta2 = int(input("Digite a meta2:"))
meta3 = int(input("Digite a meta3:"))
soma = meta1+meta2+meta3
soma2 = soma/3
print (f"média:{soma2:.2f}")
if soma2>=7:
    print("Aprovado !!!")
elif soma2 >=5 <7:
    print("Em treinamento !!")
elif soma2 <5:
    print("Reprovado !")
