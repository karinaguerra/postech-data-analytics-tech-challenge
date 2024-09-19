import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from util.layout import output_layout
from util.carregar_dados import main

st.set_page_config(
    page_title=f"EDA", layout="wide"
)
output_layout()

# Carregamento dos dado (carregar_dados.py)
df_magico = main()

caminho_csv_2020 = 'fase_5/streamlit-main/data/df_2020_limpo.csv'
caminho_csv_2021 = 'fase_5/streamlit-main/data/df_2021_limpo.csv'
caminho_csv_2022 = 'fase_5/streamlit-main/data/df_2022_limpo.csv'

def carregar_dados():
    df_2020 = pd.read_csv(caminho_csv_2020)
    df_2021 = pd.read_csv(caminho_csv_2021)
    df_2022 = pd.read_csv(caminho_csv_2022)
    return df_2020, df_2021, df_2022
    
with st.container():
    st.title("Análise dos Alunos da Passos Mágicos ")
    st.subheader("Análise exploratória de dados")

    st.write(f"""
        A análise exploratória foi iniciada utilizando dados dos anos de 2020, 2021 e 2022. Primeiramente, realizou-se a limpeza e a segmentação dos dados por ano. Assim, caso um aluno tivesse informações registradas tanto para 2020 quanto para 2021, seriam gerados dois registros distintos no conjunto final, um para cada ano.
        \n\n Em seguida, foi feita a contagem inicial da quantidade de alunos por ano:
        """)
    
def mostrar_metricas_alunos_por_ano(df_magico):

    total_alunos_por_ano = df_magico.groupby('ANO')['NOME'].nunique()
    
    total_geral_alunos = df_magico['NOME'].nunique()

    col1, col2, col3, col4 = st.columns(4)
    

    anos = total_alunos_por_ano.index.tolist()
    if len(anos) > 0:
        col1.metric(f"Total de alunos em {anos[0]}", f"{total_alunos_por_ano[anos[0]]:,}")
    if len(anos) > 1:
        col2.metric(f"Total de alunos em {anos[1]}", f"{total_alunos_por_ano[anos[1]]:,}")
    if len(anos) > 2:
        col3.metric(f"Total de alunos em {anos[2]}", f"{total_alunos_por_ano[anos[2]]:,}")
    
    col4.metric("Total Geral", f"{total_geral_alunos:,}")

mostrar_metricas_alunos_por_ano(df_magico)


with st.container():
    st.header("Análise da Distribuição Etária dos Alunos")
    st.write(f"""
        Um aspecto fundamental é compreender a distribuição das idades dos alunos, conforme ilustrado nos gráficos abaixo. O primeiro gráfico é um box plot, que exibe a mediana (12 anos), o primeiro e o terceiro quartis (Q1 = 10 anos, Q3 = 14 anos), além dos valores mínimo e máximo (7 e 20 anos, respectivamente). Essa visualização é útil para identificar a dispersão das idades e eventuais valores atípicos (outliers), permitindo uma análise detalhada de como as idades se distribuem em torno da média.
        \n\n O segundo gráfico é um histograma, que mostra a frequência com que as diferentes idades aparecem na amostra de alunos. Ele permite observar a concentração de alunos em determinadas faixas etárias, destacando uma maior frequência de alunos entre 10 e 14 anos. Esse tipo de gráfico é importante para identificar tendências, como a predominância de uma faixa etária específica, além de possibilitar uma visualização mais detalhada da distribuição geral das idades.
         """)
    
st.markdown(""":orange[Para gerar o gráfico, foram removidos os valores menores que zero, considerados como outliers.]""")

with st.container():
    tab0, tab1 = st.tabs(["Média de Idade", "Histograma de Idade"])

    with tab0:
        def mostrar_grafico_idade(df_magico):
            df_idade_media = df_magico[df_magico['IDADE_ALUNO'] > 0]
            
            fig = px.box(
                df_idade_media,
                y='IDADE_ALUNO',
                labels={'IDADE_ALUNO': 'Idade dos Alunos'},
                color_discrete_sequence=['#626EF5']
            )
            
            st.plotly_chart(fig, use_container_width=True)

        if df_magico is not None:  # Verifica se o DataFrame foi carregado
            mostrar_grafico_idade(df_magico)
        else:
            st.error("Erro ao carregar os dados.")

    with tab1:
        def plot_histogram(df):
            df_filtered = df[df['IDADE_ALUNO'] > 0]

            fig = px.histogram(
                df_filtered,
                x='IDADE_ALUNO',
                labels={'IDADE_ALUNO': 'Idade dos Alunos'},
                color_discrete_sequence=['#626EF5']
            )

            fig.update_layout(
                xaxis_title='Idade dos Alunos',
                yaxis_title='Total de Alunos',
            )

            st.plotly_chart(fig, use_container_width=True)

        plot_histogram(df_magico)




st.divider()

with st.container():

    st.header("Análise das Instituições de Ensino Frequentadas pelos Alunos da ONG Passos Mágicos (2020-2021)")
    st.write(f"""
        O gráfico comparativo utilizado na análise destaca a quantidade de alunos por instituição de ensino nos anos de 2020 e 2021. Nele, é possível observar claramente a predominância dos estudantes vindos de escolas públicas no total atendido pela ONG. Por motivos de indisponibilidade de informações, o ano de 2022 não foi incluído na análise.
        \n\nAlém disso, a visualização dos dados é dinâmica, permitindo ajustes para a análise de cada ano separadamente, caso seja do interesse aprofundar o estudo de um período específico.
        \n\nComo destacado no gráfico apresentado, a maioria significativa dos estudantes atendidos pela ONG provém de escolas públicas. Este fato sublinha o impacto que a Passos Mágicos tem na vida desses jovens, os quais frequentemente enfrentam barreiras no acesso à educação de qualidade, como a falta de recursos e incentivo por parte do sistema público de ensino. A atuação da ONG oferece suporte fundamental a esses alunos, ampliando suas oportunidades educacionais e pessoais.
        """)
    
with st.container():

        df_2020, df_2021, df_2022 = carregar_dados()

        def criar_df_magico(df_2020, df_2021, df_2022):
            df_2020['Ano'] = '2020'
            df_2021['Ano'] = '2021'
            df_2022['Ano'] = '2022'
            
            df_magico = pd.concat([df_2020, df_2021, df_2022], ignore_index=True)
            df_magico_total = df_magico.groupby('INSTITUICAO_ENSINO_ALUNO').agg({'Ano': 'count'}).reset_index()
            df_magico_total.columns = ['Instituição de Ensino', 'Total de Alunos']
            df_magico_total = df_magico_total.sort_values(by='Total de Alunos', ascending=False)
            
            return df_magico, df_magico_total

        df_magico, df_magico_total = criar_df_magico(df_2020, df_2021, df_2022)

        def plot_alunos_por_instituicao(df, ano):
            alunos_por_instituicao = df['INSTITUICAO_ENSINO_ALUNO'].value_counts().reset_index()
            alunos_por_instituicao.columns = ['Instituição de Ensino', 'Quantidade de Alunos']
            
            fig = px.bar(
                alunos_por_instituicao,
                x='Instituição de Ensino',
                y='Quantidade de Alunos',
                title=f'Quantidade de Alunos por Instituição de Ensino ({ano})',
                labels={'Instituição de Ensino': 'Instituição de Ensino', 'Quantidade de Alunos': 'Quantidade de Alunos'},
                color_discrete_sequence=['#626EF5']
            )
            
            fig.update_layout(
                xaxis_title='Instituição de Ensino',
                yaxis_title='Quantidade de Alunos',
            )
            
            return fig

        def plot_total_alunos(df_total):
            fig = px.bar(
                df_total,
                x='Instituição de Ensino',
                y='Total de Alunos',
                title='Quantidade Total de Alunos por Instituição de Ensino (2020-2022)',
                labels={'Instituição de Ensino': 'Instituição de Ensino', 'Total de Alunos': 'Total de Alunos'},
                color_discrete_sequence=['#626EF5']
            )
            
            # Ajustar a aparência do layout do gráfico
            fig.update_layout(
                xaxis_title='Instituição de Ensino',
                yaxis_title='Total de Alunos',
            )
            
            return fig

        ano = st.selectbox('Escolha o ano:', ['Total', '2020', '2021', '2022'])

        if ano == 'Total':
            fig_total = plot_total_alunos(df_magico_total)
            st.plotly_chart(fig_total, use_container_width=True)
        elif ano == '2022':
            st.warning('Aviso: Não há dados disponíveis para o ano de 2022.', icon="⚠️")
        else:
            if ano == '2020':
                df_atual = df_2020
            elif ano == '2021':
                df_atual = df_2021
            
            fig = plot_alunos_por_instituicao(df_atual, ano)

            st.plotly_chart(fig, use_container_width=True)
