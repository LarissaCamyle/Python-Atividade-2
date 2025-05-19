#importa a classe restaurante
from Classes.Restaurante import Restaurante

#Cria as Classes
restaurante_1 = Restaurante('poletto', 'Massas')
restaurante_1.alterar_status()
restaurante_1.receber_avaliacao("Lucas", 5)
restaurante_1.receber_avaliacao("Maria", 5)

restaurante_2 = Restaurante('madero', 'Massas')


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()