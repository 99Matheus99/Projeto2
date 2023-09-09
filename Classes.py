class Pessoa:
    def __init__(Self, nome, idade, altura, peso): # função construtora da minha classe
        #aqui vão ficar os parâmetros da minha classe
        Self.nome = nome
        Self.idade = idade
        Self.altura = altura
        Self.peso = peso
    
    #métodos da minha classe(todos os métodos devem possuir Self)
    def eh_maior(Self): 
        return Self.idade >= 18 # Self.idade, é a variável idade que está dentro do meu objeto
    def imc(Self):
        imc = Self.peso / (Self.altura * Self.altura)
        return imc
    def imc_longo(Self):
        imc = Self.peso / (Self.altura * Self.altura)
        if 18 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Pré-obesidade"
        elif 30 <= imc < 35:
            return "Obesidade Grau 1"
        elif 35 <= imc < 40:
            return "Obesidade Grau 2"
        else:
            return "obesidade Grau 3"
    def apresentar(Self):
        print(f'Olá! Eu sou {Self.nome} e tenho {Self.idade} anos!')
#teste da função(será apagado)
Pessoa1 = Pessoa("Matheus", 21, 1.60, 60)
print(Pessoa1.eh_maior())
print(Pessoa1.imc())
print(Pessoa1.imc_longo())
Pessoa1.apresentar()