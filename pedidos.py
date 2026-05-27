from dados import cardapio, historico_pedidos

def realizar_pedido():
    print("\n--- NOVO PEDIDO ---")
    if not cardapio:
        print("❌ Não é possível realizar pedidos. O cardápio está vazio.")
        return

    itens_pedido = []
    
    while True:
        try:
            codigo = int(input("Digite o código do produto (ou 0 para finalizar/cancelar): "))
            if codigo == 0:
                break

            # buscando o produto pelo código
            produto_encontrado = None
            for produto in cardapio:
                if produto["codigo"] == codigo:
                    produto_encontrado = produto
                    break

            if not produto_encontrado:
                print("❌ Produto não encontrado. Tente novamente.")
                continue

            quantidade = int(input(f"Quantidade de '{produto_encontrado['nome']}': "))
            if quantidade <= 0:
                print("❌ A quantidade deve ser maior que zero.")
                continue

            # guardando o item de forma temporária
            itens_pedido.append({
                "produto": produto_encontrado,
                "quantidade": quantidade
            })
            print(f"✔️ {quantidade}x {produto_encontrado['nome']} adicionado ao carrinho.")
            
        except ValueError:
            print("❌ Entrada inválida. Digite apenas números.")

    if not itens_pedido:
        print("Pedido cancelado ou nenhum item foi adicionado.")
        return

    # calculando o total do pedido
    total_pedido = sum(item["produto"]["preco"] * item["quantidade"] for item in itens_pedido)
    
    # salvando o histórico
    novo_pedido = {
        "id": len(historico_pedidos) + 1,
        "itens": itens_pedido,
        "total": total_pedido
    }
    historico_pedidos.append(novo_pedido)

    # exibição da tela
    print("\n--- RESUMO DO PEDIDO ---")
    for item in itens_pedido:
        subtotal = item["produto"]["preco"] * item["quantidade"]
        print(f"{item['quantidade']}x {item['produto']['nome']} - R$ {subtotal:.2f}")
    print("-" * 30)
    print(f"TOTAL A PAGAR: R$ {total_pedido:.2f}")
    print("------------------------")

def exibir_relatorios():
    print("\n--- RELATÓRIO DO SISTEMA ---")
    total_vendas = len(historico_pedidos)
    
    if total_vendas == 0:
        print("Nenhum pedido foi realizado até o momento.")
        return

    faturamento_total = sum(pedido["total"] for pedido in historico_pedidos)
    
    # lógica para saber qual o produto mais vendido usando um dicionário de contagem
    contagem_produtos = {}
    for pedido in historico_pedidos:
        for item in pedido["itens"]:
            nome_prod = item["produto"]["nome"]
            contagem_produtos[nome_prod] = contagem_produtos.get(nome_prod, 0) + item["quantidade"]

    produto_mais_vendido = max(contagem_produtos, key=contagem_produtos.get)
    qtd_mais_vendido = contagem_produtos[produto_mais_vendido]

    print(f"Quantidade total de pedidos: {total_vendas}")
    print(f"Faturamento bruto total  : R$ {faturamento_total:.2f}")
    print(f"Produto mais vendido     : {produto_mais_vendido} ({qtd_mais_vendido} unidades)")
