#Ejercicio 4: Diagnóstico de una computadora que no enciende
respuesta1 = input("El equipo enciende? (si/no): ").strip().lower()

# Nivel 1
if respuesta1 == "no":
    cable = input("El cable de poder esta conectado? (si/no): ").strip().lower()

    # Nivel 2
    if cable == "si":
        enchufe = input("El enchufe tiene electricidad? (si/no): ").strip().lower()

        # Nivel 3
        if enchufe == "si":
            fuente = input("La fuente hace ruido o gira el ventilador? (si/no): ").strip().lower()

            # Nivel 4
            if fuente == "no":
                pitidos = input("Emite algun pitido al intentar encender? (si/no): ").strip().lower()

                # Nivel 5
                if pitidos == "no":
                    print("Diagnostico: la fuente esta averiada")
                else:
                    print("Rechazado por Nivel 5: hay pitidos, el problema podria no ser la fuente")
            else:
                print("Rechazado por Nivel 4: la fuente suena o el ventilador gira")
        else:
            print("Rechazado por Nivel 3: el enchufe no tiene electricidad")
    else:
        print("Rechazado por Nivel 2: el cable de poder no esta conectado")
else:
    print("Rechazado por Nivel 1: el equipo si enciende")


#Ejercicio 5: Crédito

contrato = input("Ingrese el tipo de contrato (indefinido u otro): ").strip().lower()

# Nivel 1
if contrato == "indefinido":
    ingresos = float(input("Ingrese sus ingresos: "))
    gastos = float(input("Ingrese sus gastos: "))

    # Nivel 2
    ahorro = ingresos - gastos
    if ahorro >= 1000:
        historial = input("Ingrese su historial crediticio (EXCELENTE/BUENO): ").strip().upper()

        # Nivel 3
        if historial == "EXCELENTE" or historial == "BUENO":
            pago_inicial = float(input("Ingrese el % de pago inicial: "))

            # Nivel 4
            if pago_inicial >= 20.0:
                fiador = input("¿Tiene fiador? (si/no): ").strip().lower()

                # Nivel 5
                if fiador == "si" or ahorro > 2000:
                    print("Crédito otorgado")
                else:
                    print("Rechazado por Nivel 5: no hay fiador y el ahorro no supera 2000")
            else:
                print("Rechazado por Nivel 4: pago inicial menor a 20.0%")
        else:
            print("Rechazado por Nivel 3: historial crediticio no cumple")
    else:
        print("Rechazado por Nivel 2: su ahorro es menor a 1000")
else:
    print("Rechazado por Nivel 1: contrato no es indefinido")
