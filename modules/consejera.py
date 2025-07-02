import streamlit as st
import requests

# --- TU API KEY AQUÍ ---
MISTRAL_API_KEY = "6gAf9E84ob2HMGIHOBZ16Tv23LqOVFw9"   # ← Pega aquí tu key de Mistral

def chat_mistral(prompt):
    """
    Llama a Mistral API y devuelve texto generado.
    """

    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-medium",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Eres un Director Médico con gran experiencia en gestión hospitalaria. "
                    "Tu tarea es analizar la situación que se describe a continuación "
                    "y proponer EXACTAMENTE 3 acciones muy concretas y realistas que puedan "
                    "implementarse HOY MISMO en el hospital para mitigar posibles problemas "
                    "de saturación, falta de camas u otros riesgos. "
                    "No escribas más de 200 palabras. "
                    "Sé claro, ejecutivo y muy práctico. "
                    "Empieza cada recomendación con un número (1, 2, 3)."
                )

            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        res = requests.post(url, headers=headers, json=payload, timeout=30)
        res.raise_for_status()

        data = res.json()

        return data["choices"][0]["message"]["content"].strip()

    except requests.Timeout:
        return "⏱️ Timeout: Mistral ha tardado demasiado en responder."

    except requests.RequestException as e:
        return f"❌ Error llamando a Mistral: {str(e)}"

    except Exception as ex:
        return f"❌ Error procesando respuesta: {str(ex)}"


def consejera_ia():
    st.subheader("🤖 IA Consejera")

    st.write("Introduce datos actuales y deja que la IA genere recomendaciones.")

    ocupacion = st.slider("Ocupación General (%)", 50, 110, 85)
    balance = st.number_input("Balance de camas (altas - ingresos)", value=-8)
    ingresos_manana = st.number_input("Ingresos urgentes previstos mañana", value=40)

    if st.button("🤖 Generar Recomendación IA", use_container_width=True):
        prompt = (
            f"Con una ocupación general de {ocupacion}%, "
            f"un balance de camas de {balance}, "
            f"y {ingresos_manana} ingresos urgentes previstos para mañana, "
            f"¿qué recomendaciones estratégicas darías al Director Médico?"
        )
        st.info("Enviando prompt a Mistral...")

        respuesta = chat_mistral(prompt)

        st.success("✅ Recomendación generada:")
        st.write(respuesta)
