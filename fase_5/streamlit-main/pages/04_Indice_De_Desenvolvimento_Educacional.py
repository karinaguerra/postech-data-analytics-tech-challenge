import streamlit as st
import pandas as pd
import plotly.express as px
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

df_2020, df_2021, df_2022 = carregar_dados()

with st.container():
    st.title("Análise dos Indicadores do Índice de Desenvolvimento Educacional (INDE) no Passos Mágicos")

st.write("""
         Ao analisar a base de dados do Passos Mágicos, identificamos alguns indicadores anuais utilizados pela ONG para calcular o índice INDE, que é central para sua avaliação geral.
        \n\nO INDE (Índice de Desenvolvimento Educacional) é uma métrica que avalia o progresso geral do aluno. Ele é composto por 7 indicadores individuais: IAN, IDA, IEG, IAA, IPS, IPP e IPV. A pontuação do INDE é calculada para cada fase, com os indicadores distribuídos em três principais dimensões:
        \n\n - **Dimensão Acadêmica (IAN, IDA, IEG):** Avalia o desempenho acadêmico dos alunos, como a aquisição de conhecimentos e habilidades.
        \n\n - **Dimensão Psicossocial (IAA, IPS):** Mede aspectos relacionados ao desenvolvimento emocional e social dos alunos, como autoestima e interação social.
        \n\n - **Dimensão Psicopedagógica (IPP, IPV):** Foca no acompanhamento pedagógico e nas habilidades cognitivas desenvolvidas pelos alunos.
        \n\nEssas dimensões oferecem uma visão abrangente do desempenho e desenvolvimento dos alunos atendidos pela ONG.
         
        \n\nO gráfico abaixo apresenta a média de indicados por ano
         """)

with st.container():
    def plot_media_indicadores_todos_anos(df_2020, df_2021, df_2022):
        indicadores = ['IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']
        
        media_2020 = df_2020[indicadores].mean()
        media_2021 = df_2021[indicadores].mean()
        media_2022 = df_2022[indicadores].mean()
        data = {
            'Indicador': indicadores * 3,
            'Média': list(media_2020) + list(media_2021) + list(media_2022),
            'Ano': ['2020'] * len(indicadores) + ['2021'] * len(indicadores) + ['2022'] * len(indicadores)
        }
        df_media = pd.DataFrame(data)
        fig = px.bar(
            df_media,
            x='Indicador',
            y='Média',
            color='Ano',
            title='Média dos Indicadores por Ano',
            labels={'Indicador': 'Indicador', 'Média': 'Média', 'Ano': 'Ano'},
            barmode='group',
            color_discrete_sequence=['#626EF5','#629BF0','#8462F0'] 
        )
        fig.update_layout(
            xaxis_title='Indicador',
            yaxis_title='Média',
        
        )
        st.plotly_chart(fig, use_container_width=True)
    plot_media_indicadores_todos_anos(df_2020, df_2021, df_2022)

   

with st.container():
    st.write("""
        O gráfico de histograma do INDE exibe a distribuição da pontuação do Índice de Desenvolvimento Educacional ao longo de três anos: 2020, 2021 e 2022. A análise revela alguns pontos importantes
        \n\nA maior parte das pontuações do INDE está concentrada entre 6 e 8, com picos no valor 7. Isso indica que a maioria dos alunos apresentou um desenvolvimento educacional médio-alto durante esse período.
        \n\nO gráfico sugere que, ao longo dos três anos, houve um leve aumento no número de alunos com pontuações mais altas (próximas a 8). Isso pode refletir uma melhoria no desenvolvimento educacional dos alunos entre 2020 e 2022.
         """)


    def plot_histograma_inde(df_2020, df_2021, df_2022):
        inde_2020 = df_2020['INDE']
        inde_2021 = df_2021['INDE']
        inde_2022 = df_2022['INDE']
        data = {
            'INDE': list(inde_2020) + list(inde_2021) + list(inde_2022),
            'Ano': ['2020'] * len(inde_2020) + ['2021'] * len(inde_2021) + ['2022'] * len(inde_2022)
        }
        df_inde = pd.DataFrame(data)
        ano_selecionado = st.selectbox('Escolha o ano:', ['Total', '2020', '2021', '2022'], key='selectbox_inde_histograma')
        if ano_selecionado != 'Total':
            df_inde_filtrado = df_inde[df_inde['Ano'] == ano_selecionado]
        else:
            df_inde_filtrado = df_inde
        fig = px.histogram(
            df_inde_filtrado,
            x='INDE',
            color='Ano' if ano_selecionado == 'Total' else None,
            title=f'Histograma do Indicador INDE - {ano_selecionado}',
            labels={'INDE': 'Valor do INDE', 'Ano': 'Ano'},
            nbins=20,  # Número de bins (intervalos) no histograma
            color_discrete_sequence=['#626EF5', '#629BF0', '#8462F0']
        )
        fig.update_layout(
            xaxis_title='Valor do INDE',
            yaxis_title='Contagem',
            bargap=0.2  # Espaçamento entre as barras
        )
        st.plotly_chart(fig, use_container_width=True)
    plot_histograma_inde(df_2020, df_2021, df_2022)
    
    st.write("""O grafico abaixo fornece uma visão da distribuição geral do INDE entre os alunos. A concentração de valores em torno da mediana sugere que a maioria dos alunos apresenta um desenvolvimento educacional consistente, com uma pontuação de 7,28. No entanto, os outliers identificados indicam que uma pequena parte dos alunos pode estar enfrentando maiores dificuldades em seu progresso, o que exige uma atenção mais específica.""")

    def plot_inde_indicadores(df_2020, df_2021, df_2022):
        df_2020['Ano'] = '2020'
        df_2021['Ano'] = '2021'
        df_2022['Ano'] = '2022'
        df_todos = pd.concat([df_2020, df_2021, df_2022])
        ano_selecionado = st.selectbox('Selecione o ano:', ['Total', '2020', '2021', '2022'], key='selectbox_inde_boxplot')
        if ano_selecionado != 'Total':
            df_filtrado = df_todos[df_todos['Ano'] == ano_selecionado]
        else:
            df_filtrado = df_todos
        fig = px.box(
            df_filtrado,
            y='INDE',
            title=f'Distribuição dos Indicadores ({ano_selecionado})',
            labels={'value': 'Valor do Indicador', 'variable': 'Indicador Técnico'},
            color_discrete_sequence=['#626EF5']
        )
        st.plotly_chart(fig, use_container_width=True)
    plot_inde_indicadores(df_2020, df_2021, df_2022)

    st.write("""
        A análise das correlações mostra que os indicadores da Dimensão Acadêmica (IEG e IDA) têm a maior influência no INDE, o que reflete o peso que o desempenho acadêmico tem no progresso dos alunos. Em contrapartida, os indicadores relacionados ao desenvolvimento psicossocial e psicopedagógico têm menor impacto no INDE, embora ainda sejam importantes para a formação integral dos alunos.        
     """)        

    def plot_correlation_heatmap(df):
            correlation_data = df[['INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']]
            correlation_matrix = correlation_data.corr()
            fig = px.imshow(correlation_matrix, 
                            text_auto=True, 
                            aspect="auto", 
                            color_continuous_scale='Purples', 
                            title='Matriz de Correlação entre as Pontuações')

            fig.update_layout(
                width=800, 
                height=500,
            )
            st.plotly_chart(fig, use_container_width=True)

    plot_correlation_heatmap(df_magico)    


    st.write("""
        Isso sugere que, para melhorar o INDE, um foco maior deve ser dado ao desenvolvimento acadêmico, sem negligenciar os outros aspectos que contribuem para o bem-estar e desenvolvimento completo dos estudantes.
     """)   
