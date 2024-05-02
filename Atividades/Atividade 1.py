import os
os.system("clear")

quantmaca=int(input("Digite o numero de maçãs: "))
quantmorango=int(input("Digite o numero de morangos: "))

if quantmaca>5:
    precomaca = 2.20
else:
    precomaca = 2.50

if quantmorango>5:
    precomorango = 1.50
else:
    precomorango = 1.80

soma = quantmaca + quantmorango
totalmaca = float(precomaca*quantmaca)
totalmorango = float(precomorango*quantmorango)
valortotal = float(totalmorango+totalmaca)

if soma>8 or valortotal>25:
    desc = 0.1
    valortotal = (totalmorango+totalmaca) - 0.1*valortotal
os.system("clear")
print(f"Quantidade de maçãs: {quantmaca}")
print(f"Quantidade de morangos: {quantmorango}")
print(f"Total maçãs: {totalmaca}")
print(f"Total morangos: {totalmorango}")
print(f"Total da compra: {valortotal}")