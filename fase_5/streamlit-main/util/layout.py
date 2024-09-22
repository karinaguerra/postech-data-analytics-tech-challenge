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
            "Dashboard BI","https://app.powerbi.com/groups/me/reports/3be903e3-23a4-4128-a36e-b4fc1ef6adf8?ctid=11dbbfe2-89b8-4549-be10-cec364e59551&pbi_source=linkShare",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
