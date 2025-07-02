import streamlit as st
from modules import estado_general, informe, predictor, alertas, consejera

st.set_page_config(page_title="DirectIA", layout="wide")

# --- CSS ---
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 24px !important;
    }
    .stRadio > div > label > div[data-testid="stMarkdownContainer"] p {
        font-size: 25px !important;
        font-weight: 600;
    }
    .stButton>button {
        font-size: 24px !important;
        padding: 0.75em 2em;
    }
    h1, h2, h3, h4 {
        font-size: 28px !important;
    }
    textarea, input, select {
        font-size: 22px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- TITULOS ---
st.markdown('<p class="big-font">🚑 DirectIA</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">Asistente para el Director Médico del Hospital Clínico San Carlos</p>', unsafe_allow_html=True)

st.markdown("---")

# --- MENÚ PRINCIPAL ---
opcion = st.radio(
    "Selecciona un módulo:",
    [
        "🏠 Inicio",
        "🟢 Estado General",
        "🟣 Informe Automático",
        "🟠 Predicciones",
        "🔴 Alertas / Riesgos",
        "🤖 IA Consejera"
    ],
    horizontal=True
)

st.markdown("---")

# --- NAVEGACIÓN ENTRE MÓDULOS ---
if opcion == "🏠 Inicio":
    st.success("Selecciona un módulo para comenzar.")

elif opcion == "🟢 Estado General":
    estado_general.mostrar_estado_general()

elif opcion == "🟣 Informe Automático":
    informe.generar_informe()

elif opcion == "🟠 Predicciones":
    predictor.mostrar_predicciones()

elif opcion == "🔴 Alertas / Riesgos":
    alertas.mostrar_alertas()

elif opcion == "🤖 IA Consejera":
    consejera.consejera_ia()

st.markdown("---")
st.caption("© 2025 DirectIA - Prototipo en desarrollo.")
