import os
os.system("clear")
def pares(n1):
    contpar= 0
    for numero in n1:
        if numero % 2 == 0:
            contpar += 1
    return contpar
def impares(n1):
    contimpar=0
    for numero in n1:
        if numero %2 ==1:
            contimpar += 1
    return contimpar
numeros = []
QUANT = 6
for i in range (QUANT):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
quantpar = pares(numeros)
quantimpar = impares(numeros)
print(f"Pares {quantpar}")
print(f"Impares {quantimpar}")