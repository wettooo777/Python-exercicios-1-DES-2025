# Rafael trabalha com armazenamento de grãos e precisa garantir que a umidade do ar no local não ultrapasse 70%.
# Escreva um programa que receba o valor da umidade atual e exiba um alerta se estiver acima do limite.

umidadeMAX = int(input("Digite a porcetagem da umidade local:"))
if umidadeMAX >= 70:
    print("ALERTA: Umidade muito alta!!!")
else:
    print("Nada a se preocupar")