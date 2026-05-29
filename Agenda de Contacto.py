agenda = {}  

print("--- Agenda de Contactos Simple ---")

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1. Añadir un contacto")
    print("2. Buscar un contacto")
    print("3. Listar todos los contactos")
    print("4. Salir")

    opcion = input("Elige una opcion: ").strip()

    # 1) Añadir contacto
    if opcion == "1":
        print("\n--- Añadir contacto ---")
        nombre = input("Nombre: ").strip()
        telefono = input("Numero de telefono: ").strip()

        if not nombre:
            print("El nombre no puede estar vacio.")
            continue
        if not telefono:
            print("El telefono no puede estar vacio.")
            continue

        
        agenda[nombre] = telefono
        print(f"Contacto guardado: {nombre} -> {telefono}")

    # 2) Buscar contacto
    elif opcion == "2":
        print("\n--- Buscar contacto ---")
        nombre_buscado = input("Nombre a buscar: ").strip()

        if not agenda:
            print("No hay contactos guardados.")
            continue

        if not nombre_buscado:
            print("El nombre no puede estar vacio.")
            continue

        if nombre_buscado in agenda:
            print(f"Telefono de {nombre_buscado}: {agenda[nombre_buscado]}")
        else:
            
            nombre_lower = nombre_buscado.lower()
            encontrado = None
            for nombre in agenda.keys():
                if nombre.lower() == nombre_lower:
                    encontrado = nombre
                    break

            if encontrado is not None:
                print(f"Telefono de {encontrado}: {agenda[encontrado]}")
            else:
                print(f"No se encontro el contacto: {nombre_buscado}")

    # 3) Listar todos
    elif opcion == "3":
        print("\n--- Lista de contactos ---")
        if not agenda:
            print("No hay contactos guardados.")
        else:
            for nombre, telefono in agenda.items():
                print(f"Nombre: {nombre}, Telefono: {telefono}")

    # 4) Salir
    elif opcion == "4":
        print("Hasta luego")
        break

    # Opcion no valida
    else:
        print("Opcion no valida. Elige una opcion del 1 al 4.")

    # Pausa para que el usuario pueda leer el mensaje antes de volver al menú
    input("\nPresiona Enter para continuar...")