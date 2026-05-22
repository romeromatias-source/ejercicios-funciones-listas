import listas_personas 

# Función que muestra los nombres
def mostrar_nombres():
    print("=== Lista de personas ===")
    for i, nombre in enumerate(listas_personas.nombres, start=1):
        print(f"{i}. {nombre}")
        
mostrar_nombres()