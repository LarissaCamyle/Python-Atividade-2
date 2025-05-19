from Classes.Avaliacao import Avaliacao
from Classes.Cardapio.Item_cardapio import ItemCardapio

class Restaurante:
    """Classe Restaurante"""

    #armazena todos os restaurantes
    restaurantes = []

    #init é um método que todas as classes possuem
    #ele é um construtor q inicializa os atributos da classe
    def __init__(self, _nome, _categoria):
        """Cria um tipo restaurante
        Input:nome e categoria
        """

        #O "_" é a sintaxe de um atributo PRIVADO
        #Muda todas as palavras para maiuscula
        self._nome = _nome.title()
        self._categoria = _categoria
        self._status = False

        self._avaliacoes = []
        self.cardapio_do_restaurante = []

        #adiciona a lista
        Restaurante.restaurantes.append(self)


    #Personaliza como as informações serão printadas no terminal
    def __str__(self):
        """Printa as informações do restaurante"""
        return f'{self._nome} | {self._categoria} | {self.status}'
    

    #metodo para a classe
    @classmethod
    def listar_restaurantes(cls):
        """Lista todos os restaurantes"""

        #função que lista todos os restaurantes
        print(f"{"NOME".ljust(20)}  {"CATEGORIA".ljust(20)}  {"AVALIAÇÃO".ljust(20)}  {"STATUS".ljust(20)}\n")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {str(restaurante.status).ljust(20)}")


    #modifica como o atributo vai ser lido
    @property
    def status(self):
        """Modifica como é printado o status de um restaurante"""
        return "☑" if self._status else "☐"


    #um metodo para obj especificos n entra como um @classmethod
    def alterar_status(self):
        """Modifica o status de um restaurante"""
        self._status = not self._status


    def receber_avaliacao(self, cliente, nota):
        """Adiciona as avaliacoes a uma lista de avaliações"""
        #cria a classe a partir dos atributos instanciados
        if 0 < nota <= 5:
            nova_avaliacao = Avaliacao(cliente, nota)
        
            self._avaliacoes.append(nova_avaliacao)


    @property
    def media_avaliacoes(self):
        """Calcula a média das avaliações"""
        #se estiver vazio
        if not self._avaliacoes:
            return '-'
        else:               #percorre por todas as avaliações desse restaurante e soma
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
                            #pega a quantidade de notas existentes
            quantidade_de_notas = len(self._avaliacoes)
                            #resultado da media              digitos depois da virgula
            media = round(soma_das_notas/quantidade_de_notas, 1)

            return media


    def adicionar_no_cardapio(self, item):
        """Adiciona itens ao cardapio"""
        #verifica se o item é do tipo classe filho da classe pai item cardapio
        if isinstance(item, ItemCardapio):
            self.cardapio_do_restaurante.append(item)

    @property
    def listar_o_cardapio(self):
        print(f"Cardápio do Restaurante {self._nome}\n")

        print(f'{" NÚMERO DO ITEM".ljust(20)}  {" NOME".ljust(20)}  {" PREÇO".ljust(20)}')
                                #lista                         comeca a contar do 1
        for i, item in enumerate(self.cardapio_do_restaurante, start=1):
            item = f'{str(i).ljust(20)} | {str(item._nome).ljust(20)} | R${str(item._preco).ljust(20)}'
            print(item)