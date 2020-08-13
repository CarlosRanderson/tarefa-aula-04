# 8.Faça um algoritmo que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for i in range(1, 5):
    print(f'Digite a idade e a altura da {i}º pessoa:')
    idade = int(input('Idade: '))
    altura = int(input('Altura: '))
    idades.append(idade)
    alturas.append(altura)

idades.reverse()
alturas.reverse()

print(f'idades: {idades}')
print(f'alturas: {alturas}')
