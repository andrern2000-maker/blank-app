import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ---------------------------------------
# Configuración de la página
# ---------------------------------------
st.set_page_config(
    page_title="Mi Modelo",
    page_icon="📊",
    layout="wide",
)

# ---------------------------------------
# Título
# ---------------------------------------
st.title("Modelo Interactivo")

st.markdown("""
### Visualización del prototipo

A continuación se presenta el modelo interactivo desarrollado en HTML.
Puede utilizar todas sus funcionalidades directamente desde esta aplicación.
""")

st.divider()

# ---------------------------------------
# Cargar HTML
# ---------------------------------------
html_path = Path("index.html")

if html_path.exists():

    html_content = html_path.read_text(
        encoding="utf-8"
    )

    components.html(
        html_content,
        height=900,
        scrolling=True,
    )

else:

    st.error("No se encontró el archivo html/index.html")

st.divider()

st.subheader("Información")

st.write("""
Este prototipo ha sido desplegado mediante Streamlit e incrusta el archivo HTML
almacenado dentro del repositorio de GitHub.
""")
