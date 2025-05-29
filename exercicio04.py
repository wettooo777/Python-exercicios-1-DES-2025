# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

tempo = int(input("Digite sua tempo gasto:"))
distância = int(input("Digite sua distância total:"))
velocidadeM = distância / tempo
print(f"{velocidadeM:.2f} km/h")
if velocidadeM  < 5:
    print ("Lento")
elif velocidadeM  > 15:
    print ("Rápido")
elif velocidadeM >=5 <10:
    print ("médio")