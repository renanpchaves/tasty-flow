from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_horacio = Restaurante('Horacios Pizzeria', 'Pizza')
bebida1 = Bebida('Suco de Laranja', 5.0, 'Grande')
prato1 = Prato('Lasanha', 20.0, 'Bolonhesa')
restaurante_horacio.adicionar_no_cardapio(bebida1)
restaurante_horacio.adicionar_no_cardapio(prato1)

def main():
    restaurante_horacio.exibir_cardapio

if __name__ == '__main__':
    main()