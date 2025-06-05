# Talita está simulando o custo de frete para sua loja virtual. O valor depende da distância:

# Até 50 km: R$ 5,00
# De 51 a 150 km: R$ 15,00
# Acima de 150 km: R$ 25,00

MoneyKm = int(input("Digite a distância(em Km): "))
if MoneyKm <= 50:
    print("O valor de frete será: R$ 5,00 ")
elif MoneyKm <= 51 <= 150:
    print("O valor de frete será: R$ 15,00 ")
else:
    print("O valor de frete será: R$ 25,00 ")

