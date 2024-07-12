import streamlit as st
from util.constantes import TITULO_PRINCIPAL, TITULO_INTRODUCAO
from util.layout import output_layout
import warnings
import locale

warnings.filterwarnings("ignore")

# Tentando diferentes configurações de localidade para Windows
try:
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, "pt_BR")
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")
        except locale.Error:
            print("Localidade pt_BR não suportada, usando configuração padrão.")


st.set_page_config(
    page_title=f"{TITULO_INTRODUCAO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

st.subheader(f"{TITULO_PRINCIPAL}")

# Cria as abas
tab0, tab1, tab2 = st.tabs(["Introdução", "Objetivo", "Metas específicas"])

# Conteúdo da aba "Introdução"
with tab0:
    st.title('Introdução')
    st.write(
        f"""
        O nome Brent, é uma sigla utilizada para identificar o petróleo que é extraído de uma plataforma da Shell no Mar do Norte. Atualmente o termo engloba todo o petróleo dessa região comercializado na Bolsa de Londres, atendendo como uma referência de preço para os mercados europeu e asiático.\n
        O preço do petróleo Brent pode variar devido a fatores como estoque, economia, geopolítico, eventos climáticos e oferta e demanda. E estas variações têm um impacto direto nos preços de seus derivados, como óleo diesel e gasolina, com isso influenciando os custos de transporte e, consequentemente, o preço de diversas mercadorias. Esses preços são determinados principalmente pelo custo de produção e transporte.\n
        Para o mercado a análise da cotação do petróleo Brent é essencial para diversos setores econômicos, oferecendo insights valiosos para decisões estratégicas de empresas que dependem diretamente do petróleo ou são afetadas pelas flutuações de seus preços.\n 
        Prever os preços do petróleo Brent é uma tarefa fundamental. Para este estudo de caso, foram utilizados modelos preditivos de machine learning com o objetivo de prever os preços do petróleo Brent.
        """
    )

# Conteúdo da aba "Objetivo"
with tab1:
    st.title('Objetivo')
    st.write(
        f""" 
        O objetivo deste trabalho é realizar uma análise de previsão aos preços do petróleo Brent, disponíveis no site do [IPEA]("http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view"), utilizando modelos de machine learning. Dada a importância econômica e estratégica do petróleo Brent, entender as dinâmicas de preços e antecipar suas variações é crucial para diversos setores, incluindo transporte, energia e finanças.\n
        Para alcançar esse objetivo, foi realizada uma análise exploratória de dados (EDA), examinando os históricos de preços do petróleo Brent e identificando padrões, tendências e eventos significativos que impactaram seus preços ao longo do tempo. Além disso, foram analisados os principais fatores que influenciam as variações nos preços do petróleo Brent, como oferta e demanda, geopolítica, economia global, avanços tecnológicos, eventos climáticos e condições de estoque.\n
        Os modelos de machine learning aplicados foram, Prophet e LSTM (Long Short-Term Memory), para prever os preços futuros do petróleo Brent. A performance desses modelos foi avaliada com base em métricas como Erro Quadrático Médio (MSE), Erro Absoluto Médio (MAE), Coeficiente de Determinação (R²) e Erro Percentual Absoluto Médio (MAPE).\n
        Portanto, este trabalho visa compreender a variação de preço do mercado de petróleo Brent e criar previsões utilizando o machine learning.
        """
    )

# Conteúdo da aba "Metas específicas"
with tab2:
    st.title('Metas específicas')
    st.write(
        f""" 
        Criar um Dashboard Interativo:\n\n
        - Utilizar ferramentas de visualização de dados de sua escolha para construir um dashboard que apresente de forma clara e intuitiva a variação dos preços do petróleo Brent.\n\n
        - Incorporar storytelling no dashboard para destacar insights relevantes que influenciam os preços do petróleo, como situações geopolíticas, crises econômicas, demanda global por energia, entre outros.\n\n
        - Garantir que pelo menos quatro insights significativos sejam apresentados no dashboard para auxiliar na tomada de decisões.\n\n
        Desenvolver um Modelo de Machine Learning para Previsão de Preços:\n\n
        - Construir um modelo de Machine Learning para previsão diária dos preços do petróleo, considerando as características de séries temporais dos dados.\n\n
        - Integrar o modelo no storytelling do dashboard, apresentando o código utilizado e análises de performance do modelo.\n\n
        - Implementar um MVP (Minimum Viable Product) do modelo em produção utilizando Streamlit, permitindo uma visualização interativa das previsões.\n\n
        """
    )
