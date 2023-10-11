from Classes import Pessoa
import pandas as pd
import os
import re
try:
    df = pd.read_json('dados.json') # abro ele no início do programa
except FileNotFoundError:
    print('Erro... Arquivo não encontrado!\n')
while True:
    print('-'*10, 'menu', '-'*10)
    print('(1) MOSTRAR PESSOA CADASTRADA')
    print('(2) EDITAR PESSOA / CADASTRAR PESSOA')
    print('(3) SAIR DO PROGRAMA')
    print('-'*26)
    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1 :
        print(df)
    if escolha == 2:
        while True:
            nome = input('Digite seu nome: ')
            # no código de baixo, eu pego basicamente qualquer letra maiúscula, minúscula, com acentos, espaço em branco e com ponto no final
            if re.match(r'^[a-zA-ZÀ-Úá-ú\s\.]+$', nome):
                df['nome'] = nome
                break
            else:
                print('ENTRADA INVÁLIDA! Digite apenas letras contidas em espaços')
        while True:
            idade = input('Digite a idade: ')
            if re.match(r'^[0-9]{1,3}$', idade):
                idade = int(idade) # no final da análise, transformo minha variável
                df['idade'] = idade
                break
            else:
                print('ENTRADA INVÁLIDA! Digite apenas números positivos')
        while True:
            altura = input('Digite a altura: ')
            if re.match(r'^\d{1}\.\d{1,2}$', altura):
                df['altura'] = altura
                break
            else: 
                print('ENTRADA INVÁLIDA! Digite apenas números inteiros positivos')
        while True:
            peso = input('Digite o peso: ')
            # pego qualquer número inteiro antes do ponto, pego o ponto, e por fim qualquer número depois do ponto
            #esse número antes do ponto deve aparecer no máximo 3 vezes, e depois do ponto, 2 vezes
            if re.match(r'^[0-9]{2,3}\.[0-9]{1,2}$' , peso):
                df['peso'] = peso
                break
            else:
                print('ENTRADA INVÁLIDA! Digite apenas números flutuantes com ponto')
        while True:
            nascimento = input('Digite a data de nascimento [dd/mm/aaaa]: ')
            #aqui pego qualquer número inteiro, separado por "/", "." ou "-" para evitar possíveis erros
            if re.match(r'^[0-9]{1,2}[-.\/][0-9]{1,2}[-.\/][0-9]{4}$', nascimento):
                df['nascimento'] = nascimento
                break
            else:
                print('ENTRADA INVÁLIDA! Digite apenas números inteiros')
        df.to_json('dados.json', force_ascii=False, orient='records') # salvo essas alterações no meu arquivo
        print('\033[32mDados cadastrados com sucesso!\033[m') # cor verde
    if escolha == 3:
        print('Saindo...')
        break
