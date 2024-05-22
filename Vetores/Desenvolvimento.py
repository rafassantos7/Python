import os
os.system("clear")
notas=[]
QUANTIDADESDENOTAS=3
#Solicitando Notas
for i in range (QUANTIDADESDENOTAS):
    nota= float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)
media = sum(notas)/QUANTIDADESDENOTAS
os.system("clear")
#ForEach
for nota in notas:
    print(f"Sua {i+1}ª nota: {nota}")
print(f"Media: {media}")
