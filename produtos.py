from dados import cardapio

def cadastrar_produto():
    print("\n--- CADASTRO DE PRODUTO ---")
    try:
        codigo = int(input("Digite o código do produto: "))
        
        # Validação: Verifica se o produto já existe no cardápio
        for produto in cardapio:
            if produto["codigo"] == codigo:
                print("❌ Erro: Já existe um produto com este código!")
                return
        
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: R$ "))
        
        # Adiciona o novo dicionário à lista
        novo_produto = {"codigo": codigo, "nome": nome, "preco": preco}
        cardapio.append(novo_produto)
        print(f"✔️ Produto '{nome}' cadastrado com sucesso!")
    except ValueError:
        print("❌ Erro: Entrada inválida! Digite números para código e preço.")

def listar_produtos():
    print("\n--- CARDÁPIO ATUAL ---")
    if not cardapio:
        print("O cardápio está vazio.")
        return
    
    # Uso do laço 'for' para percorrer dicionários conforme o Módulo 5
    print(f"{'Código':<8}{'Nome do Produto':<25}{'Preço':<10}")
    print("-" * 43)
    for produto in cardapio:
        print(f"{produto['codigo']:<8}{produto['nome']:<25}R$ {produto['preco']:.2f}")
