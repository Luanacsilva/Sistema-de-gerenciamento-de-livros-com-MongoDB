# 📚 Sistema de Gerenciamento de Livros com MongoDB

Este projeto é um sistema web simples para gerenciamento de livros, desenvolvido com Node.js, Express, MongoDB e EJS.  
Ele permite operações de **Create**, **Read**, **Update** e **Delete** (CRUD) em um catálogo de livros.

---

## 🚀 Tecnologias Utilizadas

- Node.js
- Express.js
- MongoDB (via Mongoose)
- EJS (Embedded JavaScript Templates)
- Bootstrap (pra fingir que o CSS tá bonitinho)
- Dotenv

---

## 🛠 Funcionalidades

- 📥 Cadastro de novos livros  
- 📋 Listagem de livros cadastrados  
- ✏️ Edição das informações dos livros  
- 🗑 Remoção de livros da base de dados


---
📁 Estrutura de Pastas

├── models

│   └── Livro.js

├── routes

│   └── livroRoutes.js

├── views

│   ├── livros

│   └── partials

├── public

│   └── css

├── server.js

└── .env


---
📌 Próximos Passos

Adicionar autenticação de usuários

Implementar paginação na listagem de livros

Criar versão RESTful da API



---
## 🧰 Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Luanacsilva/Sistema-de-gerenciamento-de-livros-com-MongoDB.git
   cd Sistema-de-gerenciamento-de-livros-com-MongoDB
---
2  .Instale as dependências:

        npm install

3.  Configure o arquivo .env com sua string de conexão MongoDB:
  
        MONGO_URI=mongodb+srv://<usuário>:<senha>@cluster.mongodb.net/nomeDoBanco

5.  Inicie o servidor:

        npm start

6.  Acesse no navegador:

        http://localhost:3000


⚖️ Licença

MIT License

Copyright (c) 2024 Luana Cristina da Silva

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.



