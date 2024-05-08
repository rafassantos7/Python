import os
os.system("clear")
soma = 0
nota = -1
while True:
    nota = float(input(f"Digite sua {i+1}ª nota: "))
    if nota <0 or nota > 10:
        print("Nota errada, digite novamente.")
        soma=0
    else:
            soma+=nota
            break
media= soma/QUANTNOTAS
print(media)
if media >=7:
    print("Aprovado.")
elif media>=5:
    print("Recuperação.")
else:
    print("Reprovado.")