import os

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
media: float = (nota1+nota2)/2

os.system("clear || cls")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Media: {media}")
