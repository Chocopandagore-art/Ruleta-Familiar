import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Taller UPDS", page_icon="🍃", layout="centered")

# --- 2. ESTILOS ---
st.markdown("""
    <style>
    .main-header {color: #2E7D32; text-align: center; font-size: 2rem; font-weight: bold; font-family: sans-serif;}
    .sub-text {text-align: center; color: #666; font-size: 1rem; margin-bottom: 20px;}
    .card {padding: 15px; border-radius: 15px; margin-bottom: 15px; background-color: white;}
    
    /* Colores específicos */
    .blue {border-left: 6px solid #2196F3; background-color: #E3F2FD;}
    .pink {border-left: 6px solid #E91E63; background-color: #FCE4EC;}
    .orange {border-left: 6px solid #FF9800; background-color: #FFF3E0;}
    
    /* Botón */
    .stButton>button {width: 100%; background: linear-gradient(90deg, #4CAF50 0%, #2E7D32 100%); color: white; border-radius: 20px; font-weight: bold; border: none; padding: 10px;}
    </style>
""", unsafe_allow_html=True)

# --- 3. ENCABEZADO ---
st.markdown('<div class="main-header">🍃 Mi Reflejo Alimentario</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Taller de Prevención UPDS - Confidencial</div>', unsafe_allow_html=True)
st.info("🔒 Tus respuestas son 100% anónimas.")

# --- 4. PREGUNTAS ---

# MENTE
st.markdown('<div class="card blue"><h4>🧠 1. Mente</h4></div>', unsafe_allow_html=True)
m1 = st.checkbox("Clasifico comida en 'Buena' y 'Mala'.")
m2 = st.checkbox("Mi valor depende de mi peso.")
m3 = st.checkbox("Me comparo con cuerpos en redes sociales.")
m4 = st.checkbox("Pienso en comida todo el tiempo.")

# EMOCIÓN
st.markdown('<div class="card pink"><h4>❤️ 2. Emoción</h4></div>', unsafe_allow_html=True)
e1 = st.checkbox("Siento culpa al comer.")
e2 = st.checkbox("Como por ansiedad o estrés.")
e3 = st.checkbox("Tengo miedo de perder el control.")
e4 = st.checkbox("Evito eventos sociales por la comida.")

# CONDUCTA
st.markdown('<div class="card orange"><h4>🏃 3. Conducta</h4></div>', unsafe_allow_html=True)
c1 = st.checkbox("Me salto comidas para compensar.")
c2 = st.checkbox("Hago ejercicio por obligación.")
c3 = st.checkbox("Miento sobre lo que comí.")
c4 = st.checkbox("Tengo rituales estrictos al comer.")

# --- 5. RESULTADOS ---
if st.button("✨ Ver Reflejo"):
    total = sum([m1, m2, m3, m4, e1, e2, e3, e4, c1, c2, c3, c4])
    st.write("---")
    if total == 0:
        st.success("🌟 Relación Saludable. ¡Sigue así!")
        st.balloons()
    else:
        st.warning(f"💡 Identificaste {total} temas para reflexionar.")
        st.write("No te juzgues. El primer paso es darse cuenta.")

# --- 6. LOGO FINAL (CORREGIDO) ---
st.write(" ")
st.markdown("""
<div style="text-align: center; margin-top: 20px;">
    <svg width="180" height="140" viewBox="0 0 200 160">
        <circle cx="60" cy="40" r="15" fill="#2196F3" opacity="0.9"/>
        <circle cx="100" cy="25" r="18" fill="#E91E63" opacity="0.9"/>
        <circle cx="140" cy="40" r="15" fill="#FF9800" opacity="0.9"/>
        <circle cx="80" cy="55" r="8" fill="#4CAF50" opacity="0.7"/>
        <circle cx="120" cy="55" r="8" fill="#4CAF50" opacity="0.7"/>
        <circle cx="100" cy="80" r="12" fill="#2E7D32"/>
        <path d="M100 95 L100 140 M100 95 Q70 80 60 40 M100 95 Q130 80 140 40" stroke="#2E7D32" stroke-width="8" fill="none"/>
        <text x="100" y="155" font-family="Arial" font-size="11" fill="#555" text-anchor="middle" font-weight="bold">UNIVERSIDAD PRIVADA DOMINGO SAVIO</text>
    </svg>
    <div style="color: #888; font-size: 12px; margin-top: 5px; font-style: italic;">
        "Conocerme es el primer paso para cuidarme"
    </div>
</div>
""", unsafe_allow_html=True)
