from multiprocessing.sharedctypes import Value


def convertir_coordenadas(spec):
    letras = "ABCDEFGHIJ"
    r = spec.lstrip().upper()
    try:
        fila = letras.index(r[0])
    except ValueError as err:
        raise ValueError(f"Fila no reconocida: {err}")
    columna = int(r[1:]) - 1
    return fila, columna
