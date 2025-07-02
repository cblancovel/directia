import streamlit as st

def mostrar_estado_general():
    st.header("🟢 Estado General del Hospital")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Ingresos Totales", "74", "+5 vs ayer")
    col2.metric("Altas Totales", "66", "-3 vs ayer")
    col3.metric("Balance", "-8", "-10%")
    col4.metric("Ocupación General", "92%", "+2%")

    st.markdown("---")

    st.info("""
    **Estado General** muestra los datos más relevantes del cuadro de mando
    diario. En versiones futuras se integrará visualización con gráficas
    para una comprensión más intuitiva.
    """)
