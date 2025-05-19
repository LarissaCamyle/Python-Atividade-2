from Classes.Cardapio.Item_cardapio import ItemCardapio

#classe prato importa os valores da classe item cardapio
class Prato(ItemCardapio):
    def __init__ (self, _nome, _preco, _descricao):
        #dados importados da outra classe
        super().__init__(_nome,_preco)
        #atributo criado além dos outros importados
        self.descricao = _descricao


    def __str__(self):
        return f'{self._nome} | {self._preco} | {self._descricao}'