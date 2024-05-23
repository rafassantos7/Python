import os
os.system("clear")

def cab():
    print("---SENAI---")

def taboada(n1):
    for i in range (1,11):
      print(f"{n1}*{i} = {i*n1}")

numero1 = int(input("Número: "))
os.system("clear")
cab()
mult = taboada(numero1)
print (mult)