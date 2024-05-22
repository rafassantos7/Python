import os
os.system("clear")
notas=[]
cont = 0
soma=0
for i in range (3):
    nota= float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)
    soma+=notas[i]
    cont = cont +1
i = 0
media = soma/cont
os.system("clear")
for i in range (3):
    print(f"Sua {i+1}ª nota: {notas[i]}")
print(f"Media: {media}")