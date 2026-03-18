from pydantic import BaseModel, Field

class AvaliacaoCriar(BaseModel):
    """
    Schema para postar avaliaçoes
    """

    cliente: str = Field(...,min_length=2, max_length=100, description="Nome do Cliente")
    nota: int = Field(..., ge=1, le=5, description="Nota de 1 a 5 estrelas")

    model_config = {
        "json_schema_extra": {
            "example": {
                "cliente": "Renan",
                "nota": 5
            }
        }
    }

class AvaliacaoResponse(BaseModel):
    """
    Schema da resposta da avaliaçao
    """

    cliente: str
    nota: int

    model_config = {"from_attributes": True}