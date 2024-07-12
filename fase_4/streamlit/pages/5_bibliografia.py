import streamlit as st
from st_pages import show_pages_from_config

show_pages_from_config("config/pages_sections.toml")
# Titulo Pagina 
# st.set_page_config(layout='centered', 
#                    page_title='Modelo')

# Autor 
with st.sidebar:
    st.caption("<small>:orange[Criado por:]</small>", unsafe_allow_html=True)
    st.write("Karina Guerra do Nacimento")
    st.write("RM 352525")

# Titulo e subtitulo
with st.container():
    st.title("Bibliografia")

    st.write(
        f"""
        IPEA (2024); Disponível em: http://www.ipeadata.gov.br/Default.aspx Acesso em 02 de junho de 2024.\n
        ECONOMIA (15 de setembro de 2023) **Lehman Brothers: história para uma geração que não viveu a crise de 2008**; Disponível em: https://abrir.link/EHmvS Acesso em 10 de junho de 2024. \n
        PRESSE, France (25 de setembro de 2013) **Conheça as sanções internacionais contra o Irã**; Disponível em: https://abrir.link/tgTcM Acesso em 10 de junho de 2024. \n
        OPAS (2024) **Histórico da pandemia de COVID-19**; Disponível em: https://abrir.link/GpecY Acesso em 14 de junho de 2024. \n
        Prophet (2024); Disponível em: https://facebook.github.io/prophet/docs/quick_start.html Acesso em 10 de junho de 2024. \n
        Tensorflow (2024); Disponível em: https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM Acesso em 11 de junho de 2024. \n
        infomoney (18 de maio de 2009) **A história da Black Monday, o maior tombo da história das bolsas**; Disponível em: https://abrir.link/QcOxI Acesso em 01 de julho de 2024. \n
        SILVA, Daniel Neves (2024) **Guerra do Golfo**; Brasil Escola. Disponível em: https://abrir.link/iXFGP Acesso em 20 de junho de 2024. \n
        Warren Magazine (31 de maio de 2021) **Crise do subprime: entenda como surgiu, por que aconteceu e quais lições deixou**;  Disponível em: https://warren.com.br/magazine/crise-do-subprime/ Acesso em 21 de junho de 2024. \n
        MURTAUGH,Dan e DOAN, Lynn (14 de abriu de 2015) **Boom de petróleo de xisto nos EUA se transforma em retração ante projeções de queda da produção**; UOL. Disponível em: https://abrir.link/eDqLc Acesso em 21 de junho de 2024. \n
        G1 (08 de maio de 2018) **Trump anuncia retirada dos EUA de acordo nuclear com o Irã**; Disponível em: https://abrir.link/GXxqS Acesso em 21 de junho de 2024. \n
        ROCHA, Guilhereme Lucio (22 de fevereiro de 2022) **Quando a guerra na Ucrânia começou? Relembre o dia da invasão russa**; Disponível em: https://abrir.link/PfqQC Acesso em 29 de junho de 2024. \n       
        """)