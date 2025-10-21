import streamlit as st
import pandas as pd

# Título
st.title("Tabela de Índices de Correção Monetária")

# Carregar CSV
df = pd.read_csv("Fatores_IPCA_IPCA_E_INPC_INCC_IGPM_TR_SELIC_ENCOGE.csv", sep=";")

# Mostrar tabela dentro de um expander já aberto
with st.expander("Visualizar tabela completa", expanded=True):
    st.dataframe(df)






