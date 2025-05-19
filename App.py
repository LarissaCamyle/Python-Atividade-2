#importa a classe restaurante
from Classes.Restaurante import Restaurante
from Classes.Cardapio.Prato import Prato
from Classes.Cardapio.Bebida import Bebida

#Cria os itens do tipo classe
restaurante_1 = Restaurante('poletto', 'Massas')
restaurante_1.alterar_status()
restaurante_1.receber_avaliacao("Lucas", 5)
restaurante_1.receber_avaliacao("Maria", 5)

restaurante_2 = Restaurante('madero', 'Massas')


bebida_1 = Bebida("Suco", 2.50, "G")
prato_1 = Prato("Pizza", 60.99, "Pizza de queijo")
restaurante_1.adicionar_no_cardapio(bebida_1)
restaurante_1.adicionar_no_cardapio(prato_1)


def main():
    restaurante_1.listar_o_cardapio

if __name__ == '__main__':
    main()