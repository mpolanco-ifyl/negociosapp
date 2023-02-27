import streamlit as st
import openai
import pandas as pd

# Pide la clave de API de OpenAI al usuario
openai.api_key = st.text_input("Introduce tu clave de API de OpenAI:")

# Define una función para generar la idea de startup
def generar_idea(deseo):
    prompt = f"Quisiera que hubiera {deseo}"
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    idea = respuesta.choices[0].text.strip()
    return idea

# Define la aplicación Streamlit
def app():
    st.title("Generador de Ideas de Startups Digitales")

    # Pide la entrada del usuario
    deseo_usuario = st.text_input("¿Qué es lo que deseas?")

    if st.button("Generar Idea"):
        # Genera la idea de startup utilizando GPT
        idea_startup = generar_idea(deseo_usuario)

        # Formatea la idea de startup como un dataframe
        idea_df = pd.DataFrame({
            "Nombre de la Idea": [idea_startup],
            "Descripción Corta": ["Una startup digital que resuelve los puntos débiles del usuario."],
            "Persona Objetivo": ["[inserta la persona objetivo]"],
            "Puntos Débiles del Usuario": ["[inserta los puntos débiles del usuario a resolver]"],
            "Propuestas de Valor Principales": ["[inserta las propuestas de valor principales]"],
            "Canales de Ventas y Marketing": ["[inserta los canales de ventas y marketing]"],
            "Fuentes de Ingresos": ["[inserta las fuentes de ingresos]"],
            "Estructuras de Costos": ["[inserta las estructuras de costos]"],
            "Actividades Clave": ["[inserta las actividades clave]"],
            "Recursos Clave": ["[inserta los recursos clave]"],
            "Socios Clave": ["[inserta los socios clave]"],
            "Pasos de Validación de la Idea": ["[inserta los pasos de validación de la idea]"],
            "Costo Estimado del Primer Año de Operación": ["[inserta el costo estimado del primer año de operación]"],
            "Desafíos Potenciales del Negocio": ["[inserta los desafíos potenciales del negocio a tener en cuenta]"]
        })

        # Muestra la idea de startup como una tabla en markdown
        st.write(idea_df.to_markdown(index=False), unsafe_allow_html=True)

# Ejecuta la aplicación Streamlit
if __name__ == '__main__':
    app()
