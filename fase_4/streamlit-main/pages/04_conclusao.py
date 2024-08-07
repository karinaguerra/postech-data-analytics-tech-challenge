import streamlit as st
from util.sidebar import sidebar_layout

st.set_page_config(
    page_title=f"Conclusão", layout="wide", initial_sidebar_state="expanded"
)

sidebar_layout()

# Titulo
with st.container():
    st.header(f"Conclusão")

    st.write(
    f"""
    A previsão de preços do petróleo Brent é crucial para empresas do setor energético e outras indústrias que dependem deste recurso. Devido à natureza volátil do mercado e aos impactos geopolíticos, métodos tradicionais de previsão muitas vezes não conseguem capturar todas as variáveis envolvidas. Nesse contexto, modelos de predição baseados em machine learning têm se mostrado ferramentas poderosas para prever os preços do petróleo Brent com maior precisão.\n
    Neste estudo, foram utilizados dois modelos de machine learning: Prophet e LSTM (Long Short-Term Memory). Os resultados demonstram que ambos os modelos possuem pontos fortes distintos na previsão de preços do petróleo Brent.\n
    Para o modelo Prophet, os resultados foram:\n
    - MSE: 23.11
    - MAE: 3.66
    - R²: 0.94
    - MAPE: 4.80%\n
    Esses resultados indicam que o Prophet é bastante eficaz em capturar tendências de longo prazo e sazonalidades, apresentando uma alta precisão nas previsões gerais.\n
    Para o modelo LSTM, os resultados foram:\n
    - MSE: 9.54
    - MAE: 2.18
    - R²: 0.97
    - MAPE: 36.19%\n
    O modelo LSTM mostrou-se superior em termos de MSE e MAE, sugerindo uma menor média de erro absoluto e quadrático. No entanto, o alto valor de MAPE indica que, em termos de erro percentual absoluto médio, o LSTM apresentou maior variação, o que pode ser atribuído à sensibilidade do modelo a grandes flutuações nos dados.\n
    Com base nessas métricas, pode-se concluir que ambos os modelos são úteis para a previsão de preços do petróleo Brent, cada um com suas vantagens específicas. O Prophet se destaca pela sua capacidade de modelar tendências e sazonalidades, sendo robusto contra outliers e faltas de dados. Já o LSTM, com sua arquitetura de rede neural recorrente, mostrou-se altamente preciso em termos de erros médios absolutos e quadráticos, sendo ideal para capturar padrões complexos e sequenciais nos dados.\n
    Deste modo, a junção de ambos os modelos pode possibilitar uma abordagem mais robusta para a previsão de preços do petróleo Brent. Utilizar essas ferramentas de machine learning pode ajudar as empresas a mitigar riscos, planejar estrategicamente e aproveitar oportunidades no mercado volátil de petróleo Brent.\n
     """)