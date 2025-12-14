import streamlit as st

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Taller UPDS", page_icon="🍃", layout="centered")

# --- 2. ESTILOS VISUALES (CSS) ---
st.markdown("""
    <style>
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
    .card {
        padding: 15px; 
        border-radius: 15px; 
        margin-bottom: 15px; 
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .blue {border-left: 8px solid #2196F3; background-color: #E3F2FD;}
    .pink {border-left: 8px solid #E91E63; background-color: #FCE4EC;}
    .orange {border-left: 8px solid #FF9800; background-color: #FFF3E0;}
    
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
    </style>
""", unsafe_allow_html=True)

# --- 3. ENCABEZADO ---
st.markdown('<div class="main-header">🍃 Mi Reflejo Alimentario</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Taller de Prevención UPDS - Confidencial</div>', unsafe_allow_html=True)

# --- 4. CUESTIONARIO ---

# MENTE
st.markdown('<div class="card blue"><h4>🧠 1. Nivel Mental</h4></div>', unsafe_allow_html=True)
m1 = st.checkbox("Clasifico rígidamente la comida en 'Buena' y 'Mala'.")
m2 = st.checkbox("Siento que mi valor depende de mi peso.")
m3 = st.checkbox("Me comparo con cuerpos en redes sociales.")
m4 = st.checkbox("Pienso en comida gran parte del día.")

# EMOCIÓN
st.markdown('<div class="card pink"><h4>❤️ 2. Nivel Emocional</h4></div>', unsafe_allow_html=True)
e1 = st.checkbox("Siento CULPA después de comer.")
e2 = st.checkbox("Como por ansiedad o tristeza.")
e3 = st.checkbox("Miedo a perder el control al comer.")
e4 = st.checkbox("Ansiedad en eventos sociales por la comida.")

# CONDUCTA
st.markdown('<div class="card orange"><h4>🏃 3. Nivel Conductual</h4></div>', unsafe_allow_html=True)
c1 = st.checkbox("Me salto comidas para 'compensar'.")
c2 = st.checkbox("Hago ejercicio por obligación.")
c3 = st.checkbox("Miento sobre lo que comí.")
c4 = st.checkbox("Tengo rituales estrictos (pesar comida, etc).")

# --- 5. RESULTADOS Y RANGOS ---
if st.button("✨ Ver mi Resultado ✨"):
    total_puntos = sum([m1, m2, m3, m4, e1, e2, e3, e4, c1, c2, c3, c4])
    st.write("---")
    
    if total_puntos <= 2:
        st.success(f"🌟 **ZONA VERDE (Puntos: {total_puntos}/12)**: Relación Flexible. ¡Sigue así!")
        st.balloons()
    elif total_puntos <= 6:
        st.warning(f"⚠️ **ZONA AMARILLA (Puntos: {total_puntos}/12)**: Señales de Alerta. Intenta ser más flexible.")
    else:
        st.error(f"🚩 **ZONA NARANJA (Puntos: {total_puntos}/12)**: Necesidad de Apoyo. No dudes en pedir ayuda.")

# --- 6. LOGO UPDS (ESTA ES LA PARTE QUE FALLABA) ---
st.write(" ")
st.markdown("---")

# ATENCIÓN: Todo el código del dibujo está DENTRO de estas tres comillas """
st.markdown("""
<div style="text-align: center; margin-top: 20px;">
    
    <svg width="200" height="180" viewBox="0 0 200 180" xmlns="http://www.w3.org/2000/svg">
        
        <circle cx="100" cy="20" r="12" fill="#2E7D32" />
        <circle cx="80" cy="40" r="12" fill="#2196F3" />
        <circle cx="120" cy="40" r="12" fill="#2196F3" />
        <circle cx="60" cy="60" r="12" fill="#E91E63" />
        <circle cx="100" cy="60" r="12" fill="#E91E63" />
        <circle cx="140" cy="60" r="12" fill="#E91E63" />
        <circle cx="80" cy="80" r="12" fill="#FF9800" />
        <circle cx="120" cy="80" r="12" fill="#FF9800" />
        <circle cx="100" cy="100" r="12" fill="#2E7D32" />

        <circle cx="100" cy="130" r="15" fill="#1565C0" />
        <path d="M100 145 L100 175 M100 150 Q70 140 60 100 M100 150 Q130 140 140 100" 
              stroke="#1565C0" stroke-width="12" stroke-linecap="round" fill="none"/>
              
        <text x="100" y="195" font-family="Arial" font-size="10" fill="#555" text-anchor="middle" font-weight="bold">
            UNIVERSIDAD PRIVADA DOMINGO SAVIO
        </text>
    </svg>
    <div style="color: #777; font-size: 12px; margin-top: 10px; font-style: italic;">
        Departamento de Bienestar Estudiantil
    </div>
</div>
""", unsafe_allow_html=True) 
# 👆 ¡NO BORRES ESTA ÚLTIMA LÍNEA! ES LA LLAVE QUE CIERRA EL DIBUJO.
