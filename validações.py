from Classes import Pessoa
import os
import re
while True:
    print('-'*10, 'menu', '-'*10)
    print('(1) MOSTRAR PESSOA CADASTRADA')
    print('(2) EDITAR PESSOA / CADASTRAR PESSOA')
    print('(3) SAIR DO PROGRAMA')
    print('-'*26)
    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1 :
        try:
            with open('arquivo.txt', mode='r', encoding='utf-8') as arquivo:
                 # através da função os, vejo o status do meu arquivo, com o atributo de tamanho
                if os.stat('arquivo.txt').st_size == 0:  # caso esse tamanho seja zero, o arquivo está vazio
                    print('NÃO HÁ DADOS CADASTRADOS!')
                for linha in arquivo:
                    print(f'\033[33m{linha.strip()}\033[m') # cor amarela
        except FileNotFoundError:
            print('ARQUIVO NÃO ENCONTRADO!')       
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
        with open('arquivo.txt', mode='w', encoding='utf-8') as arquivo:
            arquivo.write(f'nome: {str(nome)}\n')
            arquivo.write(f'idade: {str(idade)}\n')
            arquivo.write(f'altura: {str(altura)}\n')
            arquivo.write(f'peso: {str(peso)}\n')
            arquivo.write(f'nascimento: {str(nascimento)}\n')
        print('\033[32mDados cadastrados com sucesso!\033[m') # cor verde
    if escolha == 3:
        print('Saindo...')
        break
