import streamlit as st

def mostrar_alertas():
    st.header("🔴 Alertas / Riesgos")

    ocupacion_uci = 95
    balance = -8

    if ocupacion_uci > 95:
        st.error("🚨 Ocupación UCI crítica: 95%")
    else:
        st.success("✅ Ocupación UCI estable.")

    if balance < -10:
        st.error(f"🚨 Balance crítico: {balance} camas negativas.")
    else:
        st.success(f"✅ Balance estable: {balance} camas negativas.")

    st.info("""
    Este módulo alerta al Director Médico de riesgos inmediatos.
    En versiones futuras podrá incorporar IA para predicción de saturaciones.
    """)
