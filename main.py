from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel, Field
from modelos.restaurante import Restaurante

app = FastAPI(title="Tasty Flow API", version="1.0")


class RestauranteCriar(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    categoria: str = Field(...,min_length=2, max_length=50)


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

    restaurantes_lista = [r.to_dict() for r in Restaurante.restaurantes]
    return {"restaurantes": restaurantes_lista, "total": len(restaurantes_lista)}


@app.get("/restaurantes/{nome}")
def buscar_restaurante(nome: str):
    """
    Busca o restaurante por nome
    """
    restaurante = Restaurante.buscar_nome(nome)

    if not restaurante:
        raise HTTPException(
            status_code=404, detail=f'Restaurante "{nome}" não foi encontrado.'
        )

    return restaurante.to_dict()


# ======= ROTAS POST =======


@app.post("/restaurantes/")
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
        "restaurante": novo_restaurante.to_dict(),
    }
