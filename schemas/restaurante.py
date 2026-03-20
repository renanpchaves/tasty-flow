from pydantic import BaseModel, Field, field_serializer
from modelos.cardapio.item_cardapio import ItemCardapio

class RestauranteCriar(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    categoria: str = Field(..., min_length=2, max_length=50)
    ativo: bool = Field(default=False, description="Define se o restaurante inicia como ativo")

    model_config = {
        "json_schema_extra": {
            "example": {
            "nome": "Horacios Pizzeria",
            "categoria": "Pizza",
            "ativo": False
            }
        }
    }

class RestauranteResponse(BaseModel):
    nome: str 
    categoria: str 
    ativo: bool
    avaliacao_media: float
    avaliacao_total: int

    @field_serializer('ativo')
    def serialize_ativo(self, valor: bool) -> str:
        return "ativo" if valor else "inativo"
    
    model_config = {"from_attributes": True}

class RestauranteCriadoResponse(BaseModel):
    mensagem: str
    restaurante: RestauranteResponse

#wrapper pra lista de todos os restaurantes:
class RestauranteListaTotal(BaseModel):
    """
    Schema pra lista de todos os restaurantes
    """

    restaurantes:list[RestauranteResponse]
    total:int