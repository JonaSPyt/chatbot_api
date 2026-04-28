# Chatbot API com FastAPI e Gemini

API simples em Python usando FastAPI para receber uma pergunta e gerar uma resposta com a API do Gemini.

## O que este projeto faz

- expõe uma API HTTP com FastAPI
- permite chamadas de outros frontends com CORS liberado
- recebe uma pergunta em `POST /chat`
- usa a biblioteca `google-genai` para gerar a resposta
- disponibiliza documentação automática em `/docs`

## Estrutura do projeto

```text
.
├── .env
├── testback.py
└── testapi.py
```

`testback.py` contém a aplicação principal.

## Requisitos

- Python 3.12 ou compatível
- uma chave válida da API Gemini

## Configuração

Crie ou ajuste o arquivo `.env` com a variável abaixo:

```env
GEMINI_API_KEY=sua_chave_aqui
```

## Instalação

Se você ainda não instalou as dependências no ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-dotenv pydantic google-genai
```

Se o `venv` já existe, basta ativá-lo:

```bash
source venv/bin/activate
```

## Como executar

Com o ambiente virtual ativado:

```bash
uvicorn testback:app --reload
```

Ou sem ativar o ambiente:

```bash
venv/bin/uvicorn testback:app --reload
```

Depois disso, a API ficará disponível em:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`

## Endpoints

### `GET /`

Retorna uma mensagem simples para validar que a API está no ar.

Exemplo de resposta:

```json
{
  "message": "Hello World"
}
```

### `POST /chat`

Recebe uma pergunta e retorna a resposta gerada pelo Gemini.

Exemplo de corpo da requisição:

```json
{
  "question": "Explique o que é FastAPI"
}
```

Exemplo de resposta:

```json
{
  "question": "Explique o que é FastAPI",
  "answer": "FastAPI e uma framework..."
}
```

## Exemplo com `curl`

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"question":"O que e FastAPI?"}'
```

## Solução de problemas

### `uvicorn: command not found`

Ative o ambiente virtual antes de rodar o comando:

```bash
source venv/bin/activate
uvicorn testback:app --reload
```

Ou rode diretamente:

```bash
venv/bin/uvicorn testback:app --reload
```

### `GEMINI_API_KEY não foi definida no arquivo .env`

Confira se:

- o arquivo `.env` existe na raiz do projeto
- a variável está com o nome `GEMINI_API_KEY`
- a chave foi preenchida corretamente

### Erro de importação de bibliotecas

Reinstale as dependências dentro do ambiente virtual:

```bash
source venv/bin/activate
pip install fastapi uvicorn python-dotenv pydantic google-genai
```

## Próximos passos sugeridos

- criar um `requirements.txt`
- adicionar testes para a rota `/chat`
- separar configurações em um arquivo próprio
- validar melhor erros da API externa
