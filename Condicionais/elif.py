import os
os.system("clear")

peso = int(input("Digite seu peso: "))

os.system("clear")

if peso < 40:
    print("abaixo do peso")
elif peso > 80:
    print("acima do peso")
else:
    print("sobrepeso")
print("==FIM==")