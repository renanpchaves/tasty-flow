from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_horacio = Restaurante('Horacios Pizzeria', 'Pizza')
bebida1 = Bebida('Suco', 5.0, 'Grande', 'Laranja')
bebida1.desconto()
prato1 = Prato('Lasanha', 20.0, 'Bolonhesa')
prato1.desconto()
sobremesa1 = Sobremesa('Pudim', 15.0, 'Doce de Leite', 'Médio', 'Grande')
sobremesa1.desconto()
restaurante_horacio.adicionar_no_cardapio(bebida1)
restaurante_horacio.adicionar_no_cardapio(prato1)
restaurante_horacio.adicionar_no_cardapio(sobremesa1)

def main():
    Restaurante.listar_restaurantes()
    print('\n')
    restaurante_horacio.exibir_cardapio

if __name__ == '__main__':
    main()