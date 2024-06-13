import os
os.system("clear")
while True:
    os.system("clear")
    print("Escolha")
    print("1\t Digite seu nome")
    print("2\t Digite seu numero")
    print("3\t Digite sua idade")
    opcao = int(input("Digite a opção: "))
    match(opcao):
        case 1:
            nome = str(input("Nome: "))
          