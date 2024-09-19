import streamlit as st
from util.layout import output_layout


output_layout()
# Titulo
with st.container():
    st.header(f"Passos Mágicos")

    st.write(
    f"""

    A Associação Passos Mágicos é uma organização que, há mais de 30 anos, dedica-se a transformar a vida de crianças e jovens de baixa renda no município de Embu-Guaçu. Fundada em 1992 por Michelle Flues e Dimetri Ivanoff, a instituição começou como um projeto voluntário em orfanatos, oferecendo apoio educacional e psicológico a crianças em situação de vulnerabilidade. Ao longo dos anos, a Passos Mágicos cresceu e, em 2016, consolidou-se como uma associação oficial, com foco em educação e transformação social.

    \n\nA organização desenvolve programas que oferecem educação de qualidade com suporte psicopedagógico, além de projetos especiais como apadrinhamento e intercâmbios culturais. Através de eventos sociais e campanhas anuais de arrecadação, a associação também mobiliza a comunidade para apoiar a trajetória educacional das crianças e adolescentes atendidos. Com um compromisso firme com os Objetivos de Desenvolvimento Sustentável da ONU, a Passos Mágicos busca reduzir desigualdades e promover oportunidades iguais para todos.
    
     """)
    st.link_button("🧙🏻‍♂ ONG Passos Mágicos","https://passosmagicos.org.br/")