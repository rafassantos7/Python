import os
os.system("clear")
cont = 0
soma = 0
QUANTNOTAS = 2
for i in range (2):
    while True:
        nota = float(input(f"Digite sua {i+1} nota: "))
        if nota <0 or nota >10:
            print("Digite sua nota novamente. ")
            soma = 0
        else :
            os.system("clear")
            soma += nota
            break
media = soma/QUANTNOTAS
print (media)