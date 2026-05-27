from dados import cardapio, historico_pedidos

def realizar_pedido():
    print("\n--- REALIZAR NOVO PEDIDO ---")
    if not cardapio:
        print("Não há produtos cadastrados para fazer um pedido.")
        return

    carrinho = []
    
    while True:
        codigo_busca = int(input("\nDigite o código do produto (ou 0 para finalizar o carrinho): "))
        if codigo_busca == 0:
            break
            
        # Busca se o produto existe usando estrutura de decisão (Módulo 4)
        produto_encontrado = None
        for produto in cardapio:
            if produto["codigo"] == codigo_busca:
                produto_encontrado = produto
                break
                
        if produto_encontrado:
            quantidade = int(input(f"Quantidade de '{produto_encontrado['nome']}': "))
            if quantidade <= 0:
                print("Quantidade inválida.")
                continue
                
            carrinho.append({"produto": produto_encontrado, "quantidade": quantidade})
            print(f"✔️ {quantidade}x {produto_encontrado['nome']} adicionado ao carrinho.")
        else:
            print("❌ Produto não encontrado") # Mensagem obrigatória do PDF

    if not carrinho:
        print("Pedido cancelado (carrinho vazio).")
        return

    # Processa e calcula o total do pedido
    total_pedido = 0
    print("\n--- RESUMO DO PEDIDO ---")
    for item in carrinho:
        subtotal = item["produto"]["preco"] * item["quantidade"]
        total_pedido += subtotal
        print(f"- {item['quantidade']}x {item['produto']['nome']} : R$ {subtotal:.2f}")
        
    print(f"**Total a Pagar: R$ {total_pedido:.2f}**")
    
    # Salva no histórico geral
    pedido_finalizado = {"itens": carrinho, "total": total_pedido}
    historico_pedidos.append(pedido_finalizado)
    print("🎉 Pedido registrado com sucesso!")

def ver_pedidos():
    print("\n--- RELATÓRIOS GERAIS DO SISTEMA ---")
    total_vendas = len(historico_pedidos)
    
    if total_vendas == 0:
        print("Nenhum pedido foi realizado até o momento.")
        return

    faturamento_total = 0
    contagem_produtos = {}

    # Percorre o histórico acumulando faturamento e contando itens vendidos
    for pedido in historico_pedidos:
        faturamento_total += pedido["total"]
        for item in pedido["itens"]:
            nome = item["produto"]["nome"]
            contagem_produtos[nome] = contagem_produtos.get(nome, 0) + item["quantidade"]

    # Identifica o produto com maior volume de saída
    produto_mais_vendido = max(contagem_produtos, key=contagem_produtos.get)
    qtd_mais_vendida = contagem_produtos[produto_mais_vendido]

    # Exibe os dados do Módulo 5 (Relatórios)
    print(f"Quantidade total de pedidos: {total_vendas}")
    print(f"Valor total vendido: R$ {faturamento_total:.2f}")
    print(f"Produto mais vendido: {produto_mais_vendido} ({qtd_mais_vendida} unidades)")
