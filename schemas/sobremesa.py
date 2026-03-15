from pydantic import BaseModel, Field

# ======= NOVA SOBREMESA =======

class SobremesaCriar(BaseModel):
    """
    Schema da criaçao da sobremesa
    """
    nome: str = Field(...,min_length=2, max_length=100)
    preco: float = Field(..., gt=0, description="Preço deve ser maior que 0")
    descricao: str = Field(...,min_length=1, max_length=150)
    tipo: str = Field(...,min_length=2, max_length=100)
    tamanho: str = Field(...,min_length=2, max_length=100)

    model_config = {
        "json_schema_extra": {
            "example": {
                "nome": "Pudim",
                "preco": 10.00,
                "descricao": "Descrição da sobremesa",
                "tipo": "Doce de Leite",
                "tamanho": "Médio"
            }
        }
    }

class SobremesaResponse(BaseModel):
    """
    Schema de response do prato
    """
    nome:str
    preco:float
    descricao:str
    tipo:str
    tamanho:str

    model_config = {"from_attributes": True}