from pydantic import BaseModel, Field

# ======= NOVO PRATO =======

class PratoCriar(BaseModel):
    """
    Schema da criaçao do prato
    """
    nome: str = Field(...,min_length=2, max_length=100)
    preco: float = Field(..., gt=0, description="Preço deve ser maior que 0")
    descricao: str = Field(...,min_length=1, max_length=150)
    categoria: str = Field(...,min_length=2, max_length=100)

    model_config = {
        "json_schema_extra": {
            "example": {
                "nome": "Suco",
                "preco": 8.50,
                "descricao": "Descrição do prato principal",
                "categoria": "Pizza"
            }
        }
    }

class PratoResponse(BaseModel):
    """
    Schema de response do prato
    """
    nome:str
    preco:float
    descricao:str
    categoria:str

    model_config = {"from_attributes": True}