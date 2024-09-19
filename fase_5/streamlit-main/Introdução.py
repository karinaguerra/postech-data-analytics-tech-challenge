import streamlit as st
from util.layout import output_layout
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Introdução")

output_layout()

st.subheader(f"FIAP - TechChallenge 5 - Proposta Analítica")

# Cria as abas
tab0, tab1, tab2 = st.tabs(["Introdução", "Objetivo", "Metas específicas"])

# Conteúdo da aba "Introdução"
with tab0:
    st.title('Introdução')
    st.write(
        f"""
        Este trabalho apresenta uma análise detalhada dos dados educacionais e de desenvolvimento dos alunos atendidos pela Associação Passos Mágicos, uma organização sem fins lucrativos que, há mais de 30 anos, se dedica a transformar a vida de crianças e jovens de baixa renda em Embu-Guaçu. Desde sua fundação, em 1992, a instituição tem como missão oferecer suporte educacional e psicopedagógico para crianças em situação de vulnerabilidade social, contribuindo significativamente para a redução das desigualdades na região.\n\n

        O estudo foca na análise exploratória dos dados de alunos entre 2020 e 2022, com o objetivo de identificar tendências, padrões e possíveis intervenções educacionais necessárias. Através da avaliação de indicadores-chave, como o Índice de Desenvolvimento Educacional (INDE) e a distribuição etária dos alunos, a análise busca fornecer uma visão abrangente do desempenho e progresso educacional dos atendidos. Além disso, serão analisados aspectos como as instituições de ensino frequentadas, o impacto das fases de aprendizado, e o desempenho acadêmico medido por faixas de avaliação representadas por pedras preciosas.\n\n

        Essa análise visa, portanto, entender melhor o papel transformador da Passos Mágicos na vida de seus alunos, destacando os desafios enfrentados, os avanços obtidos e as áreas que requerem maior atenção para potencializar o desenvolvimento educacional e social dessas crianças e adolescentes.


        """
    )


    
# Conteúdo da aba "Objetivo"
with tab1:
    st.title('Objetivo')
    st.write(
        f""" 
        O objetivo deste trabalho é realizar uma análise abrangente dos dados educacionais dos alunos atendidos pela Associação Passos Mágicos, com foco em identificar tendências, padrões de desempenho e áreas de melhoria. Através da análise exploratória de dados referentes aos anos de 2020 a 2022, buscamos:\n\n

        - Avaliar a distribuição etária dos alunos e entender como essa variável pode influenciar o aprendizado.\n\n
        - Examinar a quantidade de alunos por instituição de ensino, destacando a predominância das escolas públicas e seu impacto na formação dos jovens.\n\n
        - Analisar os indicadores do Índice de Desenvolvimento Educacional (INDE) para mensurar o progresso acadêmico dos alunos em diferentes dimensões: acadêmica, psicossocial e psicopedagógica.\n\n
        - Identificar tendências no nível de aprendizado ao longo das fases educacionais, observando a evolução do desempenho em disciplinas como Português, Matemática e Inglês.\n\n
        - Propor intervenções e estratégias para melhorar o desempenho acadêmico, com base nas descobertas, visando potencializar as oportunidades educacionais e promover a equidade no acesso à educação de qualidade.\n\n
        
        Através dessa análise, espera-se contribuir para a compreensão do impacto da Passos Mágicos na vida dos alunos e para a formulação de ações que melhorem continuamente os resultados educacionais da instituição.

        """
    )

# Conteúdo da aba "Metas específicas"
with tab2:
    st.title('Metas específicas')
    st.write(
        f""" 
        1. **Proposta Escolhida:** Proposta Analítica\n\n
        Objetivo: Desenvolver uma narrativa baseada nos dados para destacar como o programa Passos Mágicos impacta o desempenho dos estudantes.\n\n
        - Desenvolver um storytelling com base nos dados que destaque os impactos da Passos Mágicos sobre a performance dos estudantes.\n\n
        - Criar um dashboard interativo que permita à ONG visualizar os principais indicadores de desempenho e o perfil dos estudantes.\n\n
        - Fornecer insights acionáveis que possam orientar a ONG na tomada de decisões estratégicas para o futuro.\n\n
        
        2. Proposta Preditiva:\n\n
        Objetivo: Desenvolver modelos preditivos para antecipar o comportamento dos estudantes e entender melhor os fatores que influenciam seu desenvolvimento.\n\n
        - Criar um modelo preditivo para antecipar o comportamento dos estudantes, identificando variáveis-chave que influenciam seu desenvolvimento.\n\n
        - Explorar técnicas de machine learning, deep learning ou processamento de linguagem natural para criar um algoritmo eficiente e aplicável ao contexto da ONG.\n\n
        - Propor uma solução criativa que possa ser integrada às estratégias da ONG para monitorar e apoiar o progresso dos jovens atendidos.\n\n
        """
    )
