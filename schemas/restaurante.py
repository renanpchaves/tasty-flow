from pydantic import BaseModel, Field
from modelos.cardapio.item_cardapio import ItemCardapio

class RestauranteCriar(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    categoria: str = Field(..., min_length=2, max_length=50)
    ativo: bool = Field(default=False, description="Define se o restaurante inicia como ativo")

    model_config = {
        "json_schema_extra": {
            "nome": "Horacios Pizzeria",
            "categoria": "Pizza",
            "ativo": False
        }
    }

class RestauranteResponse(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    categoria: str = Field(..., min_length=2, max_length=50)
    ativo: bool
    avaliacao_media: float
    avaliacao_total: int

    model_config = {"from_attributes": True}

class RestauranteCriadoResponse(BaseModel):
    mensagem: str
    restaurante: RestauranteResponse