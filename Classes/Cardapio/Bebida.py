from Classes.Cardapio.Item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__ (self, _nome, _preco, _tamanho):
        #importa os dados nome e preco da outra classe
        super().__init__(_nome,_preco)
        self._tamanho = _tamanho


    def __str__(self):
        return f'{self._nome} | {self._preco} | {self._tamanho}'