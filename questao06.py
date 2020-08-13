# 6.Faça um algoritmo que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

nota_dos_alunos = []


#Preenchendo lista com as médias
for aluno in range(1, 3):
    print(f'Digite as 4 notas do {aluno}º aluno. ')
    soma_das_notas = 0

    for notas in range(1, 5):
        soma_das_notas += int(input(f'{notas}º nota: '))
        if notas <= 4:
            media = soma_das_notas/4

    nota_dos_alunos.append(media)

#Imprimindo as médias dos alunos
for i in range(0, 2):
    print(f'A média do {i+1}º aluno foi:',nota_dos_alunos[i])
