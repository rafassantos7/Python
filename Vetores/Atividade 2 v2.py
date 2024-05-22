import os
import sys
os.system("clear")

notas=[]

QUANTIDADESNOTAS = 5

maiornota=0
menornota=sys.maxsize

#Solicitando Notas
for i in range (QUANTIDADESNOTAS):
    nota =float(input(f"Digite sua {i+1}ª nota: "))
    notas.append(nota)
    maiornota=max(nota,maiornota)
    menornota=min(nota,menornota)

media = sum(notas)/QUANTIDADESNOTAS

os.system("clear")
#Exibindo Dados
for i, nota in enumerate(notas):
    print(f"Sua {i+1}ª nota é: {nota} ")
print(f"Sua média é: {media}")
print(f"Maior nota: {maiornota}")
print(f"Menor nota: {menornota}")