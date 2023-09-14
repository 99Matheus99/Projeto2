from classes import Pessoa
import re
while True:
    nome = str(input('Digite seu nome: '))
    # no código de baixo, eu pego basicamente qualquer letra maiúscula, minúscula, com acentos, espaço em brando e com ponto no final
    if re.match(r'^[a-zA-ZÀ-Úá-ú\s\.]+$', nome):
        break
    else:
        print('ENTRADA INVÁLIDA! Digite apenas letras contidas em espaços')



#idade = int(input('Digite a idade: '))
#altura = float(input('Digite a altura: '))
#peso = float(input('Digite o peso: '))
#nascimento = str(input('Digite a data de nascimento: ')) # o str() é pra deixar bem claro que a data é dado em string
#Pessoa1 = Pessoa(nome, idade, altura, peso, nascimento)