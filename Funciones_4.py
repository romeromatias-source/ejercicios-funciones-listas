# EJERCICIO 4

def buscar_numero(lista, numero):
    for elemento in lista:
        if elemento == numero:
            return True
    return False


# Programa principal 
lista_numeros = [5, 12, 33, 7, 89, 44, 21, 63, 18, 50]

print("--- Lista de números ---")
print(lista_numeros)

numero_buscar = int(input("\nIngrese el número a buscar: "))

resultado = buscar_numero(lista_numeros, numero_buscar)

print(f"\n¿El número {numero_buscar} existe en la lista? ")
if resultado:
    print(f"Si, el número {numero_buscar} existe en la lista")
else:
    print(f"No, el número {numero_buscar} no existe en la lista")
