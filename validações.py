from classes import Pessoa
nome = str(input('Digite seu nome: '))
idade = int(input('Digite a idade: '))
altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))
nascimento = str(input('Digite a data de nascimento: ')) # o str() é pra deixar bem claro que a data é dado em string
Pessoa1 = Pessoa(nome, idade, altura, peso, nascimento)