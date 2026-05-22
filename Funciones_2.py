# EJERCICIO 2

def guardar_en_posicion():
    lista_numeros = [0] * 10

    print("--- Lista inicializada ---")
    print(f"Lista actual: {lista_numeros}")

    posicion = int(input("\nIngrese la posición donde guardar (0-9): "))
    while posicion < 0 or posicion > 9:
        print("Posición inválida. Debe estar entre 0 y 9.")
        posicion = int(input("Ingrese la posición donde guardar (0-9): "))

    numero = int(input("Ingrese el número a guardar: "))

    lista_numeros[posicion] = numero

    return lista_numeros

# Programa principal
lista = guardar_en_posicion()

print("\n--- Lista resultante ---")
print(lista)