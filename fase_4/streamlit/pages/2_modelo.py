import streamlit as st
from st_pages import show_pages_from_config

show_pages_from_config("config/pages_sections.toml")
# Titulo Pagina 
# st.set_page_config(layout='centered', 
#                    page_title='Modelo')

# Autor 
with st.sidebar:
    st.caption("<small>:orange[Criado por:]</small>", unsafe_allow_html=True)
    st.write("Karina Guerra do Nacimento")
    st.write("RM 352525")
    
# Titulo e subtitulo
with st.container():
    st.title("Modelos")
    st.write(f"""
                Antes de explicar os processos dos modelos utilizados neste relatório, é importante mencionar as métricas utilizadas para avaliar a qualidade das previsões. As métricas escolhidas foram o Erro Quadrático Médio (MSE), Erro Absoluto Médio (MAE), Coeficiente de Determinação (R²) e Erro Percentual Absoluto Médio (MAPE).\n
                - **MSE:** *Mean Squared Error* (Erro Quadrático Médio) é a média dos quadrados dos erros entre os valores observados e os valores previstos pelo modelo. É uma medida que penaliza mais fortemente os erros maiores, ou seja, quanto maior o erro, maior será sua contribuição para o MSE.\n
                - **MAE:** *Mean Absolute Error* (Erro Absoluto Médio) é a média dos valores absolutos dos erros entre os valores observados e os valores previstos pelo modelo. É uma medida que não considera a direção dos erros, ou seja, erros positivos e negativos têm o mesmo peso.\n
                - **R²:** *R-squared* (Coeficiente de Determinação) é uma medida que indica a proporção da variância dos valores observados que é explicada pelo modelo. Ele varia de 0 a 1, onde 0 indica que o modelo não explica nenhuma variabilidade dos dados e 1 indica que o modelo explica toda a variabilidade.\n
                - **MAPE:** *Mean Absolute Percentage* Error (Erro Percentual Absoluto Médio) é a média dos valores absolutos dos erros percentuais entre os valores observados e os valores previstos pelo modelo. É uma medida útil para avaliar a precisão das previsões em termos percentuais.\n
                Essas métricas são importantes para avaliar o desempenho do modelo de previsão e entender o quão bem ele está se ajustando aos dados observados.
                """)
    st.write(f"""
             Para a escolha dos modelos para previsão foi baseada em critérios como robustez, adaptabilidade, eficiência computacional, interpretação dos resultados e precisão da previsão. Isso porque diferentes modelos têm diferentes capacidades de lidar com a complexidade dos dados e capturar padrões relevantes.
             \nOs modelos escolhidos foram:
             """)

with st.container():
    tab0, tab1  = st.tabs(["Prophet", "LSTM (Long Short-Term Memory)"])

    # Conteúdo da aba "Prophet"
    with tab0:
        st.write(f"""Utilizar o modelo Prophet para prever preços do petróleo Brent é interessante por várias razões, este é um modelo desenvolvido pelo Meta, fácil de usar, captura sazonalidades e tendências de longo prazo, e é robusto contra dados faltantes e outliers.
                 \n O Prophet permite a inclusão de eventos específicos, oferece flexibilidade de ajuste manual, e gera previsões rapidamente. Suas visualizações intuitivas facilitam a interpretação dos resultados, tornando-o uma ferramenta poderosa para melhorar a precisão das previsões de preços do petróleo Brent.
                 \n No geral, o Prophet é uma ferramenta poderosa e acessível para previsão de séries temporais, sendo amplamente utilizado em diversas áreas, como finanças, marketing, e-commerce e meteorologia, entre outras.
                 """)
        st.link_button("Documentação","https://facebook.github.io/prophet/docs/quick_start.html")

    # Conteúdo da aba "LSTM"
    with tab1:
        st.write(f"""Escolher um modelo LSTM (Long Short-Term Memory) para prever os preços do petróleo Brent é uma boa decisão estratégica por várias razões. 
                 \n O LSTM é uma arquitetura de rede neural recorrente para lidar com sequências temporais de longo prazo e padrões complexos. Elas são resistentes a ruídos e variabilidade nos dados, algo crucial quando se está trabalhando com dados mais voláteis como o de petróleo. Sua capacidade de lidar com previsões sequenciais as torna ideais para o mercado brent.
                 """)

        st.link_button("Documentação","https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM")
