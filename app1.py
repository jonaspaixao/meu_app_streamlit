import streamlit as st
import pandas as pd

# Carregar CSV
df = pd.read_csv("Fatores_IPCA_IPCA_E_INPC_INCC_IGPM_TR_SELIC_ENCOGE.csv", sep=";")

# Mostrar tabela
#st.title("Tabela de Índices de Correção Monetária")
with st.expanded("Tabela de Índices de Correção Monetária", expanded=True):
st.dataframe(df)




