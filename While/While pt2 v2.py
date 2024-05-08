import os
os.system("clear")

while True:
    nota = float(input("Digite sua nota: "))
    if nota <0 or nota>10:
        print("Digite sua nota novamente. ")
    else :
        os.system("clear")
        print("Nota válida: ",nota)
        break