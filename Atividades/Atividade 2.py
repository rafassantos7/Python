import os 

nome = str(input("Digite seu nome: "))
sexo = str(input("Digite seu sexo: "))
estado = str(input("Digite seu estado civil: "))

sexo = sexo.lower()
estado = estado.lower()

os.system("clear")
if sexo == "f" and estado == "casada":
    tempo = input("Digite o tempo de casamento(em anos): ")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado: {estado}")
if sexo == "f" and estado == "casada":
    print(f"Tempo de casamento: {tempo} anos ")