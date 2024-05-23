import os

def logo():
    print("---SENAI---")

def somar(n1,n2):
    resultado = n1+n2
    return resultado

logo()
numero1 = int(input("Digite o numero: "))
numero2 = int(input("Digite o numero: "))

soma = somar(numero1,numero2)
print(soma)