#Crie uma função area_retangulo(base, altura) que retorna a área de um retângulo.
def area_retangulo(base, altura):
    return base * altura
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
print(f"A área do retângulo é {area_retangulo(base, altura)}")