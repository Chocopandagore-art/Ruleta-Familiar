import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Taller UPDS - Mi Reflejo",
    page_icon="🍃",
    layout="centered"
)

# 2. ESTILOS VISUALES (CSS)
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #2E7D32; /* Verde bosque */
        text-align: center;
        font-weight: bold;
        font-family: 'Helvetica', sans-serif;
    }
    .sub-text {
        text-align: center;
        color: #666;
        font-size: 1rem;
        margin-bottom: 20px;
    }
    /* Tarjetas */
    .card-mental {
        background-color: #E3F2FD;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #2196F3; /* Azul */
        margin-bottom: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .card-emocional {
        background-color: #FCE4EC;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #E91E63; /* Rosa */
        margin-bottom: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .card-conductual {
        background-color: #FFF3E0;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #FF9800; /* Naranja */
        margin-bottom: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    /* Botón */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #4CAF50 0%, #2E7D32 100%);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        padding: 12px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #43A047 0%, #1B5E20 100%);
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO CON LOGO SVG PEQUEÑO
# Dibujamos un mini icono temático arriba
st.markdown("""
<div style="text-align: center;">
    <svg width="60" height="60" viewBox="0 0 100 100">
        <circle cx="50" cy="50" r="45" fill="#E8F5E9" />
        <path d="M50 25 Q30 50 50 85 Q70 50 50 25" fill="#4CAF50" />
    </svg>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Mi Reflejo Alimentario</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Una herramienta confidencial de autoconocimiento.<br>Taller de Prevención UPDS</div>', unsafe_allow_html=True)

st.info("🔒 **Anonimato Total:** Tus respuestas no se guardan. Sé sincero/a contigo mismo/a.")

# 4. PREGUNTAS (ESTILO TARJETAS)

# --- MENTAL ---
st.markdown('<div class="card-mental"><h4>🧠 1. Mente (Pensamientos)</h4></div>', unsafe_allow_html=True)
m1 = st.checkbox("Clasifico la comida rígidamente en 'Buena' y 'Mala'.")
m2 = st.checkbox("Siento que valgo más o menos según lo que peso.")
m3 = st.checkbox("Me critico duramente al mirarme al espejo.")

# --- EMOCIONAL ---
st.markdown('<div class="card-emocional"><h4>❤️ 2. Emoción (Sentimientos)</h4></div>', unsafe_allow_html=True)
e1 = st.checkbox("Siento mucha CULPA después de comer algo 'rico'.")
e2 = st.checkbox("Como para tapar ansiedad, tristeza o estrés.")
e3 = st.checkbox("Me da miedo ir a eventos sociales donde hay comida.")

# --- CONDUCTUAL ---
st.markdown('<div class="card-conductual"><h4>🏃 3. Conducta (Acciones)</h4></div>', unsafe_allow_html=True)
c1 = st.checkbox("Me salto comidas (ayuno) para 'compensar' excesos.")
c2 = st.checkbox("Hago ejercicio solo para 'quemar', no por placer.")
c3 = st.checkbox("Tengo reglas estrictas (pesar comida, trozos pequeños).")

st.write("---")

# 5. RESULTADOS
if st.button("✨ Ver mi Reflejo ✨"):
    
    total = sum([m1, m2, m3, e1, e2, e3, c1, c2, c3])
    
    if total == 0:
        st.balloons()
        st.success("🌟 **Zona de Bienestar y Flexibilidad**")
        st.write("Tu relación con la alimentación parece sana y libre. ¡Sigue nutriendo esa paz!")
    else:
        st.warning(f"💡 **Has identificado {total} áreas para reflexionar**")
        st.write("No es un diagnóstico, es una invitación a ser más amable contigo.")
        
        if m1 or m2 or m3:
            st.markdown("🔹 **Mente:** Desafía esas reglas. ¿La comida tiene moral?")
        if e1 or e2 or e3:
            st.markdown("🔹 **Emoción:** Permítete sentir sin usar la comida como escudo.")
        if c1 or c2 or c3:
            st.markdown("🔹 **Cuerpo:** Tu cuerpo necesita energía, no castigos.")

st.write(" ")
st.write(" ")

# 6. EL LOGO NUEVO (SVG) AL FINAL
st.markdown("---")
st.markdown("""
<div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <svg width="150" height="120" viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
        
        <circle cx="60" cy="40" r="15" fill="#2196F3" opacity="0.9"/>
        <circle cx="100" cy="25" r="18" fill="#E91E63" opacity="0.9"/>
        <circle cx="140" cy="40" r="15" fill="#FF9800" opacity="0.9"/>
        
        <circle cx="80" cy="55" r="8" fill="#4CAF50" opacity="0.7"/>
        <circle cx="120" cy="55" r="8" fill="#4CAF50" opacity="0.7"/>

        <circle cx="100" cy="80" r="12" fill="#2E7D32"/>
        <path d="M100 95 
                 L100 140 
                 M100 95 
                 Q70 80 60 40 
                 M100 95 
                 Q130 80 140 40" 
              stroke="#2E7D32" stroke-width="8" stroke-linecap="round" fill="none"/>
              
        <text x="100" y="155" font-family="Arial, sans-serif" font-size="12" fill="#555" text-anchor="middle" font-weight="bold">
            UNIVERSIDAD PRIVADA DOMINGO SAVIO
        </text>
    </svg>
    
    <div style="color: #888; font-size: 12px; margin-top: 5px;">
        Taller de Psicoeducación
    </div>
</div>
""", unsafe_allow_html=True)
