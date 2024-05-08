import os
os.system("clear")
cont = 0
soma = 0
for i in range (4):
    nota = float(input(f"Digite sua {i+1}º nota: "))
    soma += nota
    cont = cont + 1
    os.system("clear")
media = soma/cont
print("<<<--- Exibindo dados --->>>")
print(f"Sua media é: {media}")