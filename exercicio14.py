compra = float(input("Digite o total da sua compra: "))

if compra >= 500:
    print("Desconto de 10%")
elif compra >= 300 <= 500:
    print("Desconto de 5%")
else:
    print("Sem desconto")
