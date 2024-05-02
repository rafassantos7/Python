import os
os.system("clear")
media = float
valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))
maiorvalor = max(valor1, valor2)
menorvalor = min(valor1, valor2)

soma = valor1+valor2
mult = valor1*valor2
media = soma/2

os.system("clear")

print("--Exibindo dados--")
print(f"Soma: {soma}")
print(f"Produto: {mult}")
print(f"Media: {media}")
print(f"Maior Numero: {maiorvalor}")
print(f"Menor Numero: {menorvalor}")

