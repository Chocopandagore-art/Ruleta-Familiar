# ESTO SON LOS DATOS (Tu "Base de Datos" simulada)
# En la vida real, esto estaría en un archivo separado (.json)
cie11_datos = {
    "01": {
        "titulo": "Ciertas enfermedades infecciosas o parasitarias",
        "bloques": {
            "Gastroenteritis o colitis": {
                "rango": "1A00–1A4Z",
                "detalle": ["Cólera", "Shigelosis", "E. coli"]
            },
            "Transmisión sexual": {
                "rango": "1A60–1A9Z",
                "detalle": ["Sífilis", "Gonorrea", "Clamidia"]
            },
            "Micobacteriosis": {
                "rango": "1B10–1B1Z",
                "detalle": ["Tuberculosis", "Lepra"]
            }
        }
    },
    "06": {
        "titulo": "Trastornos mentales, del comportamiento o del neurodesarrollo",
        "bloques": {
            "Trastornos del neurodesarrollo": {
                "rango": "6A00–6A0Z",
                "detalle": ["Autismo", "TDAH"]
            },
            "Esquizofrenia": {
                "rango": "6A20–6A2Z",
                "detalle": ["Esquizofrenia", "Trastorno esquizoafectivo"]
            }
        }
    }
}

# ESTA ES LA LÓGICA (Tu programa en Python)
# Fíjate que es corto y sirve para 2 capítulos o para 25.
def navegar_cie11(datos):
    print("--- NAVEGADOR CIE-11 ---")
    
    # 1. Mostrar Capítulos
    for id_cap, info in datos.items():
        print(f"[{id_cap}] {info['titulo']}")
    
    eleccion = input("\nElige el número de capítulo (ej. 01): ")
    
    if eleccion in datos:
        capitulo = datos[eleccion]
        print(f"\nEntrando a: {capitulo['titulo']}")
        print("="*40)
        
        # 2. Mostrar Bloques dentro del capítulo
        for nombre_bloque, contenido in capitulo['bloques'].items():
            print(f"> {nombre_bloque} (Códigos: {contenido['rango']})")
            # 3. Mostrar enfermedades específicas
            for enfermedad in contenido['detalle']:
                print(f"   - {enfermedad}")
            print("-" * 20)
    else:
        print("Capítulo no encontrado.")

# Ejecutamos el programa
navegar_cie11(cie11_datos)
