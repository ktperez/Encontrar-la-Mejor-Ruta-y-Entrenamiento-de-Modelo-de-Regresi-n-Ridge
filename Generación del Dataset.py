
from queue import PriorityQueue

# Paso 1: Base de Conocimiento en Reglas Lógicas
base_conocimiento = {
    "conexion": [
        ("A", "B", 5),
        ("A", "C", 3),
        ("B", "C", 1),
        ("B", "D", 4),
        ("C", "D", 2),
        ("C", "E", 6),
        ("D", "E", 3)
    ]
}

# Paso 2: Función para Encontrar la Mejor Ruta
def encontrar_mejor_ruta(base_conocimiento, inicio, final):
    # Creamos una cola de prioridad para explorar las rutas
    cola_prioridad = PriorityQueue()
    cola_prioridad.put((0, inicio, []))  # (costo acumulado, nodo actual, ruta hasta el nodo)

    visitados = set()

    while not cola_prioridad.empty():
        (costo_acumulado, nodo_actual, ruta) = cola_prioridad.get()

        # Si el nodo actual no ha sido visitado
        if nodo_actual not in visitados:
            ruta.append(nodo_actual)
            visitados.add(nodo_actual)

            # Si llegamos al nodo final, retornamos la ruta y el costo acumulado
            if nodo_actual == final:
                return ruta, costo_acumulado

            # Exploramos las conexiones desde el nodo actual
            for conexion in base_conocimiento["conexion"]:
                if conexion[0] == nodo_actual:
                    costo, siguiente_nodo = conexion[2], conexion[1]
                    nueva_ruta = list(ruta)
                    nueva_costo_acumulado = costo_acumulado + costo
                    cola_prioridad.put((nueva_costo_acumulado, siguiente_nodo, nueva_ruta))

    # Si no se encuentra ruta, retornamos None
    return None, None

# Ejemplo de uso
ruta_optima, costo_total = encontrar_mejor_ruta(base_conocimiento, "A", "E")
print("Ruta óptima:", ruta_optima)
print("Costo total:", costo_total)

import pandas as pd

# Base de conocimiento en forma de reglas lógicas
base_conocimiento = {
    "conexion": [
        ("A", "B", 5),
        ("A", "C", 3),
        ("B", "C", 1),
        ("B", "D", 4),
        ("C", "D", 2),
        ("C", "E", 6),
        ("D", "E", 3)
    ]
}

# Crear un DataFrame a partir de la base de conocimiento
data = []
for conexion in base_conocimiento["conexion"]:
    origen, destino, costo = conexion
    data.append([origen, destino, costo])

df = pd.DataFrame(data, columns=["Origen", "Destino", "Costo"])

# Guardar el DataFrame como un archivo CSV
df.to_csv("transporte_dataset.csv", index=False)
