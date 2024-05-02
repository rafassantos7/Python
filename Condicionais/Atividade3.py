import os
os.system("clear")

usuario: str
senha: str

usuario = (input("Digite o usuario: "))
senha = (input("Digite a senha: "))

if usuario == "seila" and senha == "1234":
    print("Bem vindo!")
else:
    print("Tudo errado.")    
