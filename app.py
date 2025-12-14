import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Taller UPDS", page_icon="🍃", layout="centered")

# --- 2. ESTILOS VISUALES (CSS) ---
st.markdown("""
    <style>
    /* Estilo del Título */
    .main-header {
        color: #004d40; 
        text-align: center; 
        font-size: 2.2rem; 
        font-weight: bold; 
        font-family: sans-serif;
    }
    .sub-text {
        text-align: center; 
        color: #666; 
        font-size: 1rem; 
        margin-bottom: 20px;
    }
    
    /* Tarjetas de preguntas */
    .card {
        padding: 15px; 
        border-radius: 15px; 
        margin-bottom: 15px; 
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Colores por sección */
    .blue {border-left: 8px solid #2196F3; background-color: #E3F2FD;}
    .pink {border-left: 8px solid #E91E63; background-color: #FCE4EC;}
    .orange {border-left: 8px solid #FF9800; background-color: #FFF3E0;}
    
    /* Estilo del Botón */
    .stButton>button {
        width: 100%; 
        background: linear-gradient(90deg, #2E7D32 0%, #1B5E20 100%); 
        color: white; 
        border-radius: 20px; 
        font-weight: bold; 
        border: none; 
        padding: 12px;
        font-size: 18px;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. ENCABEZADO ---
st.markdown('<div class="main-header">🍃 Mi Reflejo Alimentario</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Taller de Prevención de TCA - UPDS<br>Encuesta Anónima y Confidencial</div>', unsafe_allow_html=True)

# --- 4. CUESTIONARIO ---

# SECCIÓN MENTE (Azul)
st.markdown('<div class="card blue"><h4>🧠 1. Nivel Mental (Mis Pensamientos)</h4></div>', unsafe_allow_html=True)
m1 = st.checkbox("Clasifico rígidamente la comida en 'Buena' y 'Mala'.")
m2 = st.checkbox("Siento que mi valor como persona depende de mi peso o figura.")
m3 = st.checkbox("Me comparo constantemente con cuerpos que veo en redes sociales.")
m4 = st.checkbox("Tengo pensamientos sobre comida o dietas gran parte del día.")

# SECCIÓN EMOCIÓN (Rosa)
st.markdown('<div class="card pink"><h4>❤️ 2. Nivel Emocional (Mis Sentimientos)</h4></div>', unsafe_allow_html=True)
e1 = st.checkbox("Siento mucha CULPA o vergüenza después de comer ciertos alimentos.")
e2 = st.checkbox("Uso la comida para gestionar ansiedad, tristeza o estrés.")
e3 = st.checkbox("Siento miedo intenso a perder el control si empiezo a comer.")
e4 = st.checkbox("Me genera ansiedad ir a eventos sociales donde habrá comida.")

# SECCIÓN CONDUCTA (Naranja)
st.markdown('<div class="card orange"><h4>🏃 3. Nivel Conductual (Mis Acciones)</h4></div>', unsafe_allow_html=True)
c1 = st.checkbox("Me salto comidas (ayuno) intencionalmente para 'compensar'.")
c2 = st.checkbox("Hago ejercicio físico obligado/a para 'quemar', no por placer.")
c3 = st.checkbox("Como a escondidas o miento diciendo que ya comí.")
c4 = st.checkbox("Tengo rituales estrictos (cortar comida muy pequeña, pesar todo).")

# --- 5. LÓGICA DE RANGOS Y RESULTADOS ---
if st.button("✨ Ver mi Resultado ✨"):
    
    # Sumamos todas las selecciones
    total_puntos = sum([m1, m2, m3, m4, e1, e2, e3, e4, c1, c2, c3, c4])
    
    st.write("---")
    
    # RANGO 1: ZONA VERDE (0 a 2 puntos)
    if total_puntos <= 2:
        st.success(f"🌟 **ZONA VERDE: RELACIÓN FLEXIBLE (Puntos: {total_puntos}/12)**")
        st.markdown("""
        **¡Excelente noticia!** Tus respuestas indican una relación saludable y flexible con la alimentación.
        * Comes para nutrirte y disfrutar.
        * Tu cuerpo es tu aliado, no tu enemigo.
        * **Consejo:** ¡Sigue protegiendo esta paz mental y ayuda a otros con tu ejemplo!
        """)
        st.balloons()

    # RANGO 2: ZONA AMARILLA (3 a 6 puntos)
    elif total_puntos <= 6:
        st.warning(f"⚠️ **ZONA AMARILLA: SEÑALES DE ALERTA (Puntos: {total_puntos}/12)**")
        st.markdown("""
        **Momento de reflexionar.** Has identificado varias conductas o pensamientos rígidos.
        * No es un trastorno, pero indica que la relación con la comida te está generando cierto estrés.
        * Es probable que estés siguiendo muchas "reglas" externas en lugar de escuchar a tu cuerpo.
        * **Consejo:** Intenta flexibilizar una de esas reglas esta semana. ¿Qué pasaría si no fueras tan estricto/a contigo?
        """)

    # RANGO 3: ZONA NARANJA (7 a 12 puntos)
    else:
        st.error(f"🚩 **ZONA NARANJA: NECESIDAD DE APOYO (Puntos: {total_puntos}/12)**")
        st.markdown("""
        **Tu bienestar es prioridad.** Tus respuestas indican un nivel alto de sufrimiento o rigidez respecto a la comida.
        * Es posible que esto esté afectando tu calidad de vida, tus estudios o tu felicidad diaria.
        * No tienes que cargar con esto en soledad.
        * **Consejo:** Te invitamos a acercarte al Gabinete Psicológico de la universidad o hablar con un profesional de confianza. Mereces vivir sin esta presión.
        """)

# --- 6. LOGO UPDS (DIBUJADO CON CÓDIGO) ---
st.write(" ")
st.write(" ")
st.markdown("---")

# Aquí dibujamos el logo estilo UPDS: Figura humana sosteniendo el rombo de esferas
st.markdown("""
<div style="text-align: center;">
    <svg width="200" height="180" viewBox="0 0 200 180" xmlns="http://www.w3.org/2000/svg">
        
        <circle cx="100" cy="20" r="12" fill="#2E7D32" /> <circle cx="80" cy="40" r="12" fill="#2196F3" /> <circle cx="120" cy="40" r="12" fill="#2196F3" /> <circle cx="60" cy="60" r="12" fill="#E91E63" /> <circle cx="100" cy="60" r="12" fill="#E91E63" /> <circle cx="140" cy="60" r="12" fill="#E91E63" /> <circle cx="80" cy="80" r="12" fill="#FF9800" /> <circle cx="120" cy="80" r="12" fill="#FF9800" /> <circle cx="100" cy="100" r="12" fill="#2E7D32" /> <circle cx="100" cy="130" r="15" fill="#1565C0" /> <path d="M100 145 
                 L100 175 
                 M100 150 
                 Q70 140 60 100 
                 M100 150 
                 Q130 140 140 100" 
              stroke="#1565C0" stroke-width="12" stroke-linecap="round" fill="none"/>
              
        <text x="100" y="195" font-family="Arial, sans-serif" font-size="10" fill="#555" text-anchor="middle" font-weight="bold" letter-spacing="1">
            UNIVERSIDAD PRIVADA DOMINGO SAVIO
        </text>
    </svg>
    
    <div style="color: #777; font-size: 12px; margin-top: 10px; font-style: italic;">
        Departamento de Bienestar Estudiantil
    </div>
</div>
""", unsafe_allow_html=True)
