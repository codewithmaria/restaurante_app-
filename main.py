import sys
import os
import streamlit as st

# Configuração absoluta de caminhos para o servidor local e nuvem
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuração da página web (Deve ser o primeiro comando Streamlit)
st.set_page_config(page_title="Gestão de Restaurante", page_icon="🍔", layout="centered")

# --- CONTROLE DE SESSÃO E LOGIN ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if "cardapio" not in st.session_state:
    st.session_state.cardapio = [
        {"codigo": 1, "nome": "Hambúrguer Artesanal", "preco": 28.50},
        {"codigo": 2, "nome": "Batata Frita Média", "preco": 12.00},
        {"codigo": 3, "nome": "Refrigerante Lata", "preco": 6.00},
    ]

if "historico_pedidos" not in st.session_state:
    st.session_state.historico_pedidos = []

if "carrinho_atual" not in st.session_state:
    st.session_state.carrinho_atual = []


# --- FLUXO DE RENDERIZAÇÃO ---
if not st.session_state.autenticado:
    # Se não estiver logado, importa e mostra estritamente a tela de login
    import login
    login.exibir_tela_login()
else:
    # Se estiver logado, libera o acesso aos módulos originais do sistema
    import produtos
    import pedidos

    st.title("🍔 Podrão do Erick")
    st.caption("Aqui a sua satisfação é garatida")
    st.write("---")

    # Menu de navegação lateral original [cite: 33, 34]
    opcao = st.sidebar.radio(
        "Navegue pelo Sistema:",
        [
            "1. Ver Cardápio / Listar Produtos", [cite: 36]
            "2. Cadastrar Produto", [cite: 35]
            "3. Realizar Pedido", [cite: 37]
            "4. Relatórios de Vendas" [cite: 38]
        ]
    )
    
    st.sidebar.write("---")
    # Botão de Logout para encerrar a sessão com segurança 
    if st.sidebar.button("🚪 Sair do Sistema"): [cite: 39]
        st.session_state.autenticado = False
        st.session_state.carrinho_atual = [] # Limpa o carrinho de segurança
        st.rerun()

    # Direcionamento dos módulos baseados no menu [cite: 63, 64]
    if opcao == "1. Ver Cardápio / Listar Produtos":
        produtos.listar_produtos() [cite: 66]

    elif opcao == "2. Cadastrar Produto":
        produtos.cadastrar_produto() [cite: 65]

    elif opcao == "3. Realizar Pedido":
        pedidos.realizar_pedido() [cite: 67]

    elif opcao == "4. Relatórios de Vendas":
        pedidos.exibir_relatorios()
