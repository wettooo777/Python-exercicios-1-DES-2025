#Exercício 16 – Cálculo de Reajuste Salarial
#Crie um programa que calcule o reajuste de salário:

#Salários até R$ 2000,00: +15%
#De R$ 2000,01 a R$ 5000,00: +10%
#Acima de R$ 5000,00: +5%
salario = float(input("Digite o salário: R$ "))
if salario <= 2000.00:
    reajuste = salario * 0.15
    print(f"Salário com reajuste: R$ {salario + reajuste:.2f}")
elif salario <= 5000.00:
    reajuste = salario * 0.10
    print(f"salário com reajuste: r$ {salario + reajuste:.2f}")
else:
    reajuste = salario * 0.05
    print(f"Salário com reajuste: R$ {salario + reajuste:.2f}")
