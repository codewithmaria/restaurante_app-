import streamlit as st
import produtos
import pedidos

# configura as informações iniciais da aba do navegador
st.set_page_config(page_title="Gestão de Restaurante", page_icon="🍔", layout="centered")

# Cabeçalho da aplicação web
st.title("🍔 Sistema de Gestão de Pedidos")
st.caption("Arquitetura Modular em Python com interface Streamlit")
st.write("---")

# menu de navegação lateral (vai substituir o loop 'while' do terminal)
opcao = st.sidebar.radio(
    "Navegue pelo Sistema:",
    [
        "1. Ver Cardápio / Listar Produtos", 
        "2. Cadastrar Produto", 
        "3. Realizar Pedido", 
        "4. Relatórios de Vendas"
    ]
)

# direciona os módulos de acordo com a escolha do usuário
if opcao == "1. Ver Cardápio / Listar Produtos":
    produtos.listar_produtos()

elif opcao == "2. Cadastrar Produto":
    produtos.cadastrar_produto()

elif opcao == "3. Realizar Pedido":
    pedidos.realizar_pedido()

elif opcao == "4. Relatórios de Vendas":
    pedidos.exibir_relatorios()
