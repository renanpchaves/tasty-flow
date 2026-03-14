# 🍽️ TASTY FLOW API

API REST para gerenciamento de restaurantes, cardápios e avaliações. Desenvolvida com FastAPI e programação orientada a objetos.

## 📁 Estrutura do Projeto
```
tasty-flow/
├── modelos/
│   ├── restaurante.py          # Classe principal de restaurantes
│   ├── avaliacao.py            # Sistema de avaliações
│   └── cardapio/
│       ├── item_cardapio.py    # Classe abstrata base
│       ├── bebida.py           # Classes para bebidas
│       ├── prato.py            # Classes para pratos principais
│       └── sobremesa.py        # Classes para sobremesas
├── schemas/
│   ├── restaurante.py          # Schemas Pydantic (entrada e saída da API)
│ 
├── main.py                     # Aplicação FastAPI
└── README.md
```

## 🔌 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/restaurantes/`                | Visualiza restaurantes |
| GET | `/restaurantes/{nome}`          | Visualiza restaurante por nome |
| GET | `/restaurantes/{nome}/cardapio` | Visualiza cardápio completo por restaurante |
| POST | `/restaurantes/`               | Adiciona um novo restaurante |
| POST | `/restaurantes/{nome}/cardapio/bebida` | Adiciona bebida |
| POST | `/restaurantes/{nome}/cardapio/prato` | Adiciona prato | 
| POST | `/restaurantes/{nome}/cardapio/sobremesa` | Adiciona sobremesa (não implementado) |


Ainda construindo!

### Restaurantes

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Informações da API |
| GET | `/restaurantes/` | Lista todos os restaurantes |
| GET | `/restaurantes/{nome}` | Busca restaurante específico |
| POST | `/restaurantes/` | Cria novo restaurante |

## 🛠️ Tecnologias

- **Python 3.12+**
- **FastAPI** - Framework web moderno e rápido
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI
- **POO** - Programação Orientada a Objetos com herança e classes abstratas

---

⭐ Projeto desenvolvido como parte dos estudos de desenvolvimento backend com Python.