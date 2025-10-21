import streamlit as st
import pandas as pd

# Estilo fullscreen
st.markdown("""
    <style>
        .fullscreen-table .stDataFrame {
            height: 90vh !important;
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("Tabela de Índices de Correção Monetária")

# Carregar CSV
df = pd.read_csv("Fatores_IPCA_IPCA_E_INPC_INCC_IGPM_TR_SELIC_ENCOGE.csv", sep=";")

# Tabela com classe personalizada
with st.container():
    st.markdown('<div class="fullscreen-table">', unsafe_allow_html=True)
    st.dataframe(df)
    st.markdown('</div>', unsafe_allow_html=True)








