#Ejercicio 1
def invertir_diccionario(diccionario):
    resultado = {}
    for clave, valor in diccionario.items():
        if valor in resultado:
            resultado[valor] = resultado[valor] + (clave,)
        else:
            resultado[valor] = (clave,)
    return resultado

# Prueba
d = {"a": 1, "b": 2, "c": 1, "d": 3}
print(invertir_diccionario(d))
# {1: ('a', 'c'), 2: ('b',), 3: ('d',)}

#Ejercicio 2

def agrupar_anagramas(palabras):
    grupos = {}
    for palabra in palabras:
        clave = "".join(sorted(palabra))
        if clave in grupos:
            grupos[clave].append(palabra)
        else:
            grupos[clave] = [palabra]
    return list(grupos.values())

# Prueba
lista = ["amor", "roma", "mora", "perro", "ropem", "repom"]
print(agrupar_anagramas(lista))
# [['amor', 'roma', 'mora'], ['perro'], ['ropem', 'repom']]

#Ejercicio 3
def resumen_gastos(transacciones):
    resumen = {}
    total_general = 0
    for categoria, monto in transacciones:
        if categoria in resumen:
            resumen[categoria] += monto
        else:
            resumen[categoria] = monto
        total_general += monto
    return (resumen, total_general)

# Prueba
transacciones = [("pastelitos 1$", 650), ("Carritos de galeria", 150), ("pastelitos 1$", 650), ("magis tv", 2000)]
print(resumen_gastos(transacciones))
# ({'pastelitos 1$': 1300, 'Carritos de galeria': 150, 'magis tv': 2000}, 3450)

#Ejercicio 4

def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    for j in range(columnas):
        nueva_fila = tuple(matriz[i][j] for i in range(filas))
        resultado.append(nueva_fila)
    return resultado

# Prueba
matriz = [[1, 2, 3], [4, 5, 6]]
print(transponer_matriz(matriz))
# [(1, 4), (2, 5), (3, 6)]

#Ejercicio 5

def comprimir_rle(texto):
    if not texto:
        return []
    resultado = []
    letra_actual = texto[0]
    conteo = 1
    for i in range(1, len(texto)):
        if texto[i] == letra_actual:
            conteo += 1
        else:
            resultado.append((letra_actual, conteo))
            letra_actual = texto[i]
            conteo = 1
    resultado.append((letra_actual, conteo))
    return resultado

# Prueba
print(comprimir_rle("AAABBBCCDDDDEE"))
# [('A', 3), ('B', 3), ('C', 2), ('D', 4), ('E', 2)]

#Ejercicio 6

diccionario = {
    "clave": "bnc>>>>>cualquier otro banco de venezuela",  
    "nombre": "Andres",
    "logros": {
        "nombre_curso": "programacion",
        "clave": "Contraseña123",  
        "materia": {
            "nombre_materia": "programacion_basica_17400",
            "clave": "bleach"  
        }
    }
}

def buscar_en_diccionario(diccionario, buscar_clave):
    lista_resultado = []
    for clave, valor in diccionario.items():
        if clave == buscar_clave:
            lista_resultado.append(valor)
        
        if isinstance(valor, dict):
            resultado_niveles = buscar_en_diccionario(valor, buscar_clave)
            
            lista_resultado.extend(resultado_niveles)
    return lista_resultado

final = buscar_en_diccionario(diccionario, "clave")

print(final)

#Ejercicio 7

def detectar_colisiones(reuniones):
    reuniones_ordenadas = sorted(reuniones, key=lambda x: x[0])
    colisiones = []
    for i in range(len(reuniones_ordenadas) - 1):
        actual = reuniones_ordenadas[i]
        siguiente = reuniones_ordenadas[i + 1]
        if actual[1] > siguiente[0]:
            colisiones.append((actual, siguiente))
    return colisiones

# Prueba
agenda = [(9, 10), (10, 11), (9, 30, 10, 30)]
agenda = [(9, 10), (9.5, 10.5), (11, 12)]
print(detectar_colisiones(agenda))
# [((9, 10), (9.5, 10.5))]

#Ejercicio 8

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def traducir_morse(texto):
    # Si contiene puntos o guiones, es Morse -> texto
    if all(c in ".- /" for c in texto.strip()):
        inverso = {v: k for k, v in MORSE.items()}
        palabras = texto.strip().split(" / ")
        resultado = ""
        for palabra in palabras:
            for codigo in palabra.split():
                resultado += inverso.get(codigo, "?")
            resultado += " "
        return resultado.strip()
    else:
        # Texto -> Morse
        resultado = []
        for char in texto.upper():
            if char == " ":
                resultado.append("/")
            elif char in MORSE:
                resultado.append(MORSE[char])
        return " ".join(resultado)

# Prueba
print(traducir_morse("HOLA"))         # .... --- .-.. .-
print(traducir_morse(".... --- .-.. .-"))  # HOLA

#Ejercicio 9

def calcular_votacion(votos):
    puntajes = {}
    for primero, segundo, tercero in votos:
        for candidato, puntos in [(primero, 3), (segundo, 2), (tercero, 1)]:
            if candidato in puntajes:
                puntajes[candidato] += puntos
            else:
                puntajes[candidato] = puntos
    return sorted(puntajes.items(), key=lambda x: x[1], reverse=True)

# Prueba
votos = [("Ana", "Luis", "Mia"), ("Luis", "Ana", "Mia"), ("Ana", "Mia", "Luis")]
print(calcular_votacion(votos))
# [('Ana', 8), ('Luis', 6), ('Mia', 4)]

#Ejercicio 10

def actualizar_cache(cache, nuevas_visitas, limite):
    for url in nuevas_visitas:
        if url in cache:
            cache[url] += 1
        else:
            if len(cache) >= limite:
                # Eliminar la URL con menor frecuencia
                url_min = min(cache, key=lambda k: cache[k])
                del cache[url_min]
            cache[url] = 1
    return cache

# Prueba
cache = {"google.com": 5, "youtube.com": 3, "reddit.com": 1}
nuevas = ["twitter.com", "google.com", "tiktok.com"]
print(actualizar_cache(cache, nuevas, 3))
# {'youtube.com': 3, 'google.com': 6, 'twitter.com': 1}
# (reddit.com fue eliminado por tener frecuencia 1, luego twitter entra;
#  al entrar tiktok, se elimina twitter o reddit según el estado)