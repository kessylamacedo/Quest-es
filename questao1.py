
# Questão 1 - Leitura e validação das notas

notas = []

for i in range(6):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))

    while nota < 0 or nota > 10:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        nota = float(input(f"Digite novamente a nota do aluno {i + 1}: "))

    notas.append(nota)

print("\nNotas dos alunos:")

for i in range(6):
    print(f"Aluno {i + 1}: {notas[i]}")



# Questão 2 - Cálculo da média e filtragem

soma = 0

for nota in notas:
    soma += nota

media = soma / 6

acima_media = 0

print(f"\nMédia geral da turma: {media:.2f}")

for i in range(6):
    if notas[i] >= media:
        acima_media += 1
    else:
        print(f"Nota abaixo da média: {notas[i]}")

print(f"Alunos acima ou iguais à média: {acima_media}")


# Questão 3 - Recuperação e atualização

for i in range(6):
    if notas[i] < media:
        print(f"\nAluno {i + 1} está de recuperação.")

        recuperacao = float(input("Digite a nota da recuperação: "))

        while recuperacao < 0 or recuperacao > 10:
            print("Nota inválida! Digite entre 0 e 10.")
            recuperacao = float(input("Digite novamente: "))

        if recuperacao > notas[i]:
            notas[i] = recuperacao

soma = 0

for nota in notas:
    soma += nota

nova_media = soma / 6

print("\nNotas atualizadas:")

for i in range(6):
    print(f"Aluno {i + 1}: {notas[i]}")

print(f"\nNova média da turma: {nova_media:.2f}")


