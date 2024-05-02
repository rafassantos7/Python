import os

os.system("clear")

nome=str(input("Digite seu nome: "))
idade=int(input("Digite seu idade: "))
nota1=int(input("Digite sua primeira nota: "))
nota2=int(input("Digite sua segunda nota: "))
nota3=int(input("Digite sua terceira nota: "))
soma = nota1 + nota2 + nota3
media = soma/3

os.system("clear")

print("Exibindo dados")
print(f"Idade: {idade}")
print(f"Primeria nota: {nota1}")
print(f"Segunda nota: {nota2}")
print(f"Terceira nota: {nota3}")
print(f"Media: {media}")

if media >= 7:
    print("Aprovado.")
else:
    print("Reprovado.")