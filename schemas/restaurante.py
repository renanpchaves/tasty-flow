from pydantic import BaseModel, Field


class RestauranteCriar(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    categoria: str = Field(..., min_length=2, max_length=50)


class RestauranteResponse(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    categoria: str = Field(..., min_length=2, max_length=50)
    ativo: bool
    avaliacao_media: float
    total_avaliacoes: int

    model_config = {"from_attributes": True}


class RestauranteCriadoResponse(BaseModel):
    mensagem: str
    restaurante: RestauranteResponse