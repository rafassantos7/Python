import os
os.system("clear")
contpar = 0
contimpar = 0
for i in range (6):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero %2==0:
        contpar += 1
    else:
        contimpar += 1

print(f"Quantidade de numeros pares : {contpar}")
print(f"Quantidade de numeros impares : {contimpar}")