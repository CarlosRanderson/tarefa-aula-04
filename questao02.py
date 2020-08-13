# 2.Faça um algoritmo que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vet=[]
for n in range(1, 11):
    num = int(input(f'Informe os numeros {n} '))
    vet.append(num)
vet.sort()
vet.reverse()
print(vet)