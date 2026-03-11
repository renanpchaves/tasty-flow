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
│       ├── bebida.py           # Itens tipo bebida
│       ├── prato.py            # Itens tipo prato
│       └── sobremesa.py        # Itens tipo sobremesa
├── main.py                     # Aplicação FastAPI
└── README.md
```

## 🔌 Endpoints
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/restaurantes/{nome}/cardapio` | Visualiza cardápio completo |
| POST | `/restaurantes/{nome}/cardapio/bebida` | Adiciona bebida |
| POST | `/restaurantes/{nome}/cardapio/prato` | Adiciona prato |
| POST | `/restaurantes/{nome}/cardapio/sobremesa` | Adiciona sobremesa |

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