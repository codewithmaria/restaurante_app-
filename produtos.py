from dados import cardapio

def cadastrar_produto():
    print("\n--- CADASTRO DE PRODUTO ---")
    
    try:
        codigo = int(input("Digite o código do produto (apenas números): "))
        
        # ver se o código já existe
        for produto in cardapio:
            if produto["codigo"] == codigo:
                print("❌ Erro: Já existe um produto com este código.")
                return

        nome = input("Digite o nome do produto: ").strip()
        if not nome:
            print("❌ Erro: O nome do produto não pode ser vazio.")
            return

        preco = float(input("Digite o preço do produto (Ex: 25.50): "))
        if preco <= 0:
            print("❌ Erro: O preço deve ser maior que zero.")
            return

        # add novo produto como dicionário
        novo_produto = {"codigo": codigo, "nome": nome, "preco": preco}
        cardapio.append(novo_produto)
        print(f"✔️ Produto '{nome}' cadastrado com sucesso!")
        
    except ValueError:
        print("❌ Erro: Entrada inválida. Digite números corretamente nos campos de código e preço.")

def listar_produtos():
    print("\n--- CARDÁPIO ATUAL ---")
    if not cardapio:
        print("O cardápio está vazio.")
        return

    print(f"{'Cód':<6} | {'Nome do Produto':<25} | {'Preço':<10}")
    print("-" * 46)
    for produto in cardapio:
        print(f"{produto['codigo']:<6} | {produto['nome']:<25} | R$ {produto['preco']:>7.2f}")
