# Buscador de Rutas Logísticas (BFS)

Algoritmo en Python que encuentra la ruta más corta entre dos puntos de una red logística, evitando nodos bloqueados (por ejemplo: una vía cerrada, un almacén fuera de servicio).

## El problema

Dada una red de puntos conectados entre sí, ¿cuál es el camino más corto desde un origen hasta un destino si algunos puntos intermedios no se pueden usar?

## La solución

Implementación de **búsqueda en anchura (BFS)** sobre un grafo representado como diccionario de listas de adyacencia.

- Cola de exploración por niveles → garantiza que la primera ruta encontrada es la más corta en número de saltos.
- Conjunto de nodos visitados → evita ciclos infinitos.
- Diccionario de padres → permite reconstruir la ruta completa hacia atrás una vez alcanzado el destino.
- Los nodos bloqueados se descartan antes de entrar en la cola.

**Complejidad:** O(V + E), donde V son los nodos y E las conexiones.

## Casos borde cubiertos

| Situación | Resultado |
|---|---|
| El origen o el destino está bloqueado | Devuelve lista vacía |
| El origen o el destino no existe en el grafo | Devuelve lista vacía |
| No existe ningún camino posible | Devuelve lista vacía |

En ningún caso el programa lanza una excepción: siempre devuelve un resultado controlado.

## Cómo ejecutarlo

```bash
python trabajo_con_ia.py
```

Requiere Python 3. Sin dependencias externas.

## Ejemplo de uso

```python
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

ruta = encontrar_ruta_logistica(grafo, "A", "E", bloqueados=["B"])
# -> ['A', 'C', 'D', 'E']
```

## Qué aprendí

Cómo representar un grafo con diccionarios, la diferencia entre recorrer en anchura y en profundidad, y por qué BFS es el algoritmo correcto cuando lo que se busca es el camino **más corto** y no simplemente *un* camino.

## Tecnologías

`Python 3` · `Estructuras de datos` · `Algoritmos de grafos` · `BFS`

---
Andrés Barros · Estudiante de Ingeniería de Sistemas
