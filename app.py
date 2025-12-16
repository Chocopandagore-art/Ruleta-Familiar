import streamlit as st

# 1. LOS DATOS (Esto no cambia, es tu "base de datos")
cie11_datos = {
    "01": {
        "titulo": "Ciertas enfermedades infecciosas o parasitarias",
        "bloques": {
            "Gastroenteritis o colitis": ["Cólera", "Shigelosis", "E. coli"],
            "Transmisión sexual": ["Sífilis", "Gonorrea", "Clamidia"],
            "Micobacteriosis": ["Tuberculosis", "Lepra"]
        }
    },
    "06": {
        "titulo": "Trastornos mentales y del comportamiento",
        "bloques": {
            "Trastornos del neurodesarrollo": ["Autismo", "TDAH"],
            "Esquizofrenia": ["Esquizofrenia", "Trastorno esquizoafectivo"]
        }
    }
}

# 2. LA INTERFAZ (Aquí usamos comandos de Streamlit)
st.title("🏥 Navegador CIE-11")
st.write("Selecciona un capítulo para ver los detalles.")

# Creamos una lista solo con los números de los capítulos (01, 06...)
lista_capitulos = list(cie11_datos.keys())

# EN LUGAR DE INPUT, USAMOS UN SELECTBOX (Menú desplegable)
# Esto guarda la elección del usuario en la variable 'opcion_usuario'
opcion_usuario = st.selectbox(
    "Selecciona el Capítulo:",
    lista_capitulos
)

# 3. LA LÓGICA (Mostrar lo que el usuario eligió)
if opcion_usuario:
    # Recuperamos la info de ese capítulo
    datos_capitulo = cie11_datos[opcion_usuario]
    
    # Mostramos el título grande
    st.header(f"Capítulo {opcion_usuario}: {datos_capitulo['titulo']}")
    
    st.divider() # Una línea visual divisoria
    
    # Mostramos los bloques de enfermedades
    for nombre_bloque, lista_enfermedades in datos_capitulo['bloques'].items():
        # Usamos expander para que se vea limpio (se abre al hacer clic)
        with st.expander(f"📂 {nombre_bloque}"):
            for enfermedad in lista_enfermedades:
                st.write(f"- {enfermedad}")
