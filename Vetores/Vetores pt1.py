import os
os.system("clear")
notas = []
for i in range (3):
    nota=float(input("Digite sua nota: "))
    notas.append(nota)
os.system("clear")
for i in range (3):
    print(f" {i+1}º Nota : {notas[i]}")
