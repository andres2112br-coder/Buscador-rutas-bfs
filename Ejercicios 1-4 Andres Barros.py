# Ejercicio: Contador de vocales y consonantes

frase = input("Ingresa una frase: ")

frase_normalizada = frase.lower()

vocales = "aeiou"
vocales_count = 0
consonantes_count = 0

for ch in frase_normalizada:
    if ch in vocales:
        vocales_count += 1
    elif ch.isalpha():
        consonantes_count += 1

print(f"La frase '{frase}' tiene {vocales_count} vocales y {consonantes_count} consonantes")

#Ejercicio: Adivina el numero

import random

def adivina_el_numero():
    """Juego: el programa genera un numero secreto entre 1 y 100 y el usuario debe adivinarlo."""

    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = input("Adivina el numero (1-100): ")

        if not intento.strip().lstrip("-").isdigit():
            print("Ingresa un numero entero valido.")
            continue

        numero_usuario = int(intento)

        if numero_usuario < 1 or numero_usuario > 100:
            print("El numero debe estar entre 1 y 100.")
            continue

        intentos += 1

        if numero_usuario == numero_secreto:
            print(f"Bien hecho sois un duro, {numero_secreto} en {intentos} intento(s).")
            break
        elif numero_usuario < numero_secreto:
            print("Tai cerca papi pero el numero que ingresaste es MENOR que el secreto.")
        else:
            print("Tai cerca papi pero el numero que ingresaste es MAYOR que el secreto.")


if __name__ == "__main__":
    adivina_el_numero()

#Ejercicio: Verificador de palindromos

def es_palindromo(palabra: str) -> bool:                
    normalizada = "".join(ch.lower() for ch in palabra if ch.isalnum())
    return normalizada == normalizada[::-1]


if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    resultado = es_palindromo(palabra)
    print(resultado)

#Ejercicio: Suma de numeros pares en una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        suma_pares += numero

print(f"La suma de los números pares es: {suma_pares}")
