# ********** Importa o streamlit (site), as classes do arquivo main e as funções do database ***************
import streamlit as st
from main import Cliente, Animal
from database import listar_clientes, buscar_cliente_por_cpf

# ************ configuração da página ********************
st.set_page_config(page_title="Petshop Manager", page_icon="🐾")
                   
# ************ titulo principal **************************
st.title("🐕 PetShop Client Manager 🐈")
st.markdown("---")

# ************ menu lateral ******************************
menu = st.sidebar.selectbox(
    "Escolha uma opção",
    ["📝 Cadastrar cliente", "📋 Listar clientes", "🔍 Buscar cliente"]
)

# ************ PAG 1 cadastrar cliente ********************
if menu == "📝 Cadastrar cliente":
    st.subheader("Novo cadastro de cliente")

    with st.form("form_cadastro"):
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("Nome completo*")
            cpf = st.text_input("CPF*")
            telefone = st.text_input("Telefone*")
        
        with col2:
            endereco = st.text_input("Endereço*")
            email = st.text_input("Email*")
        
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            if nome and cpf:
                cliente = Cliente(nome, endereco, telefone, email, cpf)
                sucesso, mensagem = cliente.salvar_no_banco() #chama a função que salva no database
                
                if sucesso:
                    st.success(mensagem)
                else:
                    st.error(mensagem)
            else:
                st.warning("Preencha nome e CPF (são obrigatórios)")

# ************** PAG 2 listar clientes *******************************************
elif menu == "📋 Listar clientes":
    st.subheader("Clientes Cadastrados")

    clientes = listar_clientes() #chama a função que lista os clientes

    if clientes:
        for cliente in clientes:
            with st.expander(f"{cliente[1]} - CPF: {cliente[5]}"):
                st.write(f"**Endereço:**{cliente[2] or 'Não informado'}")
                st.write(f"**Telefone:**{cliente[3] or 'Não informado'}")
                st.write(f"**E-mail:**{cliente[4] or 'Não informado'}")

    else:
        st.info("Nenhum ciente cadastrado ainda.")

# ************** PAG 3 buscar cliente *********************************************
elif menu == "Buscar cliente🔍":
    st.subheader("Buscar cliente por CPF")

    cpf_busca = st.text_input("Digite o CPF do cliente")

    if st.button("Buscar"):
        resultado = Cliente.buscar_por_cpf(cpf_busca) #chama a função que busca o cliente pelo cpf
        
        if resultado:
            st.success("Cliente encontrado!")
            st.write(f"**Nome:** {resultado[1]}")
            st.write(f"**Endereço:** {resultado[2]}" or 'Não informado')
            st.write(f"**Telefone:** {resultado[3]}" or 'Não informado')
            st.write(f"**E-mail:** {resultado[4]}" or 'Não informado')
            st.write(f"**CPF:** {resultado[5]}" or 'Não informado')
    else:
        st.error("Cliente não ecnotrado!")

