# 3.Faça um algoritmo que leia 4 notas, mostre as notas e a média na tela.
notas = []
soma = 0
for i in range (1,5):
    nota = float(input(f"Digite a nota {i}: "))
    soma += nota
    notas.append(nota)

media = soma / 4

for i in range(4):
    print(f"Nr[{i+1}]: ",notas[i])

print(f"E a média: {media}")