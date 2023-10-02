from Classes import Pessoa
import re
nome = ''
idade = altura = peso = nascimento = 0
while True:
    print('---menu---')
    print('(1) MOSTRAR PESSOA CADASTRADA')
    print('(2) EDITAR PESSOA / CADASTRAR PESSOA')
    print('(3) SAIR DO PROGRAMA')
    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1 :
        if idade == 0:
            print('Não há dados cadastrados!')
        else:
            print(f'Nome: {nome}')
            print(f'idade: {idade}')
            print(f'altura: {altura}')
            print(f'peso: {peso}')
            print(f'nascimento: {nascimento}')
    if escolha == 2:
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
        print('Dados cadastrados com sucesso!')
    if escolha == 3:
        break
