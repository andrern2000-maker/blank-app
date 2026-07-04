import re
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------------
# Configuración de la página
# -------------------------------------------------

st.set_page_config(
    page_title="SportLab 360",
    page_icon="🏪",
    layout="wide"
)

st.title("🏪 SportLab 360")

st.subheader("Prototipo interactivo de Trade Marketing")

st.markdown(
    """
Visualización 3D del layout de la tienda.

- Arrastra para rotar.
- Usa la rueda del mouse para hacer zoom.
- Haz clic sobre las zonas para visualizar la información.
"""
)

st.divider()

# -------------------------------------------------
# Leer archivos
# -------------------------------------------------

html = Path("index.html").read_text(encoding="utf-8")
css = Path("style.css").read_text(encoding="utf-8")
js = Path("script.js").read_text(encoding="utf-8")

# -------------------------------------------------
# Reemplazar referencias externas
# -------------------------------------------------

html = re.sub(
    r'<link.*?href="style\.css".*?>',
    f"<style>\n{css}\n</style>",
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<script.*?src="script\.js".*?></script>',
    f"<script>\n{js}\n</script>",
    html,
    flags=re.DOTALL
)

# -------------------------------------------------
# Mostrar HTML
# -------------------------------------------------

components.html(
    html,
    height=950,
    scrolling=False,
)

st.divider()

st.caption("SportLab 360 • Streamlit + HTML + Three.js")
