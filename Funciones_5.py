def buscar_menores(edades):
    menor_edad = edades[0]

# Primer recorrido: encontrar la edad mínima
    for edad in edades:
        if edad < menor_edad:
            menor_edad = edad

# Segundo recorrido: guardar índices de quienes tienen esa edad
    indices_menores = []
    for i in range(len(edades)):
        if edades[i] == menor_edad:
            indices_menores.append(i)

    return indices_menores


# Programa principal 
Nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia",
           "Ulises", "Sofia", "Maria", "Pedro", "Antonio",
           "Eugenia", "Soledad", "Mario", "Mariela"]

edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

indices = buscar_menores(edades)

print("--- Persona/s de menor edad ---")
for i in indices:
    print(f"Nombre: {Nombres[i]} | Edad: {edades[i]}")
