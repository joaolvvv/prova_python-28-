import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Acidentes por dia da semana",
    page_icon="🚦",
    layout="centered"
)


st.title("Painel de acidentes por dia da semana")
st.header("Quantidade de acidentes registrados em 2023 e 2024")


@st.cache_data
def carregar_dados():
    dados = pd.read_csv("acidentes.csv")
    return dados

dados = carregar_dados()


ordem_dias = [
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo"
]


total_por_dia = (
    dados.groupby("dia_semana")
    .size()
    .reindex(ordem_dias, fill_value=0)
    .reset_index()
)

total_por_dia.columns = ["Dia da semana", "Total de acidentes"]


st.sidebar.header("Visualização")
visualizacao = st.sidebar.radio(
    "Escolha como deseja visualizar os dados:",
    ["Tabela", "Gráfico"]
)

if visualizacao == "Tabela":
    st.subheader("Tabela de acidentes por dia")
    st.dataframe(total_por_dia, use_container_width=True, hide_index=True)

else:
    st.subheader("Gráfico de acidentes por dia")
    grafico = px.bar(
        total_por_dia,
        x="Dia da semana",
        y="Total de acidentes",
        title="Total de acidentes por dia da semana",
        labels={
            "Dia da semana": "Dia da semana",
            "Total de acidentes": "Total de acidentes"
        },
        text="Total de acidentes"
    )
    grafico.update_traces(textposition="outside")
    grafico.update_layout(xaxis_title="Dia da semana", yaxis_title="Total de acidentes")
    st.plotly_chart(grafico, use_container_width=True)
    
st.caption("Fonte dos dados: https://basedosdados.org/")
