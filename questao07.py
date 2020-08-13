# 7.Faça um algoritmo que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros_inteiros = []
soma = 0
multiplicação = 1
for i in range(1, 6):
    valor = input(f'Digite o {i}º valor inteiro: ')
    numeros_inteiros.append(valor)
    print(f'Valor adicionado: {valor}')

for percorendo in range(0, 5):
    soma += int(numeros_inteiros[percorendo])
    print(f'Somando os valores: {int(soma)}')
    multiplicação *= int(numeros_inteiros[percorendo])
    print(f'Multiplicando os valores: {int(multiplicação)}')

print(f'Os números digitados foram: {numeros_inteiros}')
print(f'A soma dos numero é {soma}')
print(f'A multiplicação dos números é {multiplicação}')
