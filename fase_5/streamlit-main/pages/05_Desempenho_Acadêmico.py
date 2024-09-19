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

# Defina os caminhos corretos dos arquivos CSV
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
    st.title("Desempenho Acadêmico")
    st.header("Classificação de Desempenho Acadêmico com Pedras Preciosas: O Índice INDE e Suas Faixas de Avaliação")
    st.write("""
         O indicador INDE associa o desempenho do aluno a pedras preciosas, tornando a avaliação mais significativa e motivadora. Cada pedra representa uma faixa específica de desempenho, conferindo um elemento de valor e prestígio ao progresso acadêmico. Para determinar a pedra correspondente ao desempenho do aluno:
             
        \n\n - Se o INDE está entre 2,405 e 5,506, a pedra é Quartzo.
        \n\n - Se o INDE está entre 5,506 e 6,868, a pedra é Ágata.
        \n\n - Se o INDE está entre 6,868 e 8,230, a pedra é Ametista.
        \n\n - Se o INDE está acima de 8,230, a pedra é Topázio.
    
        """)
             
with st.container():
    def plot_alunos_por_pedra_por_ano(df_2020, df_2021, df_2022):
        df_grouped_2020 = df_2020.groupby(['PEDRA']).size().reset_index(name='Alunos').sort_values(by='Alunos', ascending=False)
        df_grouped_2021 = df_2021.groupby(['PEDRA']).size().reset_index(name='Alunos').sort_values(by='Alunos', ascending=False)
        df_grouped_2022 = df_2022.groupby(['PEDRA']).size().reset_index(name='Alunos').sort_values(by='Alunos', ascending=False)
        
        ano_selecionado = st.selectbox('Escolha o ano:', ['2020', '2021', '2022'], key='selectbox_ano')

        if ano_selecionado == '2020':
            df_selecionado = df_grouped_2020
        elif ano_selecionado == '2021':
            df_selecionado = df_grouped_2021
        else:
            df_selecionado = df_grouped_2022

        fig = px.bar(
            df_selecionado,
            x='PEDRA',
            y='Alunos',
            title=f'Número de Alunos por Tipo de Pedra ({ano_selecionado})',
            labels={'PEDRA': 'Tipo de Pedra', 'Alunos': 'Número de Alunos'},
            color_discrete_sequence=['#626EF5']
        )

        fig.update_layout(
            xaxis_title='Tipo de Pedra',
            yaxis_title='Número de Alunos'
        )

        st.plotly_chart(fig, use_container_width=True)

    plot_alunos_por_pedra_por_ano(df_2020, df_2021, df_2022)

with st.container():
    st.write("""
        \n\nSignificado de cada pedra:
        \n\n1. Quartzo: O quartzo, uma pedra comum e essencial, simboliza os primeiros passos no aprendizado, onde a base de conhecimento está sendo firmemente estabelecida.
        \n\n2. Ágata: A ágata, com suas belas bandas e variedades de cores, representa o crescimento e a diversificação do conhecimento e habilidades.
        \n\n3. Ametista: A ametista, com sua cor vibrante e propriedades únicas, reflete a criatividade e a profundidade do entendimento alcançado pelo aluno.
        \n\n4. Topázio: O topázio representa a excelência acadêmica. Conhecida por sua clareza e brilho, esta pedra preciosa reflete o esforço e a dedicação excepcionais do aluno.
        
        \n\nEm 2020, um grande número de alunos atingiu a pedra de Ametista, demonstrando um alto desempenho acadêmico com médias de INDE entre 7 e 8. Apenas alguns alcançaram a pedra de Topázio (acima de 8,2), uma distinção reservada para aqueles que superaram todas as expectativas. Mesmo sendo o ano que mais sofreu com o impacto da pandemia de COVID-19, os alunos mantiveram um bom desempenho.
        \n\nEm 2021, houve uma diminuição no número de alunos avaliados. Proporcionalmente, observou-se uma redução nas conquistas da pedra de Quartzo e um leve aumento na de Topázio, sugerindo que alguns alunos que estavam no nível de Ametista progrediram para o nível máximo, enquanto menos estudantes permaneceram no nível inicial.
        \n\nJá em 2022, o número total de alunos aumentou, assim como as conquistas na maioria das categorias, com exceção da pedra de Ametista, que permaneceu estável. Houve um crescimento significativo na atribuição da pedra de Ágata, o que sugere que, com a volta à normalidade das atividades escolares, muitos alunos apresentaram um desempenho um pouco inferior ao dos anos anteriores, com médias de INDE entre 5,5 e 6,8, mas ainda mostrando progresso.
        """)

    def plot_numero_alunos_por_fase_e_pedra(df_concat):
        df_grouped = df_concat.groupby(['FASE', 'PEDRA']).size().reset_index(name='Alunos')
        
        pedras = df_grouped['PEDRA'].unique()
        
        pedras_selecionadas = st.multiselect(
            'Selecione as Pedras para Exibir:',
            options=pedras,
            default=pedras  # Por padrão, exibe todas as pedras
        )
        
        df_filtered = df_grouped[df_grouped['PEDRA'].isin(pedras_selecionadas)]
        

        fig = px.bar(
            df_filtered,
            x='FASE',
            y='Alunos',
            color='PEDRA',
            title='Tipo de Pedra por fase',
            labels={'FASE': 'Fase', 'Alunos': 'Número de Alunos', 'PEDRA': 'Tipo de Pedra'},
            color_discrete_sequence=['#629BF0', '#8462F0', '#626EF0', '#62C7F0'],  # Definindo cores específicas
            text='Alunos'
        )
        
        fig.update_layout(
            xaxis_title='Fase',
            yaxis_title='Número de Pedras',
            barmode='group',  # Barra agrupada
        )
        
        fig.update_traces(texttemplate='%{text}', textposition='outside')
        
        st.plotly_chart(fig, use_container_width=True)

    plot_numero_alunos_por_fase_e_pedra(df_magico)

    st.write("""
            O gráfico apresenta o número de pedras associadas ao desempenho dos alunos em diferentes fases de avaliação.
             
            \n\n - **Fase 0:** O maior número de alunos recebeu a pedra Ametista (194), o que indica um bom desempenho (INDE entre 6,868 e 8,230), enquanto alguns poucos (19) conseguiram o nível de Topázio (INDE acima de 8,230). Há uma quantidade considerável de alunos com Quartzo (91) e Ágata (88), sugerindo que uma parcela significativa ainda está nos estágios iniciais de desenvolvimento.

            \n\n - **Fase 1:** Nota-se uma queda no número de pedras, com um número menor de Ametista (114) e Topázio (18), o que pode indicar uma redução no desempenho. No entanto, a presença de muitos alunos com Quartzo (77) e Ágata (65) ainda demonstra progresso em fases intermediárias.

            \n\n - **Fase 2 a 4:** O número de Ametistas (147 e 70, respectivamente) continua dominante, mostrando que muitos alunos mantêm um nível elevado de desempenho. Há um leve aumento em Ágata na fase 2 (89), sugerindo uma evolução de alunos que estavam no nível de Quartzo.

            \n\n - **Fases 6 e 8:** Nestas fases finais, o número de pedras de Topázio e Ametista diminui, indicando que apenas uma pequena quantidade de alunos atingiu ou manteve a excelência acadêmica ao longo do tempo.
            
            \n\nO gráfico sugere uma forte presença de alunos no nível de Ametista nas primeiras fases, o que pode indicar que, mesmo com as dificuldades iniciais (como a pandemia), muitos alunos mantiveram um desempenho sólido (7 a 8 de INDE). No entanto, em fases posteriores, o número de Ágatas e Quartzos cresce, sugerindo que alguns alunos enfrentaram dificuldades para sustentar esse alto desempenho.

            \n\nO progresso acadêmico representado pelas pedras mostra uma curva de desempenho, onde a maioria começa com um desempenho mediano e evolui, com alguns poucos atingindo a excelência (Topázio).
             
            """)
