from classes import Pessoa
import re
while True:
    nome = input('Digite seu nome: ')
    # no código de baixo, eu pego basicamente qualquer letra maiúscula, minúscula, com acentos, espaço em branco e com ponto no final
    if re.match(r'^[a-zA-ZÀ-Úá-ú\s\.]+$', nome):
        break
    else:
        print('ENTRADA INVÁLIDA! Digite apenas letras contidas em espaços')
while True:
    idade = input('Digite a idade: ')
    if re.match(r'^[0-9]{1,3}$', idade):
        idade = int(idade) # no final da análise, transformo minha variável
        break
    else:
        print('ENTRADA INVÁLIDA! Digite apenas números positivos')
while True:
    altura = input('Digite a altura: ')
    if re.match(r'^\d{1}\.\d{1,2}$', altura):
        break
    else: 
        print('ENTRADA INVÁLIDA! Digite apenas números inteiros positivos')
while True:
    peso = input('Digite o peso: ')
    # pego qualquer número inteiro antes do ponto, pego o ponto, e por fim qualquer número depois do ponto
    #esse número antes do ponto deve aparecer no máximo 3 vezes, e depois do ponto, 2 vezes
    if re.match(r'^[0-9]{2,3}\.[0-9]{1,2}$' , peso):
        break
    else:
        print('ENTRADA INVÁLIDA! Digite apenas números flutuantes com ponto')
while True:
    nascimento = input('Digite a data de nascimento [dd/mm/aaaa]: ')
    #aqui pego qualquer número inteiro, separado por "/", "." ou "-" para evitar possíveis erros
    if re.match(r'^[0-9]{1,2}[-.\/][0-9]{1,2}[-.\/][0-9]{4}$', nascimento):
        break
    else:
        print('ENTRADA INVÁLIDA! Digite apenas números inteiros')





#Pessoa1 = Pessoa(nome, idade, altura, peso, nascimento)