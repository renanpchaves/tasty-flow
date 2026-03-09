from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida1 = Bebida('Suco de Laranja', 5.0, 'Grande')
prato1 = Prato('Lasanha', 20.0, 'Bolonhesa')


def main():
    print(bebida1)
    print (prato1)

if __name__ == '__main__':
    main()