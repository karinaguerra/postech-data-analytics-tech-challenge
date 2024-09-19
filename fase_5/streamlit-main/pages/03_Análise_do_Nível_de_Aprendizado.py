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
caminho_csv_2020 = 'data/df_2020_limpo.csv'
caminho_csv_2021 = 'data/df_2021_limpo.csv'
caminho_csv_2022 = 'data/df_2022_limpo.csv'

# Função para carregar os dados
def carregar_dados():
    df_2020 = pd.read_csv(caminho_csv_2020)
    df_2021 = pd.read_csv(caminho_csv_2021)
    df_2022 = pd.read_csv(caminho_csv_2022)
    return df_2020, df_2021, df_2022

df_2020, df_2021, df_2022 = carregar_dados()
# Titulo e subtitulo
with st.container():
    st.title("Análise do Nível de Aprendizado dos Alunos por Fase")

    st.write("""
        O gráfico a seguir fornece uma visão detalhada do número de alunos distribuídos por fase de aprendizado ao longo dos anos disponíveis. Esta análise é essencial para compreender como os alunos estão se desenvolvendo em diferentes fases de seu percurso educacional.        
        \n\nIsso possibilita a identificação de tendências e variações no número de alunos conforme eles avançam pelas diferentes fases. Além disso, a pontuação do INDE, indicador de desempenho acadêmico, é calculada para cada fase, refletindo o desempenho dos alunos em cada etapa.
    """)
               
with st.container():

    # Função para agrupar e contar alunos por fase e ano
    def agrupar_por_fase_e_ano(df):
        df_grouped = df.groupby(['ANO', 'FASE']).size().reset_index(name='Alunos')
        df_grouped['ANO'] = df_grouped['ANO'].astype(str)  # Garantir que 'ANO' seja tratado como string
        return df_grouped

    # Função para criar o gráfico
    def plot_alunos_por_fase(df_grouped, titulo):
        fig = px.bar(
            df_grouped,
            x='FASE',
            y='Alunos',
            color= 'ANO' if ano_selecionado == 'Total' else None,
            title=titulo,
            labels={'FASE': 'Fase', 'Alunos': 'Número de Alunos'},
            barmode='group',
            color_discrete_sequence=['#626EF5','#629BF0','#8462F0']  # Paleta de cores azul
        )
    

        # Melhorando a apresentação do layout
        fig.update_layout(
            xaxis_title='Fase',
            yaxis_title='Número de Alunos',
            legend_title_text='Ano',
            bargap=0.2,  # Ajusta o espaço entre as barras
        )
        
        return fig

    # Agrupar os dados totais e por ano a partir do df_magico
    df_total = agrupar_por_fase_e_ano(df_magico)
    df_2020_grouped = df_total[df_total['ANO'] == '2020']
    df_2021_grouped = df_total[df_total['ANO'] == '2021']
    df_2022_grouped = df_total[df_total['ANO'] == '2022']

    # Seletor para escolher o ano, com chave (key) única
    ano_selecionado = st.selectbox('Escolha o ano:', ['Total', '2020', '2021', '2022'], key='ano_selecionado')

    # Exibir o gráfico ou aviso dependendo do ano selecionado
    if ano_selecionado == 'Total':
        fig_total = plot_alunos_por_fase(df_total, 'Número Total de Alunos por Fase (2020-2022)')
        st.plotly_chart(fig_total, use_container_width=True)
    elif ano_selecionado == '2020':
        fig_2020 = plot_alunos_por_fase(df_2020_grouped, 'Número de Alunos por Fase (2020)')
        st.plotly_chart(fig_2020, use_container_width=True)
    elif ano_selecionado == '2021':
        fig_2021 = plot_alunos_por_fase(df_2021_grouped, 'Número de Alunos por Fase (2021)')
        st.plotly_chart(fig_2021, use_container_width=True)
    elif ano_selecionado == '2022':
        if df_2022_grouped.empty:
            st.warning('Não há dados disponíveis para o ano de 2022.')
        else:
            fig_2022 = plot_alunos_por_fase(df_2022_grouped, 'Número de Alunos por Fase (2022)')
            st.plotly_chart(fig_2022, use_container_width=True)

    st.write("""
             
        **Analisando o gráfico de total de alunos por fase:**
        \n\n**Altas nas Fases Iniciais:** As fases 0 e 1 apresentam o maior número de alunos, o que sugere que essas são fases onde mais alunos ingressam no programa. É possível que muitos alunos não avancem para as fases posteriores, conforme evidenciado pela diminuição de alunos nas fases 4 a 8.
        \n\n**Variações entre Anos:** Apesar de pequenas diferenças, as tendências gerais permanecem consistentes entre os anos. Isso sugere que o padrão de progressão dos alunos tem sido semelhante ao longo dos três anos.
        \n\n**Alto abandono ou progressão lenta:** Como o número de alunos diminui nas fases mais avançadas (4 a 8), pode ser necessário investigar o que está ocorrendo. Fatores como dificuldades acadêmicas, mudanças no interesse dos alunos, ou questões estruturais no programa podem estar contribuindo para a queda de alunos nessas fases.
        \n\n**Planejamento e Intervenções:** Identificar as fases onde o número de alunos cai abruptamente pode ajudar na criação de estratégias de intervenção, como tutorias adicionais ou suporte acadêmico, para garantir que mais alunos progridam para as fases avançadas com sucesso.
        """)

    def plot_grades_plotly(df_concat):
        # Agrupar os dados por fase e calcular a média das notas
        df_grouped = df_concat.groupby('FASE')[['NOTA_PORT', 'NOTA_MAT', 'NOTA_ING']].mean().reset_index()
        
        # Criar o gráfico de linhas usando Plotly
        fig = px.line(df_grouped, 
                    x='FASE', 
                    y=['NOTA_PORT', 'NOTA_MAT', 'NOTA_ING'],
                    markers=True,
                    labels={'value': 'Média das Notas', 'FASE': 'Fase'},
                    title='Média das Notas por Fase')


        fig.for_each_trace(lambda t: t.update(name='Português' if t.name == 'NOTA_PORT' 
                                                else 'Matemática' if t.name == 'NOTA_MAT' 
                                                else 'Inglês'))
        
        # Configurar as cores das linhas
        colors = {
            'Português': '#626EF5',
            'Matemática': '#8562F5',
            'Inglês': '#629DF5'
        }
        
        fig.for_each_trace(lambda t: t.update(line=dict(color=colors[t.name], width=2)))
    
        # Atualizar a legenda e layout
        fig.update_layout(
            legend_title_text='Disciplinas',
        )
        
        st.plotly_chart(fig, use_container_width=True)

    plot_grades_plotly(df_magico)

    st.write("""
            O gráfico mostra a média das notas por fase para três disciplinas: Português, Matemática e Inglês. Analisando o desempenho dos alunos parece flutuar bastante entre as fases, especialmente nas fases 3 e 6, onde há picos ou quedas notáveis.
            \n\nAs disciplinas parecem ter uma queda de desempenho até a fase 3, mas depois mostram recuperação até a fase 6. A fase 6 destaca-se como um ponto de alto desempenho, enquanto as fases 7 e 8 mostram uma queda considerável em todas as disciplinas.       
               
             """)
    
    # Função para criar e exibir o gráfico
    def plot_individual_scores(df):
        df_grouped = df.groupby('FASE')['INDE'].mean().reset_index()
        
        # Criar o gráfico de linhas
        fig = go.Figure()
        
        # Adicionar linha
        fig.add_trace(go.Scatter(
            x=df_grouped['FASE'], 
            y=df_grouped['INDE'],
            mode='lines+markers',
            line=dict(color='#626EF5', width=2),
            marker=dict(size=8, color='#626EF5', line=dict(width=1, color='DarkSlateGrey')),
            name='Média da Pontuação INDE'
        ))
        
        # Adicionar anotações
        for index, row in df_grouped.iterrows():
            fig.add_annotation(
                x=row['FASE'], 
                y=row['INDE'], 
                text=str(round(row['INDE'], 1)),
                showarrow=True,
                arrowhead=2,
                ax=0,
                ay=-40
            )
        
        # Ajustar a aparência do gráfico
        fig.update_layout(
            title='Média da Pontuação INDE por Fase',
            xaxis_title='Fase',
            yaxis_title='Média da Pontuação INDE',
            template='plotly_white'
        )
        
        # Exibir o gráfico
        st.plotly_chart(fig, use_container_width=True)
    
    plot_individual_scores(df_magico)

    st.write("""
            Como o INDE está relacionado às fases, o gráfico acima apresenta a média da pontuação do INDE em cada fase. Ao analisar os dados, foi possível observar que:
            \n\n- **Fase 0:** Os alunos começam com uma pontuação média alta de 7.5, sugerindo um bom desempenho inicial.
            \n\n - **Fases 1 e 2:** Há uma queda nas pontuações médias, atingindo 6.9 na fase 2, o que pode indicar dificuldades iniciais enfrentadas pelos alunos nessas fases.
            \n\n - **Fase 4:** O desempenho se estabiliza em 7.0, sugerindo uma leve recuperação.
            \n\n - **Fase 6:** Uma nova queda é observada, com a pontuação caindo para 6.7, o que pode indicar uma fase mais desafiadora.
            \n\n - **Fases 7 e 8:** A partir da fase 6, há uma recuperação significativa, com a pontuação média subindo até 7.7 na fase 8, sugerindo que os alunos têm mais sucesso conforme avançam para as últimas fases.
             
            \n\n Este gráfico foi criado para destacar a variação da pontuação INDE ao longo das fases. O objetivo é analisar onde os alunos podem estar enfrentando dificuldades ou demonstrando maior sucesso em suas trajetórias acadêmicas. 
            \n\n A importância do INDE neste contexto é fornecer uma métrica objetiva de desempenho que possa guiar políticas acadêmicas ou ajustes no currículo para otimizar o sucesso dos alunos nas fases em que encontram mais desafios.
        """)
    

