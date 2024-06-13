import os
os.system("cls||clear")

valor=float(input("Digite o valor do produto: "))
os.system("cls||clear")

print("1\t Pagamento à vista.\n2\t Pagamento à prazo.")
pag= int(input("Qual a forma de pagamento?\n"))
match(pag):
    case 1:
       desc = valor*0.1
       valorfinal = valor - desc
       forma = "Pagamento à vista."
    case 2:
        os.system("cls||clear")
        parcela = int(input("Digite o numero de parcelas: "))
        valorparcela = valor/parcela
        forma = "Pagamento à prazo."
    case _:
        input("Opção incorreta, escolha novamente.")

os.system("cls||clear")
if pag == 1:
    print(f"Valor do produto: R${valor}")
    print(f"Forma de Pagamento: {forma}")
    print(f"Valor do desconto: R${desc}")
    print(f"Total à vista: R${valorfinal}")
elif pag == 2:
    print(f"Valor do produto: R${valor}")
    print(f"Forma de Pagamento: {forma}")
    print(f"Quantidade de parcelas: {parcela}")
    print(f"Valor por parcela: R${valorparcela}")
    print(f"Total à prazo: R${valor}")
else :
    print("Operação inválida.")