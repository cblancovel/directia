import streamlit as st

def mostrar_predicciones():
    st.header("🟠 Predicciones para mañana")

    col1, col2, col3 = st.columns(3)

    col1.metric("🔮 Ingresos previstos", "80", "+5 vs hoy")
    col2.metric("🔮 Ocupación UCI prevista", "95%", "+3%")
    col3.metric("🔮 Riesgo Saturación", "Moderado")

    st.markdown("---")

    st.info("""
    Este módulo mostrará predicciones basadas en modelos de IA (Gemma o similares).
    Permite anticipar escenarios críticos y tomar decisiones proactivas.
    """)
