# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

tempo = int(input("Digite sua tempo gasto em segundos:"))
distância = int(input("Digite sua distância total em metros:"))
velocidadeM = distância / tempo
kmh = velocidadeM *3.6
print(f"{kmh:.2f} km/h")
if kmh < 5:
    print ("Lento")
elif kmh >10:
    print ("Rápido")
elif kmh >=5 <10:
    print ("médio")