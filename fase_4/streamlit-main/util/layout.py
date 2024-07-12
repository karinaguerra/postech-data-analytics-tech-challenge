import streamlit as st
from st_pages import show_pages, Page
import locale

from util.constantes import TITULO_INTRODUCAO, TITULO_EDA, TITULO_MODELO, TITULO_PREV, TITULO_CONCLUSAO, TITULO_BIBLI

def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

def output_layout():
    show_pages(
        [
            Page("/main.py", TITULO_INTRODUCAO, use_relative_hash=True),
            Page("/pages/intro.py", TITULO_EDA, use_relative_hash=True),
            Page("/pages/modelo.py", TITULO_MODELO, use_relative_hash=True),
            Page("/pages/prev.py", TITULO_PREV, use_relative_hash=True,),
            Page("/pages/conclusao.py", TITULO_CONCLUSAO, use_relative_hash=True),
            Page("/pages/teste.py", 'Teste', use_relative_hash=True),
            Page("/pages/bibliografia.py",TITULO_BIBLI,use_relative_hash=True,),
        ]

    )
    # Autor 
    with st.sidebar:
        st.caption("<small>:orange[Criado por:]</small>", unsafe_allow_html=True)
        st.write("Karina Guerra do Nacimento")
        st.write("RM 352525")

        st.divider()

        st.subheader("Instalando as dependências do app")
        st.code(body="python -m venv venv", language="shell")
        st.code(body="source venv/Scripts/activate", language="shell")
        st.code(body="pip install -r requirements.txt", language="shell")

        st.divider()

        st.subheader("Executando localmente")
        st.code(body="streamlit run main.py", language="shell")

        st.divider()

        st.subheader("Repositórios do projeto")
        st.link_button(
            "Repositório Streamlit",
            "https://github.com/dhachcar/postech-tech-challenge-4-streamlit",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
        st.link_button(
            "Repositório Jupyter Notebook",
            "https://github.com/dhachcar/postech-tech-challenge-4",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
