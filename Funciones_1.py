# EJERCICIO 1

def pedir_nombres():
    lista_nombres = []
    
    print("--- Ingrese 10 nombres ---")
    for i in range(1, 11):
        nombre = input(f"Ingrese el nombre #{i}: ")
        lista_nombres.append(nombre)
    
    return lista_nombres


# Programa principa
lista = pedir_nombres()

print("\n--- Nombres ingresados ---")
print(lista)