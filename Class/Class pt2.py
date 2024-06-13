from dataclasses import dataclass
import os
os.system("cls||clear")


@dataclass
class Aluno:
    def __init__(self,nome,idade,sexo,telefone,peso,altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.telefone = telefone
        self.peso = peso
        self.altura = altura
    
alunos = []
QUANT = 1

#Solicitando dados ao usuário.

for i in range(QUANT):
    os.system("cls || clear")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    sexo = input("Digite seu sexo: 'F' OU 'M': ").upper()
    telefone = input("Digite seu telefone: ")
    altura = input("Digite sua altura: ")
    peso = input("Digite seu peso: ")

    alunos.append(Aluno(nome,idade,sexo,telefone,altura,peso))

for i in alunos:
    os.system("clear || cls")
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Sexo: {i.sexo}")
    print(f"Telefone: {i.telefone}")
    print(f"Peso: {i.peso}")
    print(f"Altura: {i.altura}")