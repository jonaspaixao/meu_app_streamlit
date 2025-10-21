import streamlit as st
import pandas as pd

# Título
st.title("📊 Tabela de Fatores de Correção Monetária")

# Carregar CSV
df = pd.read_csv("Fatores_IPCA_IPCA_E_INPC_INCC_IGPM_TR_SELIC_ENCOGE.csv", sep=";")

# Mostrar tabela
st.dataframe(df)

# Botão de download abaixo da tabela
st.download_button(
    label="⬇️ Baixar a tabela",
    data=df.to_csv(index=False, sep=";").encode("utf-8"),
    file_name="indices_correcao.csv",
    mime="text/csv"
)


















