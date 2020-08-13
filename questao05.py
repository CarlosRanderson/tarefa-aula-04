# 5.Faça um algoritmo que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista_de_numero = []
lista_de_numeros_pares = []
lista_de_numeros_impares = []

valores = 0

for c in range(1, 20):

    valor = int(input('Digite um valor: '))

    lista_de_numero.append(valor)

    if valor % 2 == 0:
        lista_de_numeros_pares.append(valor)
    else:
        lista_de_numeros_impares.append(valor)

print(f'Os valores digitados foram: {lista_de_numero}')
print(f'Os valores digitados pares foram: {lista_de_numeros_pares}')
print(f'Os valores digitados impares foram: {lista_de_numeros_impares}')