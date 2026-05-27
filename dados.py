import streamlit as st

# inicializando o cardápio com produtos padrão se ainda não existir na sessão
if "cardapio" not in st.session_state:
    st.session_state.cardapio = [
        {"codigo": 1, "nome": "Hambúrguer Artesanal", "preco": 28.50},
        {"codigo": 2, "nome": "Batata Frita Média", "preco": 12.00},
        {"codigo": 3, "nome": "Refrigerante Lata", "preco": 6.00},
    ]

# startando o histórico de pedidos se ainda não existir
if "historico_pedidos" not in st.session_state:
    st.session_state.historico_pedidos = []

# stratando o carrinho temporário do pedido atual
if "carrinho_atual" not in st.session_state:
    st.session_state.carrinho_atual = []
