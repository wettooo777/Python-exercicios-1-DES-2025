#Exercício 17 – Conversão de Temperaturas
#Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.
#Fórmula: F = C × 1.8 + 32
c = float(input("Digite a temperatura em Celsius: "))
f = c * 1.8 + 32
print(f"A temperatura em Fahrenheit é: {f:.2f}°F")