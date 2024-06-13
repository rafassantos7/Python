import os
import time
import sys

os.system("cls")

print("O minha lindaaa, vou te dar umas opções e você escolhe direitinho na ordem que quiser, ta bommm?")

while True:
  
  print("1\tCoisinhas bobas que gostaria de falar.")
  print("2\tCoisinhas que quero admitir.")
  print("3\tCoisinhas que quero admitir (sapecagens).")
  print("4\tVou deixar essa opçãpo aqui se tu quiser falar algo.")
  print("5\tFim.\n")
  resposta= int(input("Escolhe mo: "))

  match(resposta):
    case 1:
      print("Oioi, fiz esse código pra falar como me sinto em relação à você e a nós dois também")
      print("Queria fazer um programa mais bonitinho, mas ainda não aprendi e não sei se vou aprender a fazer o que eu quero por agora")
      resp1 = input("\nSe terminou de ler, digita S:\n")
      resp1 = resp1.upper()
      while True:
        if resp1 != "S":
          print("\nNo seu tempo, linda.")
        else:
          os.system("cls")
          print("Escolhe outra opção hihihi\n")
          break

    case 2:
      print("Nao sei")