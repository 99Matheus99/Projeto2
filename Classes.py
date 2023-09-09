class Pessoa:
    def __init__(Self, nome, idade, altura, peso): # função construtora da minha classe
        #aqui vão ficar os parâmetros da minha classe
        Self.nome = nome
        Self.idade = idade
        Self.altura = altura
        Self.peso = peso
    
    #métodos da minha classe(todos os métodos devem possuir Self)
    def eh_maior(Self):
        if Pessoa1.idade >= 18:
            return True
        else:
            return False

Pessoa1 = Pessoa("Matheus", 21, 1.60, 60)

Pessoa1.eh_maior()