from listas_personas import (nombres, telefonos, mails, address, postalZip, region, country, edades)

# Opción 1 ──────────────────────────────────────────────
def importar_listas():
    print("Listas importadas correctamente.")
    print(f"   Total de usuarios: {len(nombres)}")

# Opción 2 ──────────────────────────────────────────────
def usuarios_mexico():
    print("\n=== Usuarios de México ===")
    for i in range(len(nombres)):
        if country[i] == "Mexico":
            print(f"Nombre:    {nombres[i]}")
            print(f"Teléfono:  {telefonos[i]}")
            print(f"Mail:      {mails[i]}")
            print(f"Dirección: {address[i]}")
            print(f"Región:    {region[i]}")
            print(f"C. Postal: {postalZip[i]}")
            print(f"Edad:      {edades[i]}")
            print("-" * 40)

# Opción 3 ──────────────────────────────────────────────
def usuarios_brasil_nombre_mail_tel():
    print("\n=== Usuarios de Brasil (nombre, mail y teléfono) ===")
    for i in range(len(nombres)):
        if country[i] == "Brazil":
            print(f"Nombre:   {nombres[i]}")
            print(f"Mail:     {mails[i]}")
            print(f"Teléfono: {telefonos[i]}")
            print("-" * 40)

# Opción 4 ──────────────────────────────────────────────
def usuario_mas_joven():
    print("\n=== Usuario/s más joven/es ===")
    edad_min = min(edades)
    for i in range(len(nombres)):
        if edades[i] == edad_min:
            print(f"Nombre:    {nombres[i]}")
            print(f"Teléfono:  {telefonos[i]}")
            print(f"Mail:      {mails[i]}")
            print(f"Dirección: {address[i]}")
            print(f"País:      {country[i]}")
            print(f"Edad:      {edades[i]}")
            print("-" * 40)

# Opción 5 ──────────────────────────────────────────────
def promedio_edad():
    promedio = sum(edades) / len(edades)
    print(f"\n=== Promedio de edad de usuarios ===")
    print(f"   Promedio: {promedio:.2f} años")

# Opción 6 ──────────────────────────────────────────────
def brasil_mayor_edad():
    print("\n=== Usuario de mayor edad en Brasil ===")
    edad_max = max(edades[i] for i in range(len(nombres)) if country[i] == "Brazil")
    for i in range(len(nombres)):
        if country[i] == "Brazil" and edades[i] == edad_max:
            print(f"Nombre:    {nombres[i]}")
            print(f"Teléfono:  {telefonos[i]}")
            print(f"Mail:      {mails[i]}")
            print(f"Dirección: {address[i]}")
            print(f"Región:    {region[i]}")
            print(f"Edad:      {edades[i]}")
            print("-" * 40)

# Opción 7 ──────────────────────────────────────────────
def mexico_brasil_postal_mayor_8000():
    print("\n=== Usuarios de México y Brasil con C. Postal > 8000 ===")
    for i in range(len(nombres)):
        if country[i] in ("Mexico", "Brazil") and postalZip[i] > 8000:
            print(f"Nombre:    {nombres[i]}")
            print(f"País:      {country[i]}")
            print(f"C. Postal: {postalZip[i]}")
            print(f"Teléfono:  {telefonos[i]}")
            print(f"Mail:      {mails[i]}")
            print(f"Dirección: {address[i]}")
            print("-" * 40)

# Opción 8 ──────────────────────────────────────────────
def italianos_mayores_40():
    print("\n=== Usuarios italianos mayores de 40 años ===")
    for i in range(len(nombres)):
        if country[i] == "Italy" and edades[i] > 40:
            print(f"Nombre:   {nombres[i]}")
            print(f"Mail:     {mails[i]}")
            print(f"Teléfono: {telefonos[i]}")
            print("-" * 40)

# MENÚ PRINCIPAL ────────────────────────────────────────
def menu():
    while True:
        print("\n     SISTEMA DE USUARIOS            ")
        print(" 1 - Importar listas                  ")
        print(" 2 - Usuarios de México               ")
        print(" 3 - Nombre/mail/tel de Brasil        ")
        print(" 4 - Usuario/s más joven/es           ")
        print(" 5 - Promedio de edad                 ")
        print(" 6 - Mayor edad en Brasil             ")
        print(" 7 - México/Brasil con CP > 8000      ")
        print(" 8 - Italianos mayores de 40          ")
        print(" 0 - Salir                            ")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            importar_listas()
        elif opcion == "2":
            usuarios_mexico()
        elif opcion == "3":
            usuarios_brasil_nombre_mail_tel()
        elif opcion == "4":
            usuario_mas_joven()
        elif opcion == "5":
            promedio_edad()
        elif opcion == "6":
            brasil_mayor_edad()
        elif opcion == "7":
            mexico_brasil_postal_mayor_8000()
        elif opcion == "8":
            italianos_mayores_40()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n Opción inválida. Ingresá un número del 0 al 8.")

# INICIO ────────────────────────────────────────────────
menu()