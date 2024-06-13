import os
os.system("clear")
print("Escolha um mês do ano:")
print("1\tMês 1")
print("2\tMês 2")
print("3\tMês 3")
print("4\tMês 4")
print("5\tMês 5")
print("6\tMês 6")
print("7\tMês 7")
print("8\tMês 8")
print("9\tMês 9")
print("10\tMês 10")
print("11\tMês 11")
print("12\tMês 12")
a = int(input("Escolhe: "))
os.system("clear")
match(a):
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Escolha novamente.")