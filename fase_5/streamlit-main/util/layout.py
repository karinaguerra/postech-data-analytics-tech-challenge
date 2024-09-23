import streamlit as st

def output_layout():
    # Autor 
    with st.sidebar:
        st.caption("<small>Criado por:</small>", unsafe_allow_html=True)
        st.write("Karina Guerra do Nacimento")
        st.write("RM 352525")
        st.write("---")

        st.caption("<small>[Links:]</small>", unsafe_allow_html=True)
        st.link_button(
            "Repositório",
            "https://github.com/karinaguerra/postech-data-analytics-tech-challenge/blob/main/fase_5/README.md",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )

        st.link_button(
            "Dashboard BI","https://app.powerbi.com/groups/me/reports/7ae6e389-4714-45d8-93ea-79d556d99846/23e0b55ce0b6574fa5e6?experience=power-bi",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
