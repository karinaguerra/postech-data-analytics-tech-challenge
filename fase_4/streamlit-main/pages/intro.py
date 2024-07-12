import streamlit as st
import pandas as pd
# from tabs.intro.eia_tab import IntroEIATab
# from tabs.intro.ipea_tab import IntroIPEATab
# from tabs.intro.meta_prophet import IntroMetaProphet
# from tabs.intro.petroleo_brent_tab import IntroPetroleoBrentTab
# from tabs.intro.tensorflow_keras_lstm import IntroTensorflowKerasLSTM
from util.constantes import TITULO_EDA, TITULO_PRINCIPAL
from util.layout import output_layout
import plotly.express as px
from util.load_data_limpo import main

st.set_page_config(
    page_title=f"{TITULO_EDA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

# Carregamento dos dado (load_data.py)
df_ipea_eda = main()

# Autor 
with st.sidebar:
    st.caption("<small>:orange[Criado por:]</small>", unsafe_allow_html=True)
    st.write("Karina Guerra do Nacimento")
    st.write("RM 352525")
    
# Titulo e subtitulo
with st.container():
    st.title("EDA - Análise Exploratória de Dados")
    st.subheader("História do Preço do Petróleo Brent")

    st.write("""
        O preço do petróleo Brent, uma referência global para o valor do petróleo, tem sido moldado por diversos eventos históricos significativos desde 1987 até os dias atuais, em 2024. Esses eventos não só influenciaram os mercados financeiros, mas também tiveram impactos profundos na economia global e na geopolítica. A seguir, destacamos alguns dos principais pontos históricos que afetaram o preço do petróleo Brent ao longo deste período:
        """)
    
    st.caption("<small>:orange[Para **navegar entre os pontos históricos**, posicione o mouse sobre, **segure a tecla [SHIFT]** e utilize o **scroll do mouse**.]</small>", unsafe_allow_html=True)

    # Cria as abas
    tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9  = st.tabs(["Black Monday", "Guerra do Golfo", "11 de Setembro", "Crise do Subprime", "Falência do Lehman Brothers", "Sanções contra o Irã", "Petróleo de Xisto", "Retirada do Acordo Nuclear EUA-Irã", "Pandemia de COVID-19", "Guerra na Ucrânia"])

    # Conteúdo da aba "Black Monday"
    with tab0:
        st.write("<large>**Black Monday (1987):**</large>", unsafe_allow_html=True)
        st.write("""Em 19 de outubro de 1987, os mercados financeiros globais sofreram uma queda drástica, conhecida como Black Monday, que resultou em uma volatilidade significativa nos preços do petróleo.""")

    # Conteúdo da aba "Guerra do Golfo"
    with tab1:
        st.write("<large>**Guerra do Golfo (1990-1991):**</large>", unsafe_allow_html=True)
        st.write("""A invasão do Kuwait pelo Iraque em agosto de 1990 e a subsequente Guerra do Golfo causaram um aumento acentuado nos preços do petróleo devido às preocupações com a oferta.""")

    # Conteúdo da aba "11 de Setembro"
    with tab2:
        st.write("<large>**11 de Setembro (2001):**</large>", unsafe_allow_html=True)
        st.write(""" 
            Os ataques terroristas de 11 de setembro de 2001 nos Estados Unidos provocaram uma incerteza econômica global, impactando os preços do petróleo.
        """)

    # Conteúdo da aba "Crise do Subprime"
    with tab3:
        st.write("<large>**Crise do Subprime (2007-2010):**</large>", unsafe_allow_html=True)
        st.write("""
            A crise financeira global, iniciada com o colapso do mercado imobiliário dos EUA, levou a uma recessão econômica que afetou a demanda por petróleo, resultando em flutuações significativas nos preços.
        """)

    # Conteúdo da aba "Falência do Lehman Brothers"
    with tab4:
        st.write("<large>**Falência do Lehman Brothers (15 de setembro de 2008)**</large>", unsafe_allow_html=True)
        st.write(""" 
            A falência do banco de investimento Lehman Brothers foi um marco da crise financeira, causando um colapso nos mercados e afetando drasticamente os preços do petróleo.
        """)

    # Conteúdo da aba "Sanções contra o Irã"
    with tab5:
        st.write("<large>**Sanções contra o Irã:**</large>", unsafe_allow_html=True)
        st.write(""" 
            As sanções econômicas impostas ao Irã, principalmente relacionadas ao seu programa nuclear, impactaram a oferta de petróleo no mercado global, influenciando os preços.
        """)

    # Conteúdo da aba "Petróleo de Xisto"
    with tab6:
        st.write("<large>**Petróleo de Xisto (2015):**</large>", unsafe_allow_html=True)
        st.write(""" 
            A revolução do petróleo de xisto nos Estados Unidos aumentou a oferta global de petróleo, resultando em uma queda nos preços.
        """)

    # Conteúdo da aba "Retirada do Acordo Nuclear EUA-Irã"
    with tab7:
        st.write("<large>**Retirada do Acordo Nuclear EUA-Irã (8 de maio de 2018):**</large>", unsafe_allow_html=True)
        st.write(""" 
            A decisão dos Estados Unidos de se retirar do acordo nuclear com o Irã trouxe incertezas ao mercado de petróleo, elevando os preços devido ao potencial de novas sanções.
        """)

    # Conteúdo da aba "Pandemia de COVID-19"
    with tab8:
        st.write("<large>**Pandemia de COVID-19 (2020-2023):**</large>", unsafe_allow_html=True)
        st.write(""" 
            A pandemia global de COVID-19 causou uma queda sem precedentes na demanda por petróleo devido a lockdowns e restrições de viagem, resultando em uma queda acentuada nos preços, seguida por uma recuperação à medida que a economia global começou a se recuperar.
        """)

    # Conteúdo da aba "Guerra na Ucrânia"
    with tab9:
        st.write("<large>**Guerra na Ucrânia (2022~):**</large>", unsafe_allow_html=True)
        st.write(""" 
            A invasão da Ucrânia pela Rússia em 2022 criou uma nova onda de incerteza e volatilidade nos mercados de petróleo, devido às preocupações com a oferta e as sanções impostas à Rússia.
        """)


# Função para carregar e preparar os dados
def load_data_decada():
    df_ipea_eda["data"] = pd.to_datetime(df_ipea_eda["data"])
    df_ipea_eda.set_index("data", inplace=True)
    df_ipea_eda["decada"] = df_ipea_eda.index.year // 10 * 10
    return df_ipea_eda

# Função para criar o gráfico de histórico
def history_graph(df_ipea_eda, decada=None):
    if decada is not None:
        df_decada = df_ipea_eda[df_ipea_eda["decada"] == decada]
    else:
        df_decada = df_ipea_eda
    
    pontos_destaque = []
    destaques = [
        {"data": "1987-10-19", "legenda": "Black Monday"},
        {"data": "1990-08-02", "legenda": "Invasão do Kuwait"},
        {"data": "2007-07-24", "legenda": "Crise do subprime"},
        {"data": "2008-09-15", "legenda": "Falência Lehman Brothers"},
        {"data": "2012-01-23", "legenda": "Embargo contra Irã"},
        {"data": "2015-01-13", "legenda": "Petróleo de xisto"},
        {"data": "2018-05-08", "legenda": "Retirada nuclear EUA-Irã"},
        {"data": "2020-03-11", "legenda": "Covid 19"},
        {"data": "2022-02-24", "legenda": "Guerra Ucrânia"}
    ]

    for destaque in destaques:
        data = pd.to_datetime(destaque["data"])
        if data in df_decada.index:
            pontos_destaque.append({
                "data": data,
                "destaque": df_decada.loc[data, "valor"],
                "legenda": destaque["legenda"]
            })

    df_pontos_destaque = pd.DataFrame(pontos_destaque)

    fig1 = px.line(df_decada.reset_index(), x="data", y="valor")
    fig1.update_traces(line_color="orange")

    if not df_pontos_destaque.empty:
        fig1.add_trace(px.scatter(df_pontos_destaque, x="data", y="destaque").data[0])

        for ponto in pontos_destaque:
            fig1.add_annotation(x=ponto["data"], y=ponto["destaque"],
                               yshift=25,
                               text=ponto["legenda"],
                               showarrow=False,
                               font=dict(color="white"),
                               bgcolor="tomato",
                               bordercolor="tomato",
                               #borderwidth=1,
                               borderpad=4)

    fig1.update_traces(marker=dict(color="tomato", size=12, symbol="x"))

    fig1.update_layout(title="Pontos históricos que influenciaram o preço do petróleo bruto",
                      xaxis_title="Período",
                      yaxis_title="Valor (US$)")

    st.plotly_chart(fig1)

# Carregar dados
df_ipea_eda = load_data_decada()

# Criar selectbox para selecionar a década
with st.container():
    decadas = df_ipea_eda["decada"].unique()
    opcoes_decadas = ["Todas as Décadas"] + list(decadas)
    decada_selecionada = st.selectbox("Selecione uma década", opcoes_decadas)

# Chamar a função para criar o gráfico com a década selecionada
if decada_selecionada == "Todas as Décadas":
    history_graph(df_ipea_eda)
else:
    history_graph(df_ipea_eda, int(decada_selecionada))


with st.container():
    st.write("""
            Este gráfico ilustra como esses eventos históricos influenciaram o preço do petróleo Brent, fornecendo uma visão abrangente das dinâmicas do mercado de petróleo ao longo das últimas décadas.
             """)

with st.container():
    st.write("---")
    st.subheader("Variação percentual média do preço do petróleo em relação ao ano anterior")

    st.write("""
            Analisando o gráfico de variação percentual média do preço do petróleo em relação ao ano anterior, podemos observar como eventos históricos significativos influenciaram essas variações ao longo dos anos. Vamos comentar alguns desses eventos destacados no gráfico:
        """)
    
    st.caption("<small>:orange[Para **navegar entre os pontos históricos**, posicione o mouse sobre, **segure a tecla [SHIFT]** e utilize o **scroll do mouse**.]</small>", unsafe_allow_html=True)

    # Cria as abas
    tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7  = st.tabs(["Black Monday", "Invasão do Kuwait", "Crise do Subprime", "Falência do Lehman Brothers", "Petróleo de Xisto", "Retirada do Acordo Nuclear EUA-Irã", "Pandemia de COVID-19", "Guerra na Ucrânia"])

    # Conteúdo da aba "Black Monday"
    with tab0:
        st.write("<large>19/10/1987 - **Black Monday**</large>", unsafe_allow_html=True)
        st.write("""A queda acentuada dos mercados financeiros globais em 1987, conhecida como Black Monday, resultou em uma volatilidade significativa nos preços do petróleo. Embora a queda imediata tenha sido seguida por uma recuperação, a incerteza econômica causada por este evento levou a flutuações no preço do petróleo nos anos seguintes.""")

    # Conteúdo da aba "Invasão do Kuwait"
    with tab1:
        st.write("<large>02/08/1990 - **Invasão do Kuwait**</large>", unsafe_allow_html=True)
        st.write("""A invasão do Kuwait pelo Iraque em agosto de 1990 levou à Guerra do Golfo, resultando em um aumento imediato nos preços do petróleo devido às preocupações com a oferta. Este evento está claramente refletido no gráfico com um pico positivo nos anos 1990.""")

    # Conteúdo da aba "Crise do Subprime"
    with tab2:
        st.write("<large>24/07/2007 - **Crise do Subprime**</large>", unsafe_allow_html=True)
        st.write("""
           A crise financeira desencadeada pela bolha imobiliária nos Estados Unidos, conhecida como a crise do subprime, começou a impactar os mercados financeiros em 2007. A incerteza econômica levou a uma diminuição na demanda por petróleo, resultando em uma queda nos preços. O impacto total foi sentido mais fortemente em 2008, após a falência do Lehman Brothers.
        """)

    # Conteúdo da aba "Falência do Lehman Brothers"
    with tab3:
        st.write("<large>15/09/2008 - **Falência do Lehman Brothers**</large>", unsafe_allow_html=True)
        st.write(""" 
            A falência do Lehman Brothers marcou o ponto alto da crise financeira global, resultando em uma queda acentuada na demanda por petróleo e, consequentemente, uma queda nos preços. Esse evento está refletido no gráfico como uma variação percentual negativa significativa.
        """)

    # Conteúdo da aba "Petróleo de Xisto"
    with tab4:
        st.write("<large>13/01/2015 - **Petróleo de Xisto**</large>", unsafe_allow_html=True)
        st.write(""" 
            O aumento na produção de petróleo de xisto nos Estados Unidos levou a um aumento na oferta global de petróleo, resultando em uma queda nos preços. Este evento está refletido no gráfico com uma variação percentual negativa.
        """)

    # Conteúdo da aba "Retirada do Acordo Nuclear EUA-Irã"
    with tab5:
        st.write("<large>08/05/2018 - **Retirada do Acordo Nuclear EUA-Irã**</large>", unsafe_allow_html=True)
        st.write(""" 
            A decisão dos Estados Unidos de se retirar do acordo nuclear com o Irã e reimpor sanções resultou em novas preocupações com a oferta de petróleo, levando a um aumento nos preços. Contudo, em 2018, essa decisão refletiu no gráfico como uma variação percentual negativa.
        """)

    # Conteúdo da aba "Pandemia de COVID-19"
    with tab6:
        st.write("<large>11/03/2020 - **Pandemia de COVID-19**</large>", unsafe_allow_html=True)
        st.write(""" 
            A pandemia de COVID-19 resultou em uma queda abrupta na demanda global por petróleo devido às restrições de mobilidade e à desaceleração econômica. Contudo, apesar desse evento, a variação percentual média do preço do petróleo em 2020 foi positiva.
                 """)

    # Conteúdo da aba "Guerra na Ucrânia"
    with tab7:
        st.write("<large>24/02/2022 - **Guerra na Ucrânia**</large>", unsafe_allow_html=True)
        st.write(""" 
            A invasão da Ucrânia pela Rússia em fevereiro de 2022 resultou em preocupações com a oferta global de petróleo, levando a um aumento nos preços. Este evento está refletido no gráfico como uma variação percentual positiva.
        """)

    # Calcular a variação percentual média do preço do petróleo em relação ao ano anterior
    df_ipea_eda['var_pct_ano_anterior'] = (df_ipea_eda['valor'] - df_ipea_eda['valor'].shift(1)) / df_ipea_eda['valor'].shift(1) * 100

    # Agrupar por ano e calcular a média da variação percentual
    df_ano = df_ipea_eda.groupby('ano')['var_pct_ano_anterior'].mean().reset_index()

    # Adicionar uma coluna para cores baseadas nos valores
    df_ano['color'] = df_ano['var_pct_ano_anterior'].apply(lambda x: 'tomato' if x < 0 else 'orange')

    # Criar um gráfico de barras usando Plotly
    fig = px.bar(df_ano, x='ano', y='var_pct_ano_anterior', 
                title='Variação percentual média do preço do petróleo em relação ao ano anterior',
                labels={'ano': 'Ano', 'var_pct_ano_anterior': 'Variação percentual (%)'},
                color='color',  # Usar a coluna de cores para a cor das barras
                color_discrete_map={'tomato': 'tomato', 'orange': 'orange'})  # Definir o mapeamento de cores

    fig.update_layout(xaxis_title='Ano', yaxis_title='Variação percentual (%)')
    fig.update_layout(showlegend=False)

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig)
    
    st.write("---")

def media_graph(df_ipea_eda_filtrado):
    fig = px.box(df_ipea_eda_filtrado, x='ano', y='valor',
                 labels={'ano': 'Período', 'valor': 'Valor (US$)'},
                 color_discrete_sequence=['orange'])

    fig.update_layout(
        xaxis=dict(
            title=dict(font=dict(size=14)),
            tickfont=dict(size=12)
        ),
        yaxis=dict(
            title=dict(font=dict(size=14)),
            tickfont=dict(size=12),
        ),
    )

    st.plotly_chart(fig)

# Função para calcular as métricas
def calcular_metricas(df):
    total = df['valor'].sum()
    media = df['valor'].mean()
    maximo = df['valor'].max()
    minimo = df['valor'].min()
    return total, media, maximo, minimo

# Criar selectbox para selecionar a década
with st.container():
    st.subheader("Média de preço do Petróleo Brent por Ano")

    media_d = df_ipea_eda["decada"].unique()
    o_decada = ["Todas as Décadas"] + list(media_d)
    decada_select= st.selectbox("Selecione uma década", o_decada, key="decada_select")

    if decada_select == "Todas as Décadas":
        df_filtrado = df_ipea_eda
    else:
        df_filtrado = df_ipea_eda[df_ipea_eda["decada"] == int(decada_select)]

    # Calcular as métricas com base nos dados filtrados
    total, media, maximo, minimo = calcular_metricas(df_filtrado)

    col1, col2, col3, col4= st.columns(4)
    col1.metric("Total", f"$ {total:,.2f}")
    col2.metric("Média", f"$ {media:,.2f}")
    col3.metric("Máximo", f"$ {maximo:,.2f}")
    col4.metric("Mínimo", f"$ {minimo:,.2f}")

    # Chamar a função para criar o gráfico com a década selecionada
    media_graph(df_filtrado)

    st.write("""
    O gráfico acima mostra a média de preço do Petróleo Brent por ano em um box plot. O box plot é uma ferramenta gráfica que nos ajuda a visualizar a distribuição dos dados e identificar valores discrepantes, conhecidos como outliers.\n
    Os outliers são pontos de dados que estão significativamente distantes do restante do conjunto de dados. Eles podem indicar erros nos dados, variações naturais extremas ou padrões interessantes que merecem investigação adicional. É importante identificá-los porque podem distorcer análises estatísticas e modelos preditivos, levando a conclusões incorretas ou imprecisas.\n
    O box plot mostra a mediana do preço do Petróleo Brent (linha no meio do retângulo), os quartis (limites do retângulo), e o intervalo interquartil (IQR), que é a faixa onde está concentrada a maior parte dos dados. Os "whiskers" (linhas que se estendem além do retângulo) mostram até onde os dados se estendem, excluindo os outliers. Os pontos fora dos whiskers são considerados outliers e são representados individualmente.\n
    Este tipo de gráfico nos ajuda a ter uma visão abrangente da distribuição dos preços ao longo dos anos e a identificar anos com variações significativas de preço em relação à média. É uma ferramenta valiosa para analisar a volatilidade do mercado de petróleo ao longo do tempo.
    """)

with st.container():
    st.write("---")
    st.subheader("Distribuição de Preço do Petróleo Brent")

    # Criando o gráfico Plotly
    fig3 = px.histogram(df_ipea_eda, x="valor", marginal="violin", hover_data=df_ipea_eda.columns)
    fig3.update_traces(marker_color='orange')
    fig3.update_layout(xaxis_title='Valor (US$)',
                      yaxis_title='Densidade')

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig3)

    st.write("""
        O histograma representado acima mostra a distribuição dos preços do petróleo Brent ao longo do tempo. Esta forma de visualização é extremamente útil para identificar a dispersão dos dados e a concentração dos preços em torno de um valor central, bem como a presença de *outliers*.\n
        Ao analisar este gráfico, podemos observar que o preço do petróleo Brent teve variações ao longo do tempo, com uma tendência a valores mais baixos e com pontos de picos específicos, que estão associados a eventos históricos significativos que causaram flutuações nos preços, como crises econômicas, guerras, pandemias, ou mudanças na produção de petróleo, que é possível visualizar no gráfico de :orange[pontos históricos que influenciaram o preço do petróleo bruto].\n
        Em resumo, o histograma com a visualização marginal de violino oferece uma compreensão profunda da dinâmica dos preços do petróleo Brent, destacando tanto a distribuição geral quanto as variações ao longo do tempo.
        """)
