# 1.Faça um algoritmo que leia um vetor de 5 números inteiros e mostre-os.
numeros = []
for indice in range(1, 5):
    numero = input(f"Informe o número {indice}: ")
    numero = int(numero)
    numeros.append(numero)

print(numeros)