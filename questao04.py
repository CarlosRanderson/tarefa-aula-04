# 4.Faça um algoritmo que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

consoantes = []

for letra in letras:

    if letra not in "aeiou":
        consoantes.append(letra)

print(consoantes)