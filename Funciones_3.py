# EJERCICIO 3

def pedir_numeros_en_rango():
    minimo = int(input("Ingrese el valor mínimo del rango: "))
    maximo = int(input("Ingrese el valor máximo del rango: "))

    while minimo >= maximo:
        print("El mínimo debe ser menor que el máximo. Intente nuevamente.")
        minimo = int(input("Ingrese el valor mínimo del rango: "))
        maximo = int(input("Ingrese el valor máximo del rango: "))

    lista_numeros = []

    print(f"\n--- Ingrese 10 números entre {minimo} y {maximo} ---")
    i = 1
    while i <= 10:
        numero = int(input(f"Número #{i}: "))
        if minimo <= numero <= maximo:
            lista_numeros.append(numero)
            i += 1
        else:
            print(f"⚠ Número fuera de rango. Debe estar entre {minimo} y {maximo}.")

    return lista_numeros


# Programa principal 
lista = pedir_numeros_en_rango()

print("\n--- Lista de números ingresados ---")
print(lista)