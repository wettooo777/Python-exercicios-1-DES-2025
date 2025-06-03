# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

tempo = float(input("Digite sua tempo gasto em segundos: "))
distância = float(input("Digite sua distância total em metros: "))
velocidadeM = distância / tempo
print(f"{velocidadeM:.2f} m/s")
if velocidadeM < 5:
    print ("Lento")
elif velocidadeM >= 5 <= 10:
    print ("médio")
else:
    print ("Rápido")