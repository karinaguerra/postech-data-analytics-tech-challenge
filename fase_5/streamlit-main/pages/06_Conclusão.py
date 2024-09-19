import streamlit as st
from util.layout import output_layout

st.set_page_config(
    page_title=f"Conclusão", layout="wide"
)

output_layout()
# Titulo
with st.container():
    st.header(f"Conclusão")

    st.write(
    f"""

    A análise dos alunos da ONG Passos Mágicos, ao longo de três anos (2020, 2021 e 2022), fornece insights valiosos sobre o perfil e o progresso dos estudantes. A segmentação por ano permitiu uma visão clara da evolução do número de alunos, com um total geral de 1.348, destacando um aumento significativo em 2022. A distribuição etária dos alunos, centrada principalmente entre 10 e 14 anos, evidenciou uma predominância de jovens nessa faixa, confirmada pelos box plots e histogramas.

    A análise das instituições de ensino revelou que a maioria dos alunos atendidos pela ONG é oriunda de escolas públicas, o que reforça o papel essencial da ONG no apoio a esses estudantes, que enfrentam desafios educacionais e socioeconômicos. Através do cálculo do INDE (Índice de Desenvolvimento Educacional), foi possível medir o desempenho acadêmico, psicossocial e psicopedagógico dos alunos. A maior parte das pontuações do INDE concentrou-se entre 6 e 8, sugerindo um desenvolvimento educacional consistente, com um leve aumento em pontuações mais altas ao longo dos anos.\n\n

    A análise por fase de aprendizado indicou que as fases iniciais (0 e 1) apresentam o maior número de alunos, mas há uma diminuição nas fases mais avançadas, sugerindo possíveis dificuldades acadêmicas ou outros fatores que contribuem para o abandono ou progressão lenta. Estratégias de intervenção, como suporte adicional, podem ser necessárias para garantir que mais alunos avancem com sucesso nas fases mais desafiadoras.\n\n

    Por fim, o sistema de avaliação com pedras preciosas associado ao INDE destacou o progresso dos alunos de maneira motivadora. Em 2020, houve uma alta incidência de alunos na faixa de Ametista, refletindo bom desempenho, apesar dos desafios da pandemia. Já em 2021, houve uma leve queda no número total de alunos, mas um aumento nas conquistas de Topázio, indicando progressão de alguns alunos para níveis mais altos. Em 2022, o aumento do número total de alunos trouxe variações nas categorias de desempenho, sugerindo uma recuperação parcial das dificuldades enfrentadas nos anos anteriores.\n\n

    Essa análise evidencia a importância do acompanhamento contínuo do desenvolvimento acadêmico e pessoal dos alunos, além de ressaltar o impacto positivo da ONG Passos Mágicos em suas trajetórias educacionais.

    """)