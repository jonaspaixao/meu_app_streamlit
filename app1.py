import streamlit as st
import pandas as pd

# Carregar CSV
df = pd.read_csv("Fatores_IPCA_IPCA_E_INPC_INCC_IGPM_TR_SELIC_ENCOGE.csv", sep=";")

# Estilo personalizado
st.markdown("""
    <style>
        .custom-button {
            display: inline-block;
            background-color: #008CBA;
            color: white;
            padding: 10px 20px;
            margin: 10px 5px;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .custom-button:hover {
            background-color: #005f73;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("📊 Índices de Correção Monetária")

# Botões destacados
st.markdown("""
<a href="#" class="custom-button">🔍 Buscar</a>
<a href="#" class="custom-button">🖥️ Tela cheia</a>
<a href="Fatores_IPCA_IPCA_E_INPC_INCC_IGPM_TR_SELIC_ENCOGE.csv" download class="custom-button">⬇️ Download CSV</a>
""", unsafe_allow_html=True)

# Mostrar tabela
st.dataframe(df)












