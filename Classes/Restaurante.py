class Restaurante:
    #init é um método que todas as classes possuem
    #ele é um construtor q inicializa os atributos da classe
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    #Personalizar como as informações serão printadas no terminal
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'

#Cria as Classes
restaurante_1 = Restaurante('Poletto', 'Massas')
restaurante_2 = Restaurante('Madero', 'Massas')

#Printa as classes no terminal
print(restaurante_1)
print(restaurante_2)
