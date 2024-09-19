import streamlit as st
from util.layout import output_layout

st.set_page_config(
    page_title=f"Bibliografia"
)

output_layout()

with st.container():
    st.header(f"Bibliografia")

    st.write(
        f"""
        PASSOS MAGICOS (2024); Disponível em: https://passosmagicos.org.br/ Acesso em 02 de agosto de 2024.\n
        CRESCER SEMPRE (01 de Dezembro de 2021) **ONG de Educação: entenda a importância para a sociedade**; Disponível em: https://encurtador.com.br/lEiyu Acesso em 10 de agosto de 2024. \n
        FGV EAESP (24 de abril de 2024) **Passos Mágicos: FGVnianos se unem a projeto transformador em Embu-Guaçu**; Disponível em: https://encurtador.com.br/dysMq Acesso em 10 de setembro de 2024. \n
        SILVA, Dario Rodrigues da. **Pesquisa do Desenvolvimento Educacional - PEDE 2020. Associação Passos Mágicos.** São Paulo, 2021.\n
        SILVA, Dario Rodrigues da. **Pesquisa do Desenvolvimento Educacional - PEDE 2021. Associação Passos Mágicos.** São Paulo, 2022.\n
        SILVA, Dario Rodrigues da. **Pesquisa do Desenvolvimento Educacional - PEDE 2022. Associação Passos Mágicos.** São Paulo, 2023.\n
        STREAMLIT DOCUMENTATION (2024); Disponível em: https://docs.streamlit.io/ Acesso em 18 de setembro de 2024.\n
        PLOTLY DOCUMENTATION (2024) **Plotly Open Source Graphing Library for Python**; Disponível em: https://plotly.com/python/ Acesso em 18 de setembro de 2024.\n
        """)