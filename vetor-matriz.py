alunos = ["Alice","Bruno","Carla"]
dias = ["Seg", "Ter", "Qua","Qui"]
reservas = [["Ausente" for _ in dias] for _ in alunos]
print ("Prencha com 'S' para presença e 'X' para ausências: ")
for i, aluno in enumerate(alunos):
    print (f"f\nAlunos: (alunos)")
    for i, dia in enumerate(dias):
        entrada = input(f" (dia): ")
        if entrada.upper() == 'S':
            reservas[i][j] = "presente"
print("\ntabela de Reservas: ")
print(f" {alunos:<10} {' '.join}")