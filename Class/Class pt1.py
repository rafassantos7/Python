from dataclasses import dataclass
import os

os.system("cls||clear")

@dataclass
class Aluno:
    nome: str
    idade:int
    sexo:str
    telefone:int
    peso:float
    altura:float

alunos =[]
QUANTIDADE = 1

for i in range(QUANTIDADE):
    os.system("clear")
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = input("Digite sua idade: "),
        sexo = input("Digite seu sexo: ").upper(),
        telefone = input("Digite seu telefone: "),
        peso = input("Digite seu peso: "),
        altura = input("Digite sua altura: ")
        #o.upper()
    )
    alunos.append(aluno)

for i in alunos:
    os.system("clear || cls")
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Sexo: {i.sexo}")
    print(f"Telefone: {i.telefone}")
    print(f"Peso: {i.peso}")
    print(f"Altura: {i.altura}")