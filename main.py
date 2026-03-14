from fastapi import FastAPI, HTTPException
from schemas.restaurante import (
    RestauranteCriar,
    RestauranteResponse,
    RestauranteCriadoResponse,
)
from schemas.bebida import (
    BebidaCriar,
    BebidaResponse
)
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida

app = FastAPI(title="Tasty Flow API", version="1.0")

# ================================= ROTAS GET =================================

# ===== PAGINA INICIAL =====

@app.get("/")
def root():
    """
    Página inicial
    """
    return {
        "mensagem": "Api do app Tasty Flow está rodando normalmente.",
        "versao": "1.0",
        "endpoints": [
            "GET /restaurantes/ - Lista todos os restaurantes",
            "GET /restaurantes/{nome} - Busca restaurante específico",
            "POST /restaurantes/ - Cria novo restaurante",
        ],
    }

# ===== GET TODOS RESTAURANTES =====

@app.get("/restaurantes/")
def listar_restaurantes():
    """
    Lista todos os restaurantes do app
    """
    if not Restaurante.restaurantes:
        return {"restaurantes": [], "total": 0}

    restaurantes_lista = Restaurante.restaurantes
    return {"restaurantes": restaurantes_lista, "total": len(restaurantes_lista)}

# ===== GET RESTAURANTE POR NOME =====

@app.get("/restaurantes/{nome}", response_model=RestauranteResponse)
def buscar_restaurante(nome: str):
    """
    Busca o restaurante por nome
    """
    restaurante = Restaurante.buscar_nome(nome)

    if not restaurante:
        raise HTTPException(
            status_code=404, detail=f'Restaurante "{nome}" não foi encontrado.'
        )

    return restaurante

# ===== GET CARDAPIO POR RESTAURANTE =====

@app.get("/restaurantes/{nome}/cardapio")
def buscar_cardapio(nome:str):
    """
    Retorna o cardapio do restaurante, completo.
    """

    restaurante = Restaurante.buscar_nome(nome)

    #Validação
    if not restaurante:
        raise HTTPException(
            status_code=404,
            detail = f'Restaurante {nome} não encontrado.'
        )
    
    #Cardapio vazio?
    if not restaurante._cardapio:
        return {
            "restaurante": restaurante.nome,
            "cardapio": [],
            "total_itens": 0
        }
    
    #Lista do cardapio:
    cardapio_lista = []
    for item in restaurante._cardapio:
        item_dict = {
            "nome": item._nome,
            "preco": item._preco
        }

        
    #Identifica tipo e adiciona campo de acordo com o tipo no cardápio:
    if hasattr(item, 'sabor'): #bebida
        item_dict['tipo'] = 'Bebida'
        item_dict['tamanho'] = item.tamanho
        item_dict['sabor'] = item.sabor

    cardapio_lista.append(item_dict)

    return {
        "restaurante": restaurante._nome,
        "cardapio": restaurante._cardapio,
        "total_items": len(cardapio_lista)
    }


# ================================= ROTAS POST =================================

# ===== POST RESTAURANTE =====

@app.post("/restaurantes/", response_model=RestauranteCriadoResponse)
def criar_restaurante(dados: RestauranteCriar):
    """
    Cria um novo restaurante
    """

    # Validação
    if Restaurante.buscar_nome(dados.nome):
        raise HTTPException(
            status_code=400, detail=f'Restaurante "{dados.nome}" já existe.'
        )

    # Cria o restaurante
    novo_restaurante = Restaurante(dados.nome, dados.categoria)

    return {
        "mensagem": "Restaurante criado com sucesso!",
        "restaurante": novo_restaurante,
    }

# ===== POST PRATO =====



# ===== POST BEBIDA =====

@app.post("/restaurantes/{nome}/cardapio/bebida", response_model=BebidaResponse)
def adicionar_bebida(nome:str, bebida_dados: BebidaCriar):
    """
    Adiciona uma bebida no cardápio
    """
    
    restaurante = Restaurante.buscar_nome(nome)

    #Validação
    if not restaurante:
        raise HTTPException(
            status_code=404,
            detail=f'Restaurante "{nome} não encontrado.'
        )
    
    #Cria a bebida
    nova_bebida = Bebida(
        nome = bebida_dados.nome,
        preco = bebida_dados.preco,
        tamanho = bebida_dados.tamanho,
        sabor = bebida_dados.sabor
    )

    restaurante.adicionar_no_cardapio(nova_bebida)
    return nova_bebida

# ===== POST SOBREMESA =====