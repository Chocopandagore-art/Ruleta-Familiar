import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (Debe ser lo primero)
st.set_page_config(
    page_title="Taller UPDS - Mi Reflejo",
    page_icon="🍃",
    layout="centered"
)

# 2. ESTILOS VISUALES (CSS) - Para que se vea bonita
st.markdown("""
    <style>
    /* Estilos generales */
    .main-header {
        font-size: 2.2rem;
        color: #2E7D32;
        text-align: center;
        font-weight: bold;
        font-family: sans-serif;
    }
    .sub-text {
        text-align: center;
        color: #666;
        font-size: 1rem;
        margin-bottom: 25px;
    }
    
    /* Tarjetas de colores para las preguntas */
    .card-mental {
        background-color: #E3F2FD; /* Azulito */
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #2196F3;
        margin-bottom: 20px;
    }
    .card-emocional {
        background-color: #FCE4EC; /* Rosita */
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #E91E63;
        margin-bottom: 20px;
    }
    .card-conductual {
        background-color: #FFF3E0; /* Naranjita */
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #FF9800;
        margin-bottom: 20px;
    }
    
    /* Botón personalizado */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #4CAF50 0%, #2E7D32 100%);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        padding: 12px;
        margin-top: 20px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #66BB6A 0%, #43A047 100%);
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO CON LOGO PEQUEÑO
st.markdown("""
<div style="text-align: center;">
    <svg width="60" height="60" viewBox="0 0 100 100">
        <circle cx="50" cy="50" r="45" fill="#E8F5E9" />
        <path d="M50 25 Q30 50 50 85 Q70 50 50 25" fill="#4CAF50" />
    </svg>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🍃 Mi Reflejo Alimentario</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Herramienta de autoconocimiento confidencial.<br>Taller de Prevención UPDS</div>', unsafe_allow_html=True)

st.info("🔒 **Espacio Seguro:** Tus respuestas son anónimas y no se guardan. Sé sincero/a contigo mismo/a.")

# 4. PREGUNTAS (12 ITEMS)

# --- SECCIÓN 1: MENTE ---
st.markdown('<div class="card-mental"><h4>🧠 1. Lo que PIENSO</h4><p>Marca lo que te ocurre frecuentemente:</p></div>', unsafe_allow_html=True)
m1 = st.checkbox("Clasifico la comida rígidamente en 'Buena' y 'Mala'.")
m2 = st.checkbox("Siento que mi valor como persona depende del número en la balanza.")
m3 = st.checkbox("Me comparo constantemente con cuerpos que veo en redes sociales.")
m4 = st.checkbox("Tengo pensamientos constantes sobre comida que me distraen de estudiar.")

# --- SECCIÓN 2: EMOCIÓN ---
st.markdown('<div class="card-emocional"><h4>❤️ 2. Lo que SIENTO</h4><p>Reconoce tus emociones:</p></div>', unsafe_allow_html=True)
e1 = st.checkbox("Siento mucha CULPA o vergüenza después de comer algo 'rico'.")
e2 = st.checkbox("Como para tapar ansiedad, tristeza, estrés o aburrimiento.")
e3 = st.checkbox("Siento miedo intenso a perder el control si empiezo a comer.")
e4 = st.checkbox("Me genera ansiedad ir a eventos sociales donde no sé qué comida habrá.")

# --- SECCIÓN 3: CONDUCTA ---
st.markdown('<div class="card-conductual"><h4>🏃 3. Lo que HAGO</h4><p>Observa tus acciones:</p></div>', unsafe_allow_html=True)
c1 = st.checkbox("Me salto comidas (ayuno) intencionalmente para 'compensar'.")
c2 = st.checkbox("Hago ejercicio físico obligado/a para 'quemar', no por placer.")
c3 = st.checkbox("Como a escondidas o miento diciendo que ya comí cuando no es verdad.")
c4 = st.checkbox("Tengo rituales estrictos (cortar comida muy pequeña, tomar mucha agua para llenarme).")

st.write("---")

# 5. BOTÓN Y RESULTADOS
if st.button("✨ Ver mi Reflejo ✨"):
    
    # Contamos todas las alertas
    total_checks = sum([m1, m2, m3, m4, e1, e2, e3, e4, c1, c2, c3, c4])
    
    st.write(" ")
    
    # CASO A: TODO VERDE
    if total_checks == 0:
        st.balloons()
        st.success("🌟 **Zona de Bienestar y Flexibilidad**")
        st.markdown("""
        ¡Qué buena noticia! Tu relación con la alimentación parece ser flexible, intuitiva y libre de culpas.
        Comes para nutrirte y disfrutar. **¡Sigue protegiendo esa paz mental!**
        """)

    # CASO B: ALGUNAS SEÑALES
    else:
        st.warning(f"💡 **Has identificado {total_checks} áreas para reflexionar**")
        st.markdown("No te juzgues. Darse cuenta es el primer paso para sanar. Aquí tienes tu devolución:")
        
        # Devoluciones personalizadas por área
        if m1 or m2 or m3 or m4:
            st.markdown("🔹 **Sobre tu Mente:**")
            st.write("Tus pensamientos están siendo un poco rígidos. Pregúntate: *¿Quién puso esas reglas en mi cabeza? ¿Realmente me hacen feliz?*")
            
        if e1 or e2 or e3 or e4:
            st.markdown("🔹 **Sobre tus Emociones:**")
            st.write("Parece que la comida está ocupando un lugar emocional. Recuerda: *La comida nutre el cuerpo, pero no sana el corazón. Mereces consuelo real, no comestible.*")
            
        if c1 or c2 or c3 or c4:
            st.markdown("🔹 **Sobre tu Conducta:**")
            st.write("Tu cuerpo es sabio y se defiende del control excesivo. *Tratar de controlarlo con castigos solo genera más descontrol a largo plazo.*")

    st.write("---")
    st.info("📌 **Recuerda:** Esto no es un diagnóstico. Si alguna de estas señales te genera malestar, no dudes en acercarte al equipo de bienestar estudiantil.")
# 6. LOGO FINAL (SVG DIBUJADO)
st.write("---")
st.markdown("""
<div style="display: flex; justify-content: center; align-items: center; flex-direction: column; margin-top: 20px;">
    
    <svg width="200" height="160" viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
        <circle cx="60" cy="40" r="15" fill="#2196F3" opacity="0.9"/>
        <circle cx="100" cy="25" r="18" fill="#E91E63" opacity="0.9"/>
        <circle cx="140" cy="40" r="15" fill="#FF9800" opacity="0.9"/>
        <circle cx="80" cy="55" r="8" fill="#4CAF50" opacity="0.7"/>
        <circle cx="120" cy="55" r="8" fill="#4CAF50" opacity="0.7"/>
        <circle cx="100" cy="80" r="12" fill="#2E7D32"/>
        <path d="M100 95 L100 140 M100 95 Q70 80 60 40 M100 95 Q130 80 140 40" 
              stroke="#2E7D32" stroke-width="8" stroke-linecap="round" fill="none"/>
        <text x="100" y="155" font-family="Arial, sans-serif" font-size="11" fill="#555" text-anchor="middle" font-weight="bold">
            UNIVERSIDAD PRIVADA DOMINGO SAVIO
        </text>
    </svg>
    
    <div style="color: #888; font-size: 12px; margin-top: 5px; font-style: italic;">
        "Conocerme es el primer paso para cuidarme"
    </div>

</div>
""", unsafe_allow_html=True)
