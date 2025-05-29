#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.

trabalhoX = int(input("Digite o tempo do trabalho X:"))
trabalhoY = int(input("Digite o tempo do trabalho Y:"))
trabalhoZ = int(input("Digite o tempo do trabalho Z:"))

soma = trabalhoX + trabalhoY + trabalhoZ
soma2 = soma - 360
if soma2 <= 0:
    print("Acabou o tempo")
else:
    print("Parabéns")