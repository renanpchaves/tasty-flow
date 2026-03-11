from fastapi import FastAPI, HTTPException
import requests
from schemas.restaurante import (
    RestauranteCriar,
    RestauranteResponse,
    RestauranteCriadoResponse,
)
from modelos.restaurante import Restaurante

app = FastAPI(title="Tasty Flow API", version="1.0")

# ======= ROTAS GET =======


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


@app.get("/restaurantes/")
def listar_restaurantes():
    """
    Lista todos os restaurantes do app
    """
    if not Restaurante.restaurantes:
        return {"restaurantes": [], "total": 0}

    restaurantes_lista = Restaurante.restaurantes
    return {"restaurantes": restaurantes_lista, "total": len(restaurantes_lista)}


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


# ======= ROTAS POST =======


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
