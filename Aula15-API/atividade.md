# Aula 15 — API REST

Atividade da API de livros (Flask + SQLAlchemy). Segue os prints/comandos que rodei.

## POST - inserindo 15 livros

Comando usado repeti pra cada livro, mudando o body:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":ANO DA PUBLICAÇÃO}'
```

Já tinha os 3 livros do seed (ids 1, 2, 3), então os novos entraram do 4 até o 18: Todos deram 201 Created, sem erro.

## PUT - atualizando o livro id 1

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros/1 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"Cotemig","autor":"3A1","ano":2026}'
```

Retornou:

```
ano          : 2026
autor        : 3A1
data_criacao : 2026-07-28 15:34:51.560413
id           : 1
titulo       : Cotemig
```

## Lista depois dos POSTs + PUT

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros
```

```json
[
  {
    "ano": 1949,
    "autor": "George Orwell",
    "data_criacao": "2026-07-28 15:34:51.560422",
    "id": 3,
    "titulo": "1984"
  },
  {
    "ano": 1977,
    "autor": "Clarice Lispector",
    "data_criacao": "2026-07-28 15:35:45.282823",
    "id": 10,
    "titulo": "A Hora da Estrela"
  },
  {
    "ano": 1945,
    "autor": "George Orwell",
    "data_criacao": "2026-07-28 15:35:45.547408",
    "id": 17,
    "titulo": "A Revolução dos Bichos"
  },
  {
    "ano": 1932,
    "autor": "Aldous Huxley",
    "data_criacao": "2026-07-28 15:35:45.531268",
    "id": 16,
    "titulo": "Admirável Mundo Novo"
  },
  {
    "ano": 1937,
    "autor": "Jorge Amado",
    "data_criacao": "2026-07-28 15:35:45.189738",
    "id": 7,
    "titulo": "Capitães da Areia"
  },
  {
    "ano": 2026,
    "autor": "3A1",
    "data_criacao": "2026-07-28 15:34:51.560413",
    "id": 1,
    "titulo": "Cotemig"
  },
  {
    "ano": 1866,
    "autor": "Fiódor Dostoiévski",
    "data_criacao": "2026-07-28 15:35:45.562227",
    "id": 18,
    "titulo": "Crime e Castigo"
  },
  {
    "ano": 1953,
    "autor": "Ray Bradbury",
    "data_criacao": "2026-07-28 15:35:45.500197",
    "id": 14,
    "titulo": "Fahrenheit 451"
  },
  {
    "ano": 1956,
    "autor": "João Guimarães Rosa",
    "data_criacao": "2026-07-28 15:35:45.101642",
    "id": 6,
    "titulo": "Grande Sertão: Veredas"
  },
  {
    "ano": 1865,
    "autor": "José de Alencar",
    "data_criacao": "2026-07-28 15:35:45.215578",
    "id": 8,
    "titulo": "Iracema"
  },
  {
    "ano": 1881,
    "autor": "Machado de Assis",
    "data_criacao": "2026-07-28 15:35:44.918065",
    "id": 4,
    "titulo": "Memórias Póstumas de Brás Cubas"
  },
  {
    "ano": 1882,
    "autor": "Machado de Assis",
    "data_criacao": "2026-07-28 15:35:45.484461",
    "id": 13,
    "titulo": "O Alienista"
  },
  {
    "ano": 1890,
    "autor": "Aluísio Azevedo",
    "data_criacao": "2026-07-28 15:34:51.560421",
    "id": 2,
    "titulo": "O Cortiço"
  },
  {
    "ano": 1857,
    "autor": "José de Alencar",
    "data_criacao": "2026-07-28 15:35:45.257015",
    "id": 9,
    "titulo": "O Guarani"
  },
  {
    "ano": 1943,
    "autor": "Antoine de Saint-Exupéry",
    "data_criacao": "2026-07-28 15:35:45.515812",
    "id": 15,
    "titulo": "O Pequeno Príncipe"
  },
  {
    "ano": 1960,
    "autor": "Carolina Maria de Jesus",
    "data_criacao": "2026-07-28 15:35:45.359818",
    "id": 11,
    "titulo": "Quarto de Despejo"
  },
  {
    "ano": 2019,
    "autor": "Itamar Vieira Junior",
    "data_criacao": "2026-07-28 15:35:45.464116",
    "id": 12,
    "titulo": "Torto Arado"
  },
  {
    "ano": 1938,
    "autor": "Graciliano Ramos",
    "data_criacao": "2026-07-28 15:35:45.040674",
    "id": 5,
    "titulo": "Vidas Secas"
  }
]
```

## DELETE - excluindo os ids 5, 6 e 7

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 -Method DELETE
Invoke-RestMethod http://127.0.0.1:5000/api/livros/6 -Method DELETE
Invoke-RestMethod http://127.0.0.1:5000/api/livros/7 -Method DELETE
```

Não volta corpo nenhum (204 No Content), só some da lista. Excluí:
 id 5, id 6 , id 7 

## Lista final depois dos DELETEs

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros
```

```json
[
  {
    "ano": 1949,
    "autor": "George Orwell",
    "data_criacao": "2026-07-28 15:34:51.560422",
    "id": 3,
    "titulo": "1984"
  },
  {
    "ano": 1977,
    "autor": "Clarice Lispector",
    "data_criacao": "2026-07-28 15:35:45.282823",
    "id": 10,
    "titulo": "A Hora da Estrela"
  },
  {
    "ano": 1945,
    "autor": "George Orwell",
    "data_criacao": "2026-07-28 15:35:45.547408",
    "id": 17,
    "titulo": "A Revolução dos Bichos"
  },
  {
    "ano": 1932,
    "autor": "Aldous Huxley",
    "data_criacao": "2026-07-28 15:35:45.531268",
    "id": 16,
    "titulo": "Admirável Mundo Novo"
  },
  {
    "ano": 2026,
    "autor": "3A1",
    "data_criacao": "2026-07-28 15:34:51.560413",
    "id": 1,
    "titulo": "Cotemig"
  },
  {
    "ano": 1866,
    "autor": "Fiódor Dostoiévski",
    "data_criacao": "2026-07-28 15:35:45.562227",
    "id": 18,
    "titulo": "Crime e Castigo"
  },
  {
    "ano": 1953,
    "autor": "Ray Bradbury",
    "data_criacao": "2026-07-28 15:35:45.500197",
    "id": 14,
    "titulo": "Fahrenheit 451"
  },
  {
    "ano": 1865,
    "autor": "José de Alencar",
    "data_criacao": "2026-07-28 15:35:45.215578",
    "id": 8,
    "titulo": "Iracema"
  },
  {
    "ano": 1881,
    "autor": "Machado de Assis",
    "data_criacao": "2026-07-28 15:35:44.918065",
    "id": 4,
    "titulo": "Memórias Póstumas de Brás Cubas"
  },
  {
    "ano": 1882,
    "autor": "Machado de Assis",
    "data_criacao": "2026-07-28 15:35:45.484461",
    "id": 13,
    "titulo": "O Alienista"
  },
  {
    "ano": 1890,
    "autor": "Aluísio Azevedo",
    "data_criacao": "2026-07-28 15:34:51.560421",
    "id": 2,
    "titulo": "O Cortiço"
  },
  {
    "ano": 1857,
    "autor": "José de Alencar",
    "data_criacao": "2026-07-28 15:35:45.257015",
    "id": 9,
    "titulo": "O Guarani"
  },
  {
    "ano": 1943,
    "autor": "Antoine de Saint-Exupéry",
    "data_criacao": "2026-07-28 15:35:45.515812",
    "id": 15,
    "titulo": "O Pequeno Príncipe"
  },
  {
    "ano": 1960,
    "autor": "Carolina Maria de Jesus",
    "data_criacao": "2026-07-28 15:35:45.359818",
    "id": 11,
    "titulo": "Quarto de Despejo"
  },
  {
    "ano": 2019,
    "autor": "Itamar Vieira Junior",
    "data_criacao": "2026-07-28 15:35:45.464116",
    "id": 12,
    "titulo": "Torto Arado"
  }
]
```

