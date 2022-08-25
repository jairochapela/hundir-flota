class Barco:

    # Estas constantes definen el avance de
    # las casillas a ocupar por un barco según
    # su orientación: horizontal, vertical.
    HORIZONTAL = (1,0)
    VERTICAL = (0,1)

    def __init__(self, fila, columna, longitud, orientacion):

        horz,vert = orientacion

        if fila not in range(0, 10-vert*longitud) or columna not in range(0, 10-horz*longitud):
            raise ValueError("Posicion no válida")

        self.fila = fila
        self.columna = columna
        self.longitud = longitud
        self.orientacion = orientacion
    
    # Cálculo de los impactos en el barco, dada
    # la secuencia de disparos.
    def impactos(self, disparos):
        horz,vert = self.orientacion
        celdas = [(self.columna + horz*k, self.fila + vert*k) 
            for k in range(self.longitud)]
        return [c in disparos for c in celdas]

    # Un barco está hundido si todas sus posiciones
    # fueron tocadas
    def hundido(self, disparos):
        return all(self.impactos(disparos))

    def dibujar(self, t, disparos):
        pass






if __name__ == '__main__':
    b1 = Barco(fila=3, columna=5, longitud=4, orientacion=Barco.HORIZONTAL)
    b2 = Barco(0, 2, 3, Barco.VERTICAL)
    print(b1)
    disparos = [(1,2), (4,5), (8,3)]
    print(b1.impactos(disparos))
    print(b1.hundido(disparos))