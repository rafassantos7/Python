import  os
os.system("clear")
def somar(n1,n2):
    resultado = n1+n2
    return resultado 
def multiplicar(n1,n2):
    return n1*n2 
def subtração(n1,n2):
    resultado = n1-n2
    return resultado 
def divisão(n1,n2):
    return n1/n2


numero1 = int(input("Digite o numero: "))
numero2 = int(input("Digite o numero: "))

soma = somar(numero1,numero2)
mult = multiplicar(numero1,numero2)
div = divisão(numero1,numero2)
sub = subtração(numero1,numero2)

print(f"Soma: {soma}")
print(f"Subtração: {sub}")
print(f"Divisão: {div}")
print(f"Multiplicação: {mult}")
