import streamlit as st

def generar_informe():
    st.header("🟣 Informe Automático")

    texto = """
    Hoy el Hospital Clínico San Carlos presenta un balance negativo de -8 camas,
    con un total de 74 ingresos y 66 altas. La ocupación general se encuentra
    al 92%, manteniendo una presión asistencial moderada. Se recomienda vigilancia
    de las áreas de UCI y de Urgencias ante posibles incrementos.
    """

    st.text_area("Informe generado:", value=texto, height=250)
    st.success("Informe generado correctamente. Copia y pega en tu parte diaria.")
