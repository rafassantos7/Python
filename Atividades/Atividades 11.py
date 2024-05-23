import os
os.system("clear")

def produto(n1):
    if n1 >= 100:
        inflação = 0,2
    else :
        inflação = 0,1

    resultado1 = n1 * inflação
    return n1+resultado1
prod = int(input("Digite o preço do produto: "))
precofinal = produto(prod)

print(f"Total da compra {precofinal}")