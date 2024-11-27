import streamlit as st
from base_datos import inicializar_bd, agregar_palabra  # Asegúrate de importar agregar_palabra
from generador import generar_texto_aleatorio

def main():
    st.title("Generador de Texto Coherente con SQLite")
    st.sidebar.header("Opciones")
    
    inicializar_bd()
    
    palabras_input = st.text_area("Ingrese palabras base separadas por comas", value="tecnología, creatividad")
    num_oraciones = st.sidebar.slider("Número de oraciones por párrafo", min_value=1, max_value=10, value=5)
    fuente = st.sidebar.selectbox("Seleccione una fuente", ["Normal", "Negrita", "Cursiva", "Subrayado"])

    # Selector para el tipo de texto
    tipo_texto = st.sidebar.selectbox("Seleccione el tipo de texto", ["Poético", "Coloquial", "Formal", "Informal"])

    if st.button("Generar Texto Aleatorio"):
        palabras_base = [p.strip() for p in palabras_input.split(",") if p.strip()]
        
        # Agregar las palabras base a la base de datos en la categoría adecuada
        for palabra in palabras_base:
            agregar_palabra('sujeto', palabra)  # Usar 'sujeto' o la categoría que prefieras

        texto_generado = generar_texto_aleatorio(num_oraciones, tipo_texto)
        
        if fuente == "Negrita":
            st.markdown(f"**{texto_generado}**")
        elif fuente == "Cursiva":
            st.markdown(f"*{texto_generado}*")
        elif fuente == "Subrayado":
            st.markdown(f"<u>{texto_generado}</u>", unsafe_allow_html=True)
        else:
            st.write(texto_generado)

if __name__ == "__main__":
    main()
