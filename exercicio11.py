peso = float(input("Digite qual o seu peso em KG: "))
altura = float(input("Digite qual a sua altura em M: "))
imc = peso / (altura ** 2)
print (f"{imc} IMC")
if peso <18.5:
    print("Abaixo do peso")
elif peso >= 18.5 <= 24.9:
    print("Peso normal")
elif peso >=25 <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")