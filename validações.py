from classes import Pessoa
import re
while True:
    nome = input('Digite seu nome: ')
    # no código de baixo, eu pego basicamente qualquer letra maiúscula, minúscula, com acentos, espaço em brando e com ponto no final
    if re.match(r'^[a-zA-ZÀ-Úá-ú\s\.]+$', nome):
        break
    else:
        print('ENTRADA INVÁLIDA! Digite apenas letras contidas em espaços')
while True:
    idade = input('Digite a idade: ')
    if re.match(r'^[0-9\s]+$', idade):
        idade = int(idade) # no final da análise, transformo minha variável
        break
    else:
        print('ENTRADA INVÁLIDA! Digite apenas números positivos')
while True:
    peso = input('Digite o peso: ')
    # pego qualquer número inteiro antes do ponto, pego o ponto, e por fim qualquer número depois do ponto
    if re.match(r'^[0-9]+\.[0-9]+$' , peso):
        break
    else:
        print('ERRO! Digite apenas números flutuantes com ponto')




#nascimento = str(input('Digite a data de nascimento: ')) # o str() é pra deixar bem claro que a data é dado em string
#Pessoa1 = Pessoa(nome, idade, altura, peso, nascimento)