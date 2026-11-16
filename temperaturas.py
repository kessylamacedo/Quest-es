
# Questão 1 - Registro de temperaturas

temperaturas = []

dias = ["Domingo", "Segunda", "Terça", "Quarta",
        "Quinta", "Sexta", "Sábado"]

for i in range(7):
    temperatura = float(input(f"Digite a temperatura de {dias[i]}: "))

    while temperatura < -10 or temperatura > 50:
        print("Temperatura inválida! Digite entre -10 e 50.")
        temperatura = float(input(f"Digite novamente a temperatura de {dias[i]}: "))

    temperaturas.append(temperatura)

print("\nTemperaturas registradas:")

for i in range(7):
    print(f"{dias[i]}: {temperaturas[i]}°C")


# Questão 2 - Análise climática e alertas

maior = temperaturas[0]
menor = temperaturas[0]
indice_maior = 0
alerta_calor = 0

for i in range(7):

    if temperaturas[i] > maior:
        maior = temperaturas[i]
        indice_maior = i

    if temperaturas[i] < menor:
        menor = temperaturas[i]

    if temperaturas[i] > 32:
        alerta_calor += 1

print("\nRelatório climático da semana:")

print(f"Maior temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")
print(f"Dias com alerta de calor: {alerta_calor}")
print(f"Dia mais quente: {dias[indice_maior]}")


# Questão 3 - Simulação de frente fria

for i in range(7):

    if temperaturas[i] > 30:
        temperaturas[i] = temperaturas[i] - 4.5

        if temperaturas[i] < 15:
            temperaturas[i] = 15

print("\nTemperaturas após a frente fria:")

for i in range(7):
    print(f"{dias[i]}: {temperaturas[i]}°C")

soma = 0

for temperatura in temperaturas:
    soma += temperatura

nova_media = soma / 7

print(f"\nNova média da semana: {nova_media:.2f}°C")