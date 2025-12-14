import streamlit as st
import random

# 1. TÍTULO Y DISEÑO
st.title("🧹 Ruleta de Tareas Familiar")
st.write("¡Evita las discusiones y deja que el azar decida!")

# 2. ENTRADAS DE DATOS (Input)
texto_nombres = st.text_area("¿Quiénes participan?", "Daniel, Elizabeth")
texto_tareas = st.text_area("¿Qué hay que hacer?", "Barrer, Cocinar, Pasear a Bjork")

# 3. EL BOTÓN Y LA LÓGICA
if st.button("¡Sortear Tareas! 🎲"):
    
    nombres = [n.strip() for n in texto_nombres.split(',') if n.strip()]
    tareas = [t.strip() for t in texto_tareas.split(',') if t.strip()]
    
    if not nombres or not tareas:
        st.error("⚠️ Faltan nombres o tareas.")
    else:
        random.shuffle(tareas)
        st.success("✅ ¡Sorteo Realizado!")
        
        for i, tarea in enumerate(tareas):
            persona = nombres[i % len(nombres)]
            st.write(f"👉 **{persona}** le toca: {tarea}")
