import streamlit as st

def exibir_tela_login():
    st.markdown("<h2 style='text-align: center;'> Acesso ao Podrão</h2>", unsafe_allow_html=True)
    
    # Centraliza o formulário de login na tela
    with st.form("formulario_login", clear_on_submit=False):
        usuario = st.text_input("Usuário:")
        senha = st.text_input("Senha:", type="password")
        botao_entrar = st.form_submit_button("Entrar", use_container_width=True)
        
        if botao_entrar:
            # Validação simples de credenciais (Pode ser alterada conforme necessário)
            if usuario == "admin" and senha == "1234":
                st.session_state.autenticado = True
                st.success("Acesso autorizado! Carregando o sistema...")
                st.rerun()
            else:
                st.error("❌ Usuário ou senha incorretos. Tente novamente.")
