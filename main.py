from fastapi import FastAPI, HTTPException
from schemas import (
    RestauranteCriar, RestauranteResponse, RestauranteCriadoResponse,
    BebidaCriar, BebidaResponse,
    PratoCriar, PratoResponse, SobremesaCriar, 
    SobremesaResponse, AvaliacaoResponse, AvaliacaoCriar, RestauranteListaTotal
)
from modelos import Restaurante, Bebida, Prato, Sobremesa

app = FastAPI(title="Tasty Flow API", version="1.0")

# ================================= ROTAS GET =================================

# ===== PAGINA INICIAL =====

@app.get("/")
def root():
    """
    Página inicial da API
    """
    return {
        "mensagem": "API do Tasty Flow está rodando normalmente.",
        "versao": "1.0",
        "documentacao": "/docs", 
        "endpoints": {
            "restaurantes": [
                "GET /restaurantes/ - Lista todos os restaurantes",
                "GET /restaurantes/{nome} - Busca restaurante específico",
                "POST /restaurantes/ - Cria novo restaurante"
            ],
            "cardapio": [
                "GET /restaurantes/{nome}/cardapio - Lista o cardápio",
                "POST /restaurantes/{nome}/cardapio/bebida - Adiciona bebida",
                "POST /restaurantes/{nome}/cardapio/prato - Adiciona prato"
                "POST /restaurantes/{nome}/cardapio/sobremesa - Adiciona sobremesa"
            ],
            "avaliações": [
                "POST /restaurantes/{nome}/avaliacoes",
                "GET /restaurantes/{nome}/avaliacoes"
            ],
            "status":
            [
                "PUT /restaurantes/{nome}/status"
            ]
        }
    }
# ===== GET TODOS RESTAURANTES =====

@app.get("/restaurantes/", response_model=RestauranteListaTotal)
def listar_restaurantes():
    """
    Lista todos os restaurantes do app
    """
    if not Restaurante.restaurantes:
        return {"restaurantes": [], "total": 0}


    return {"restaurantes": Restaurante.restaurantes,
            "total": len(Restaurante.restaurantes)}

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
        elif hasattr(item, 'categoria'): #prato
            item_dict['tipo'] = 'Prato Principal'
            item_dict['descricao'] = item.descricao
            item_dict['categoria'] = item.categoria
        else:
            item_dict['tipo'] = 'Sobremesa'
            item_dict['descricao'] = item.descricao
            item_dict['tipo'] = item.tipo
            item_dict['tamanho'] = item.tamanho
        cardapio_lista.append(item_dict)

    return {
        "restaurante": restaurante._nome,
        "cardapio": cardapio_lista,
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
    novo_restaurante = Restaurante(dados.nome, dados.categoria, dados.ativo)
 
    return {
        "mensagem": "Restaurante criado com sucesso!",
        "restaurante": novo_restaurante,
    }

# ===== POST PRATO =====

@app.post("/restaurantes/{nome}/cardapio/prato", response_model=PratoResponse)
def adicionar_prato(nome:str, prato_dados: PratoCriar):
    """
    Adiciona um prato principal ao cardápio
    """

    restaurante = Restaurante.buscar_nome(nome)

    #Validação
    if not restaurante:
        raise HTTPException(
            status_code=404,
            detail = f'Restaurante "{nome}" não encontrado.'
        )
    
    #Cria o prato principal
    novo_prato = Prato(
        nome = prato_dados.nome,
        preco = prato_dados.preco,
        descricao = prato_dados.descricao,
        categoria = prato_dados.categoria
    )

    restaurante.adicionar_no_cardapio(novo_prato)
    return novo_prato

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
            detail=f'Restaurante "{nome}" não encontrado.'
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

@app.post("/restaurantes/{nome}/cardapio/sobremesa", response_model=SobremesaResponse)
def adicionar_sobremesa(nome:str, sobremesa_dados: SobremesaCriar):
    """
    Adiciona uma sobremesa ao cardápio
    """

    restaurante = Restaurante.buscar_nome(nome)

    #Validação
    if not restaurante:
        raise HTTPException(
            status_code=404,
            detail = f'Restaurante "{nome}" não encontrado.'
        )
    
    #Cria a sobremesa
    nova_sobremesa = Sobremesa(
        nome = sobremesa_dados.nome,
        preco = sobremesa_dados.preco,
        descricao = sobremesa_dados.descricao,
        tipo = sobremesa_dados.tipo,
        tamanho = sobremesa_dados.tamanho
    )

    restaurante.adicionar_no_cardapio(nova_sobremesa)
    return nova_sobremesa

# ===== POST AVALIACAO =====

@app.post("/restaurantes/{nome}/avaliacoes")
def avaliar_restaurante(nome: str, avaliacao: AvaliacaoCriar):
    """
    Adiciona uma avaliaçao ao restaurante
    """

    restaurante = Restaurante.buscar_nome(nome)

    #validaçao
    if not restaurante:
        raise HTTPException(
            status_code=404,
            detail=f'Restaurante "{nome}" não encontrado.'
        )
    
    restaurante.receber_avaliacao(avaliacao.cliente, avaliacao.nota)

    return {
        "message": "Avaliaçao adicionada com sucesso!",
        "cliente": avaliacao.cliente,
        "nota": avaliacao.nota,
        "nova_media": restaurante.avaliacao_media,
    }

# ===== GET AVALIACAO =====
@app.get("/restaurantes/{nome}/avaliacoes")
def listar_avaliacoes(nome:str):
    """
    Lista todas as avaliaçoes do restaurante especifico
    """

    restaurante = Restaurante.buscar_nome(nome)

    if not restaurante:
        raise HTTPException(
            status_code=404,
            detail=f'Restaurante "{nome}" não encontrado.'
        )
    
    if not restaurante._avaliacao:
        return{
            "restaurante": restaurante.nome,
            "avaliacoes": [],
            "media": 0.0,
            "total": 0
        }
    
    avaliacoes_lista = [
        {
            "cliente": av.cliente,
            "nota": av.nota
        }
        for av in restaurante._avaliacao
    ]

    return {
        "restaurante": restaurante.nome,
        "avaliacoes": avaliacoes_lista,
        "media_avaliacoes": restaurante.avaliacao_media,
        "total_avaliacoes": restaurante.avaliacao_total
    }

# ================================= ROTAS PUT =================================

@app.put("/restaurantes/{nome}/status")
def alterar_status(nome:str):
    """
    Altera o status do restaurante: ativo/inativo
    """

    restaurante = Restaurante.buscar_nome(nome)

    #Validação:
    if not restaurante:
        raise HTTPException(
            status_code=404,
            detail=f'Restaurante "{nome}" não encontrado.'
        )
    
    #Altera o status:
    restaurante.alterar_status()
    status_texto = "ativo" if restaurante.ativo else "inativo"

    return {
        "mensagem": f'Status do restaurante "{nome}" alterado com sucesso.',
        "novo_status": status_texto,
    }