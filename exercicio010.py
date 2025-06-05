# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do salário

salario = float(input("Digite o seu salário: "))
parcela = float(input("Digite a sua parcela: "))
limite = salario * 0,35
if salario >= 3000 and parcela <= limite:
    print("Financiamento aprovado!")
else:
    print("Financiamento negado")