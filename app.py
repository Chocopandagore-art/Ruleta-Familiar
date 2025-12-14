import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Taller UPDS", page_icon="🍃", layout="centered")

# --- 2. ESTILOS (Colores y Diseño) ---
st.markdown("""
    <style>
    /* Título principal */
    .main-header {
        color: #2E7D32; 
        text-align: center; 
        font-size: 2.5rem; 
        font-weight: bold; 
        font-family: sans-serif;
        margin-bottom: 0px;
    }
    .sub-text {
        text-align: center; 
        color: #666; 
        font-size: 1.2rem; 
        margin-bottom: 30px;
    }
    
    /* Estilo de las Tarjetas (Cajas de colores) */
    .card {
        padding: 20px; 
        border-radius: 12px; 
        margin-bottom: 20px; 
        background-color: white;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    /* Bordes de colores para identificar dimensiones */
    .blue {border-left: 10px solid #2196F3; background-color: #E3F2FD;}
    .pink {border-left: 10px solid #E91E63; background-color: #FCE4EC;}
    .orange {border-left: 10px solid #FF9800; background-color: #FFF3E0;}
    
    /* Botón grande y verde */
    .stButton>button {
        width: 100%; 
        background-color: #4CAF50; 
        color: white; 
        border-radius: 10px; 
        font-weight: bold; 
        border: none; 
        padding: 15px;
        font-size: 20px;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background-color: #2E7D32;
    }
    
    /* Frase final */
    .quote {
        text-align: center;
        font-style: italic;
        color: #555;
        font-size: 1.1rem;
        margin-top: 40px;
        padding: 20px;
        border-top: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. ENCABEZADO ---
st.markdown('<div class="main-header">Mi Reflejo Alimentario 🍃</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Guía de Auto-Observación Confidencial</div>', unsafe_allow_html=True)
st.info("🔒 **Instrucciones:** Marca las afirmaciones con las que te identifiques. Tus respuestas son anónimas.")

# --- 4. LAS 3 DIMENSIONES (INPUTS) ---

# DIMENSIÓN 1: MENTAL
st.markdown('<div class="card blue"><h3>🧠 1. Lo que PIENSO (Dimensión Mental)</h3></div>', unsafe_allow_html=True)
m1 = st.checkbox("Clasifico rígidamente la comida en 'Buena' y 'Mala'.")
m2 = st.checkbox("Siento que mi valor como persona depende del número en la balanza.")
m3 = st.checkbox("Me comparo constantemente con cuerpos que veo en redes sociales.")
m4 = st.checkbox("Tengo pensamientos sobre comida o dietas que ocupan gran parte de mi día.")

# DIMENSIÓN 2: EMOCIONAL
st.markdown('<div class="card pink"><h3>❤️ 2. Lo que SIENTO (Dimensión Emocional)</h3></div>', unsafe_allow_html=True)
e1 = st.checkbox("Siento mucha CULPA o vergüenza después de comer ciertos alimentos.")
e2 = st.checkbox("Uso la comida para calmar ansiedad, tristeza, aburrimiento o estrés.")
e3 = st.checkbox("Siento miedo intenso a perder el control si empiezo a comer.")
e4 = st.checkbox("Me genera ansiedad ir a eventos sociales donde no controlo la comida.")

# DIMENSIÓN 3: CONDUCTUAL
st.markdown('<div class="card orange"><h3>🏃 3. Lo que HAGO (Dimensión Conductual)</h3></div>', unsafe_allow_html=True)
c1 = st.checkbox("Me salto comidas (ayuno) intencionalmente para 'compensar' lo que comí.")
c2 = st.checkbox("Hago ejercicio físico obligado/a para 'quemar' calorías, no por placer.")
c3 = st.checkbox("Como a escondidas o miento diciendo que ya comí cuando no es verdad.")
c4 = st.checkbox("Tengo rituales estrictos (cortar comida muy pequeña, tomar mucha agua para llenarme).")

# --- 5. LÓGICA DE REFLEXIÓN (SEMÁFORO) ---
if st.button("✨ Ver mi Reflexión ✨"):
    
    # Calculamos el total (Máximo 12 puntos)
    total = sum([m1, m2, m3, m4, e1, e2, e3, e4, c1, c2, c3, c4])
    
    st.write("---")
    
    # RANGO 1: ZONA VERDE (0 a 2 puntos)
    if total <= 2:
        st.success(f"🌟 **ZONA DE BIENESTAR (Tu resultado: {total}/12)**")
        st.markdown("""
        **Tu reflejo muestra una relación flexible y amable.**
        
        Parece que comes para nutrirte y disfrutar, escuchando a tu cuerpo. Entiendes que tu valía no depende de tu imagen.
        
        * **Reflexión:** Sigue cultivando esta libertad. Eres un ejemplo de que se puede vivir en paz con la comida.
        """)
        st.balloons()

    # RANGO 2: ZONA AMARILLA (3 a 6 puntos)
    elif total <= 6:
        st.warning(f"⚠️ **ZONA DE ALERTA (Tu resultado: {total}/12)**")
        st.markdown("""
        **Tu reflejo muestra ciertas reglas rígidas.**
        
        Has identificado comportamientos o pensamientos que te generan tensión. No es grave, pero es una "luz amarilla" en el tablero de tu auto.
        
        * **Reflexión:** ¿Esas reglas te ayudan o te limitan? Intenta esta semana romper una pequeña regla (ej. come ese chocolate sin culpa) y observa qué pasa. Verás que no ocurre nada malo.
        """)

    # RANGO 3: ZONA NARANJA (7 a 12 puntos)
    else:
        st.error(f"🚩 **ZONA DE CUIDADO (Tu resultado: {total}/12)**")
        st.markdown("""
        **Tu reflejo indica que estás sufriendo.**
        
        Tus respuestas muestran que la comida y la imagen ocupan demasiado espacio en tu mente, generando dolor o ansiedad. No tienes por qué vivir así.
        
        * **Reflexión:** La fortaleza no es aguantar solo/a, es pedir ayuda. Te invitamos a acercarte al Gabinete de Bienestar. Mereces recuperar tu paz.
        """)

# --- 6. FRASE FINAL (SIN LOGO) ---
st.markdown("""
    <div class="quote">
        "Tu cuerpo es el vehículo de tus sueños, no el destino final.<br>Cuídalo, escúchalo y respétalo."
        <br><br>
        <strong>Taller de Prevención y Psicoeducación UPDS</strong>
    </div>
""", unsafe_allow_html=True)
