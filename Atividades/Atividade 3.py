import os
soma = 0
for i in range (5):
    numero = int(input(f"Digite o {i+1} º número: "))
    soma += numero
os.system("clear")
print(soma)