def convertir_coordenadas(spec):
    letras = "ABCDEFGHIJ"
    r = spec.lstrip().upper()
    fila = letras.index(r[0])
    columna = int(r[1:]) - 1
    return fila, columna
