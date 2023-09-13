class Pessoa:
    def __init__(Self, nome, idade, altura, peso, nascimento): # função construtora da minha classe
        #aqui vão ficar os parâmetros da minha classe
        Self.nome = nome
        Self.idade = idade
        Self.altura = altura
        Self.peso = peso
        Self.nascimento = nascimento
    
    #métodos da minha classe(todos os métodos devem possuir Self)
    def eh_maior(Self): 
        return Self.idade >= 18 # Self.idade, é a variável idade que está dentro do meu objeto
    def imc(Self):
        imc = Self.peso / (Self.altura * Self.altura) # aqui eu pego os parâmetros da minha classe
        return imc
    def imc_longo(Self):
        imc = Self.imc() # já aqui, eu pego o método da minha classe, no caso, o imc
        if imc < 18.5:
            return "Abaixo do peso"
        if imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Pré-obesidade"
        elif imc < 35:
            return "Obesidade Grau 1"
        elif imc < 40:
            return "Obesidade Grau 2"
        else:
            return "obesidade Grau 3"
    def apresentar(Self):
        print(f'Olá! Eu sou {Self.nome} e tenho {Self.idade} anos!')
    def comparar_idade(Self, idade):
        # Esse método compara a idade que entro com a idade do objeto
        if idade < Self.idade:
            print(f'{Self.nome} é mais velho do que essa idade!')
        elif idade > Self.idade:
            print(f'{Self.nome} é mais novo do que essa idade!')
        else:
            print(f'{Self.nome} possui esta idade')
