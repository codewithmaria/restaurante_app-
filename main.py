import sys
import os
import streamlit as st

# mapeia a pasta atual de execução
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import produtos
import pedidos

st.set_page_config(page_title="Gestão de Restaurante", page_icon="🍔", layout="centered")

st.title("🍔 Sistema de Gestão de Pedidos")
st.caption("Arquitetura Modular em Python com interface Streamlit")
st.write("---")

opcao = st.sidebar.radio(
    "Navegue pelo Sistema:",
    [
        "1. Ver Cardápio / Listar Produtos", 
        "2. Cadastrar Produto", 
        "3. Realizar Pedido", 
        "4. Relatórios de Vendas"
    ]
)

if opcao == "1. Ver Cardápio / Listar Produtos":
    produtos.listar_produtos()

elif opcao == "2. Cadastrar Produto":
    produtos.cadastrar_produto()

elif opcao == "3. Realizar Pedido":
    pedidos.realizar_pedido()

elif opcao == "4. Relatórios de Vendas":
    pedidos.exibir_relatorios()
