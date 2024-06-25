import os
import sys
os.system("cls||clear")
# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = sys.maxsize
soma_pares = 0
soma_impares = 0
media_pares=0
media_impares=0
media_geral = 0
QUANT_NUMEROS = 5
numeros = []
# Variáveis para armazenar os números
for i in range (QUANT_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Processando cada número
    if numero > 0:
        quantidade_positivos += 1
    else:
        quantidade_negativos += 1
        
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero
    
    maior_numero = max(numero, maior_numero)
    menor_numero = min(numero, menor_numero)

# Calculando as médias
    if quantidade_impares ==0:
        media_impares=0
    else:
        media_impares = soma_impares/quantidade_impares
    if quantidade_pares ==0:
        media_pares=0
    else:
        media_pares = soma_pares/quantidade_pares
    
media_geral = sum(numeros)/QUANT_NUMEROS
os.system("cls||clear")
# Imprimindo as estatísticas
print("Estatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Quantidade de numeros inseridos: {QUANT_NUMEROS}")
print(f"Maior numero: {maior_numero}")
print(f"Menor numero: {menor_numero}")
print(f"Media pares: {media_pares}")
print(f"Media impares: {media_impares}")
print(f"Media de todos os números: {media_geral}")

print("Numeros digitados na ordem inversa:")
numeros.reverse()
print(numeros)



