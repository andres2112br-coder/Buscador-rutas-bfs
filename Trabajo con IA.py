#Ejercicio 1
def encontrar_ruta_logistica(grafo, nodo_inicio, nodo_fin, bloqueados):
    """Encuentra una ruta en el grafo evitando nodos bloqueados.

    Parámetros:
    - grafo: dict donde cada clave es un nodo y su valor es la lista de nodos conectados.
    - nodo_inicio: nodo de partida.
    - nodo_fin: nodo destino.
    - bloqueados: lista o conjunto de nodos que no pueden usarse.

    Retorna:
    - lista con la ruta desde inicio hasta fin, o [] si no existe ruta.
    """
    bloqueados = set(bloqueados)

    if nodo_inicio in bloqueados or nodo_fin in bloqueados:
        return []
    if nodo_inicio not in grafo or nodo_fin not in grafo:
        return []

    # Cola manual para BFS
    cola = [nodo_inicio]
    visitados = {nodo_inicio}
    padre = {nodo_inicio: None}

    while cola:
        actual = cola.pop(0)

        if actual == nodo_fin:
            # Reconstruir ruta
            ruta = []
            nodo = nodo_fin
            while nodo is not None:
                ruta.append(nodo)
                nodo = padre[nodo]
            return ruta[::-1]

        for vecino in grafo.get(actual, []):
            if vecino in bloqueados or vecino in visitados:
                continue
            visitados.add(vecino)
            padre[vecino] = actual
            cola.append(vecino)

    return []

#Ejercicio 2

def validar_con_autómata(cadena, estado_inicial, estados_aceptacion, transiciones):
    """Valida una cadena usando un AFD definido por transiciones.

    Parámetros:
    - cadena: texto a evaluar.
    - estado_inicial: estado donde empieza el autómata.
    - estados_aceptacion: lista o conjunto de estados finales aceptados.
    - transiciones: dict {estado: {caracter: siguiente_estado}}.

    Retorna:
    - True si la cadena termina en un estado de aceptación, False en caso contrario.
    """
    estado_actual = estado_inicial

    for caracter in cadena:
        if estado_actual not in transiciones:
            return False
        if caracter not in transiciones[estado_actual]:
            return False
        estado_actual = transiciones[estado_actual][caracter]

    return estado_actual in estados_aceptacion


#Ejercicio 3

def validar_tablero_sudoku(tablero):
    """Valida un tablero 9x9 de Sudoku en su estado actual.

    Parámetros:
    - tablero: lista de 9 listas, cada una con 9 enteros del 0 al 9.

    Retorna:
    - True si el tablero cumple las reglas de Sudoku hasta el momento.
    - False si hay un conflicto en filas, columnas o subcuadrículas.
    """
    if len(tablero) != 9 or any(len(fila) != 9 for fila in tablero):
        return False

    filas = [set() for _ in range(9)]
    columnas = [set() for _ in range(9)]
    subcuadriculas = {(i, j): set() for i in range(3) for j in range(3)}

    for fila_idx in range(9):
        for col_idx in range(9):
            valor = tablero[fila_idx][col_idx]
            if valor == 0:
                continue
            if not 1 <= valor <= 9:
                return False

            if valor in filas[fila_idx]:
                return False
            filas[fila_idx].add(valor)

            if valor in columnas[col_idx]:
                return False
            columnas[col_idx].add(valor)

            clave_subcuad = (fila_idx // 3, col_idx // 3)
            if valor in subcuadriculas[clave_subcuad]:
                return False
            subcuadriculas[clave_subcuad].add(valor)

    return True

#Ejercicio 4

def justify_text(words, max_width):
    """Justifica una lista de palabras a un ancho exacto `max_width`.

    Args:
        words (list[str]): lista de palabras.
        max_width (int): ancho máximo de cada línea.

    Returns:
        list[str]: líneas justificadas con longitud exactamente `max_width`.
    """
    res = []
    n = len(words)
    i = 0
    while i < n:
        # Agrupar palabras en la línea actual
        line_words = [words[i]]
        line_len = len(words[i])
        i += 1
        while i < n and line_len + 1 + len(words[i]) <= max_width:
            line_len += 1 + len(words[i])
            line_words.append(words[i])
            i += 1

        # Si es la última línea o solo hay una palabra, left-justify
        if i == n or len(line_words) == 1:
            line = ' '.join(line_words)
            line += ' ' * (max_width - len(line))
        else:
            total_spaces = max_width - sum(len(w) for w in line_words)
            gaps = len(line_words) - 1
            base_space = total_spaces // gaps
            extra = total_spaces % gaps
            parts = []
            for idx, w in enumerate(line_words):
                parts.append(w)
                if idx < gaps:
                    # distribuir un espacio adicional a los primeros `extra` huecos
                    spaces = base_space + (1 if idx < extra else 0)
                    parts.append(' ' * spaces)
            line = ''.join(parts)

        res.append(line)

    return res


if __name__ == '__main__':
    sample = "This is an example of text justification.".split()
    for l in justify_text(sample, 16):
        print(repr(l))



#Ejercicio 5

from sistema_transacciones import process_transaction_batches # type: ignore

def test_transfer_and_fee():
    balances = {"A": 200.0, "B": 20.0}
    blocks = [
        [("transfer", "A", "B", 50.0), ("fee", "B", 5.0)],
    ]
    result = process_transaction_batches(balances, blocks)
    assert abs(result["A"] - 150.0) < 1e-6
    assert abs(result["B"] - 65.0) < 1e-6


def test_fee_causes_rollback():
    balances = {"A": 100.0}
    blocks = [
        [("deposit", "A", 10.0)],
        [("fee", "A", 200.0)],  # falla -> rollback del bloque
        [("withdraw", "A", 50.0)],
    ]
    result = process_transaction_batches(balances, blocks)
    assert abs(result["A"] - 60.0) < 1e-6


def test_set_balance_and_unknown_op_rollback():
    balances = {"X": 0.0}
    blocks = [
        [("set", "X", 500.0)],
        [("noop", "X")],  # operación desconocida -> rollback
        [("fee", "X", 10.0)],
    ]
    result = process_transaction_batches(balances, blocks)
    assert abs(result["X"] - 490.0) < 1e-6


if __name__ == "__main__":
    tests = [
        test_transfer_and_fee,
        test_fee_causes_rollback,
        test_set_balance_and_unknown_op_rollback,
    ]
    for t in tests:
        print('Running', t.__name__)
        t()
    print('All manual tests passed.')


# Ejercicio 6

def resolver_dependencias(paquetes):
    """Devuelve un orden de instalación para paquetes y dependencias.

    Parámetros:
    - paquetes: dict donde la clave es el paquete y el valor es la lista de dependencias.

    Retorna:
    - lista con el orden de instalación o un mensaje de error si hay un ciclo.
    """
    dependencias = {paquete: list(deps) for paquete, deps in paquetes.items()}
    for deps in paquetes.values():
        for dep in deps:
            dependencias.setdefault(dep, [])

    orden = []

    while True:
        liberados = [pkg for pkg, deps in dependencias.items() if not deps and pkg not in orden]
        if not liberados:
            break

        while liberados:
            paquete_actual = liberados.pop(0)
            if paquete_actual in orden:
                continue
            orden.append(paquete_actual)

            for otro_paquete, deps in dependencias.items():
                if paquete_actual in deps:
                    deps.remove(paquete_actual)

        # detectar si aún quedan paquetes con dependencias no resueltas
        if all(deps == [] or pkg in orden for pkg, deps in dependencias.items()):
            continue

    if len(orden) != len(dependencias):
        return "Error: Deadlock detectado por dependencias circulares."

    return orden

# Ejercicio 7

def optimizador_carga(peso_max, articulos):
    """Resuelve el problema de la mochila con memoización.

    Parámetros:
    - peso_max: capacidad máxima de peso.
    - articulos: lista de tuplas (id, peso, valor).

    Retorna:
    - tupla (valor_max, [ids_seleccionados]).
    """
    memo = {}

    def _resolver(indice, capacidad):
        if indice >= len(articulos) or capacidad <= 0:
            return 0, ()

        clave = (indice, capacidad)
        if clave in memo:
            return memo[clave]

        id_articulo, peso, valor = articulos[indice]
        valor_sin, ids_sin = _resolver(indice + 1, capacidad)
        mejor = (valor_sin, ids_sin)

        if peso <= capacidad:
            valor_con, ids_con = _resolver(indice + 1, capacidad - peso)
            valor_con += valor
            if valor_con > valor_sin:
                mejor = (valor_con, ids_con + (id_articulo,))

        memo[clave] = mejor
        return mejor

    valor_max, ids_seleccionados = _resolver(0, peso_max)
    return valor_max, list(ids_seleccionados)


if __name__ == "__main__":
    carga_ejemplo = [
        (1, 3, 40),
        (2, 4, 50),
        (3, 5, 70),
        (4, 2, 30),
    ]
    print(optimizador_carga(7, carga_ejemplo))

# Ejercicio 8

def emparejar_orden(order_book, nueva_orden):
    """Cruza una orden nueva contra un libro de órdenes.

    Parámetros:
    - order_book: dict {'COMPRA': [ordenes], 'VENTA': [ordenes]}.
      Cada orden es un dict con al menos 'precio' y 'cantidad'.
    - nueva_orden: dict con 'lado' ('COMPRA' o 'VENTA'), 'precio' y 'cantidad'.

    Retorna:
    - lista_transacciones_ejecutadas: lista de dicts con ejecuciones.
    - order_book_actualizado: libro de órdenes con la orden restante insertada si no se completó.
    """
    lado = nueva_orden.get("lado", "").upper()
    if lado not in {"COMPRA", "VENTA"}:
        raise ValueError("La nueva orden debe tener lado 'COMPRA' o 'VENTA'.")

    cantidad_restante = int(nueva_orden.get("cantidad", 0))
    precio_nuevo = float(nueva_orden.get("precio", 0))
    if cantidad_restante <= 0 or precio_nuevo <= 0:
        raise ValueError("La orden debe tener precio y cantidad mayores a cero.")

    libro = {
        "COMPRA": [dict(o) for o in order_book.get("COMPRA", [])],
        "VENTA": [dict(o) for o in order_book.get("VENTA", [])],
    }

    def ordenar_lado(lado_libro):
        return sorted(
            libro[lado_libro],
            key=(lambda o: (-o["precio"],) if lado_libro == "COMPRA" else (o["precio"],)),
        )

    libro["COMPRA"] = ordenar_lado("COMPRA")
    libro["VENTA"] = ordenar_lado("VENTA")

    lado_contrario = "VENTA" if lado == "COMPRA" else "COMPRA"
    transacciones = []

    while cantidad_restante > 0 and libro[lado_contrario]:
        orden_contraria = libro[lado_contrario][0]
        precio_contrario = float(orden_contraria["precio"])

        if lado == "COMPRA" and precio_nuevo < precio_contrario:
            break
        if lado == "VENTA" and precio_nuevo > precio_contrario:
            break

        cantidad_ejecutada = min(cantidad_restante, int(orden_contraria["cantidad"]))
        transacciones.append({
            "lado_iniciador": lado,
            "precio_ejecucion": precio_contrario,
            "cantidad": cantidad_ejecutada,
            "orden_contraria": orden_contraria.get("id"),
        })

        cantidad_restante -= cantidad_ejecutada
        orden_contraria["cantidad"] -= cantidad_ejecutada

        if orden_contraria["cantidad"] <= 0:
            libro[lado_contrario].pop(0)

    if cantidad_restante > 0:
        orden_restante = {
            "lado": lado,
            "precio": precio_nuevo,
            "cantidad": cantidad_restante,
        }
        if "id" in nueva_orden:
            orden_restante["id"] = nueva_orden["id"]
        libro[lado].append(orden_restante)
        libro[lado] = ordenar_lado(lado)

    return transacciones, libro


if __name__ == "__main__":
    libro_ejemplo = {
        "COMPRA": [
            {"id": "b1", "precio": 98, "cantidad": 3},
            {"id": "b2", "precio": 95, "cantidad": 5},
        ],
        "VENTA": [
            {"id": "s1", "precio": 100, "cantidad": 2},
            {"id": "s2", "precio": 102, "cantidad": 4},
        ],
    }
    orden_nueva = {"id": "m1", "lado": "COMPRA", "precio": 101, "cantidad": 4}
    transacciones, libro_actualizado = emparejar_orden(libro_ejemplo, orden_nueva)
    print(transacciones)
    print(libro_actualizado)

#Ejercicio 9

def aplanar_diccionario(diccionario):
    """Aplana un diccionario complejo a un diccionario de un solo nivel.

    Parámetros:
    - diccionario: entrada que puede contener dicts y listas anidadas.

    Retorna:
    - dict con claves concatenadas por punto y valores escalares.
    """
    resultado = {}
    pila = [(diccionario, "")]

    while pila:
        actual, prefijo = pila.pop()

        if isinstance(actual, dict):
            if not actual and prefijo:
                resultado[prefijo] = {}
                continue
            for clave, valor in actual.items():
                nueva_clave = f"{prefijo}.{clave}" if prefijo else clave
                pila.append((valor, nueva_clave))

        elif isinstance(actual, list):
            if not actual and prefijo:
                resultado[prefijo] = []
                continue
            for indice, valor in enumerate(actual):
                nueva_clave = f"{prefijo}.{indice}" if prefijo else str(indice)
                pila.append((valor, nueva_clave))

        else:
            resultado[prefijo] = actual

    return dict(sorted(resultado.items()))


if __name__ == "__main__":
    ejemplo_json = {
        "empresa": {
            "ventas": [
                {"producto": "A", "monto": 150},
                {"producto": "B", "monto": 200}
            ],
            "ubicacion": {"pais": "AR", "ciudad": "BsAs"}
        },
        "fecha": "2026-06-02",
        "meta": [1, 2, {"submeta": 3}]
    }

    print(aplanar_diccionario(ejemplo_json))

#Ejercicio 10

def construir_arbol_huffman(frecuencias):
    """Construye la jerarquía binaria del árbol de Huffman.

    Parámetros:
    - frecuencias: dict {caracter: frecuencia}.

    Retorna:
    - tupla del árbol de Huffman en forma (peso, nodo), donde nodo es el carácter o una tupla anidada.
    """
    nodos = [(frecuencia, caracter) for caracter, frecuencia in frecuencias.items()]

    while len(nodos) > 1:
        nodos = sorted(nodos, key=lambda item: item[0])
        menor1 = nodos.pop(0)
        menor2 = nodos.pop(0)
        nuevo_nodo = (menor1[0] + menor2[0], (menor1, menor2))
        nodos.append(nuevo_nodo)

    return nodos[0] if nodos else None


if __name__ == "__main__":
    frecuencias_ejemplo = {
        "a": 5,
        "b": 9,
        "c": 12,
        "d": 13,
        "e": 16,
        "f": 45,
    }
    print(construir_arbol_huffman(frecuencias_ejemplo))

