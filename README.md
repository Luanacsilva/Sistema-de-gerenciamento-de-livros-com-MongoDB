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

Este projeto está sob a licença MIT


