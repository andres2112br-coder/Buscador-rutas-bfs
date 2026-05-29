#Ejercicio 1

n_str = input("Ingrese un numero entero positivo: ")

try:
    n = int(n_str)
except ValueError:
    print("Error: debes ingresar un numero entero valido.")
    raise SystemExit

if n <= 0:
    print("Error: el numero debe ser mayor que cero.")
    raise SystemExit

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

#Ejercicio 2 

aprobadas = 0
reprobadas = 0

while True:
    nota_str = input("Ingrese la nota (0-100) o -1 para finalizar: ")

    try:
        nota = int(nota_str)
    except ValueError:
        print("Entrada invalida. Debes ingresar un numero entero.")
        continue

    if nota == -1:
        break

    if nota >= 60:
        aprobadas += 1
    else:
        reprobadas += 1

print(f"Notas aprobadas: {aprobadas}")
print(f"Notas reprobadas: {reprobadas}")


#Ejercicio 3

while True:
    n_str = input("Ingrese un numero entero no negativo para calcular su factorial: ")
    try:
        n = int(n_str)
    except ValueError:
        print("Entrada invalida. Debes ingresar un numero entero.")
        continue

    if n < 0:
        print("El numero debe ser no negativo. Intente de nuevo.")
        continue

    break

factorial = 1

if n == 0:
    factorial = 1
else:
    for i in range(1, n + 1):
        factorial *= i

print(f"El factorial de {n} es: {factorial}")

#Ejercicio 4

usuario = input("Ingrese el nombre de usuario: ")

# Loop limitado a 3 intentos
for intento in range(1, 4):
    contrasena = input("Ingrese la contraseña: ")

    if usuario == "admin" and contrasena == "secret123":
        print("Acceso concedido.")
        break
    else:
        if intento < 3:
            print(f"Credenciales incorrectas. Intento {intento}/3. Tienes {3 - intento} intento(s) mas.")
        else:
            print("Sistema bloqueado. Has agotado los 3 intentos.")
