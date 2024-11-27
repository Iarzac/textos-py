import streamlit as st
from base_datos import inicializar_bd, agregar_palabra, eliminar_palabra
from generador import generar_texto_aleatorio

def main():
    st.title("Generador de Texto Coherente con SQLite")
    st.sidebar.header("Opciones")
    
    inicializar_bd()
    
    palabras_input = st.text_area("Ingrese palabras base separadas por comas", value="tecnología, creatividad")
    num_oraciones = st.sidebar.slider("Número de oraciones por párrafo", min_value=1, max_value=10, value=5)
    fuente = st.sidebar.selectbox("Seleccione una fuente", ["Normal", "Negrita", "Cursiva", "Subrayado"])
    
    if st.button("Generar Texto Aleatorio"):
        palabras_base = [p.strip() for p in palabras_input.split(",") if p.strip()]
        texto_generado = generar_texto_aleatorio(num_oraciones)
        
        if fuente == "Negrita":
            st.markdown(f"**{texto_generado}**")
        elif fuente == "Cursiva":
            st.markdown(f"*{texto_generado}*")
        elif fuente == "Subrayado":
            st.markdown(f"<u>{texto_generado}</u>", unsafe_allow_html=True)
        else:
            st.write(texto_generado)
    
    st.sidebar.subheader("Gestión de Palabras")
    
    with st.sidebar.expander("Agregar Palabra"):
        nueva_categoria = st.text_input("Categoría (sujeto, verbo, adjetivo, complemento, conector)")
        nueva_palabra = st.text_input("Nueva Palabra")
        if st.button("Agregar"):
            if nueva_categoria and nueva_palabra:
                if agregar_palabra(nueva_categoria, nueva_palabra):
                    st.sidebar.success(f"'{nueva_palabra}' agregado a '{nueva_categoria}'.")
                else:
                    st.sidebar.error(f"La palabra '{nueva_palabra}' ya existe.")
            else:
                st.sidebar.error("Complete todos los campos.")

    with st.sidebar.expander("Eliminar Palabra"):
        palabra_eliminar = st.text_input("Palabra a eliminar")
        if st.button("Eliminar"):
            if palabra_eliminar:
                eliminar_palabra(palabra_eliminar)
                st.sidebar.success(f"'{palabra_eliminar}' ha sido eliminada.")
            else:
                st.sidebar.error("Ingrese una palabra para eliminar.")

if __name__ == "__main__":
    main()
