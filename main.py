import produtos
import pedidos

def exibir_menu():
    print("\n" + "="*30)
    print("  Sistema de gestão para restaurantes")
    print("="*30)
    print("1. Cadastrar Produto")
    print("2. Listar Produtos (Cardápio)")
    print("3. Realizar Pedido")
    print("4. Ver Relatórios e Vendas")
    print("5. Sair")
    print("="*30)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            produtos.cadastrar_produto()
        elif opcao == "2":
            produtos.listar_produtos()
        elif opcao == "3":
            pedidos.realizar_pedido()
        elif opcao == "4":
            pedidos.exibir_relatorios()
        elif opcao == "5":
            print("\nEncerrando o sistema. Até mais!")
            break
        else:
            print("❌ Opção inválida! Escolha um número de 1 a 5.")

# Garante que o programa só rode se for executado diretamente
if __name__ == "__main__":
    main()
