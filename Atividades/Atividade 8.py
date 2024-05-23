import os
os.system("clear")

def somar(n1,n2):
    return n1+n2
def mediar(n1,n2):
    return (n1+n2)/2

numero1 = int(input("Digite seu numero: "))
numero2 = int(input("Digite seu numero: "))

soma = somar(numero1,numero2)
media = mediar(numero1,numero2)

os.system("clear")
print(f"Soma : {soma}")
print(f"Media : {media}")