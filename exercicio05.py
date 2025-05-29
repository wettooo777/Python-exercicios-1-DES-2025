# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.

internetA = int(input("Digite quantos GB de internet foi consumida:"))
if internetA >= 100:
    print("Você passou do limite mensal do consumidor!!!")
else:
    print("O limite não passou. Aproveite!!!")