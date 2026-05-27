import sys
import os

# Configuração de caminhos para evitar problemas de diretórios no GitHub Codespaces
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import produtos
import pedidos

# Menu Principal contínuo utilizando While conforme seção 5 do PDF
while True:
    print("\n================================")
    print("       MENU PRINCIPAL")
    print("================================")
    print("5. Cadastrar produto")
    print("6. Listar produtos")
    print("7. Realizar pedido")
    print("8. Ver pedidos (Relatórios)")
    print("9. Sair")
    print("================================")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "5":
        produtos.cadastrar_produto()
    elif opcao == "6":
        produtos.listar_produtos()
    elif opcao == "7":
        pedidos.realizar_pedido()
    elif opcao == "8":
        pedidos.ver_pedidos()
    elif opcao == "9":
        print("Encerrando o sistema. Até logo!")
        break # Quebra o loop contínuo finalizando o programa
    else:
        print("Opção inválida! Digite um número entre 5 e 9.")
