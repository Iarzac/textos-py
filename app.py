import streamlit as st
from base_datos import inicializar_bd, agregar_texto_generado, obtener_historial_textos
from generador import generar_texto_aleatorio

def main():
    st.title("Generador de Texto Coherente con SQLite")
    st.sidebar.header("Opciones")
    
    inicializar_bd()
    
    palabras_input = st.text_area("Ingrese palabras base separadas por comas", value="tecnología, creatividad")
    num_oraciones = st.sidebar.slider("Número de oraciones por párrafo", min_value=1, max_value=10, value=5)
    fuente = st.sidebar.selectbox("Seleccione una fuente", ["Normal", "Negrita", "Cursiva", "Subrayado"])

    tipo_texto = st.sidebar.selectbox("Seleccione el tipo de texto", ["Poético", "Coloquial", "Formal", "Informal"])

    if st.button("Generar Texto Aleatorio"):
        palabras_base = [p.strip() for p in palabras_input.split(",") if p.strip()]
        texto_generado = generar_texto_aleatorio(num_oraciones, tipo_texto)
        
        if fuente == "Negrita":
            st.markdown(f"**{texto_generado}**")
        elif fuente == "Cursiva":
            st.markdown(f"*{texto_generado}*")
        elif fuente == "Subrayado":
            st.markdown(f"<u>{texto_generado}</u>", unsafe_allow_html=True)
        else:
            st.write(texto_generado)

        agregar_texto_generado(texto_generado)
        st.success("Texto generado y guardado exitosamente.")

    st.sidebar.subheader("Historial de Textos Generados")
    if st.sidebar.button("Ver Historial"):
        historial = obtener_historial_textos()
        if historial:
            st.sidebar.write("Historial de Textos:")
            for texto, timestamp in historial:
                st.sidebar.write(f"{timestamp}: {texto}")
        else:
            st.sidebar.write("No hay textos generados aún.")

if __name__ == "__main__":
    main()
