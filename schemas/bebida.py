from pydantic import BaseModel, Field

# ======= BEBIDA =======

class BebidaCriar(BaseModel):
    """
    Schema da criaçao de bebida
    """
    nome: str = Field(...,min_length=2, max_length=100)
    preco: float = Field(..., gt=0, description="Preço deve ser maior que 0")
    tamanho: str = Field(...,min_length=1, max_length=50)
    sabor: str = Field(...,min_length=2, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {
                "nome": "Suco",
                "preco": 8.50,
                "tamanho": "500ml",
                "sabor": "Laranja"
            }
        }
    }

class BebidaResponse(BaseModel):
    """
    Schema de response da bebida
    """
    nome:str
    preco:float
    tamanho:str
    sabor:str

    model_config = {"from_attributes": True}