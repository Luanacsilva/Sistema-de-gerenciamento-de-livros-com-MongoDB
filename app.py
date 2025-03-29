from pymongo import MongoClient


client = MongoClient("mongodb+srv://Luana:Luana231@luana.32x2ttl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
contatos = db.contatos

def inserir_contato():
    nome = input("Adicionar contato:")
    telefone = input("telefone:")
    contatos.insert_one({"nome": nome, "telefone": telefone})
    print("📥 Contato inserido com sucesso!")

def listar_contatos():
    print("\n📄 Lista de contatos:")
    for contato in contatos.find():
        print(contato)

def atualizar_contato():
    nome = input("Digite o nome do contato")
    novo_telefone = input("Digite o novo telefone: ")
    contatos.update_one({"nome": nome}, {"$set": {"telefone": novo_telefone}})
    print("✏️ Contato atualizado!")

def excluir_contato():
    nome = input("Digite o nome do contato ")
    contatos.delete_one({"nome": nome})
    print("🗑️ Contato excluído!")

while True:
    print("\n--- MENU ---")
    print("1. Inserir contato")
    print("2. Listar contatos")
    print("3. Atualizar contato")
    print("4. Excluir contato")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        inserir_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        atualizar_contato()
    elif opcao == "4":
        excluir_contato()
    elif opcao == "5":
        print("🚪 Saindo...")
        break
    else:
        print("❌ Opção inválida. Tente novamente.")
