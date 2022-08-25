from fileinput import filename
from tkinter import HORIZONTAL, VERTICAL


class Barco:

    HORIZONTAL = (1,0)
    VERTICAL = (0,1)

    def __init__(self, fila, columna, longitud, orientacion) -> None:
        self.fila = fila
        self.columna = columna
        self.longitud = longitud
        self.orientacion = orientacion
    

    def impactos(self, disparos):
        v = self.orientacion
        celdas = [(self.columna + v[0]*k, self.fila + v[1]*k) for k in range(self.longitud)]
        return [d in celdas for d in disparos]

    def hundido(self):
        return all(self.impactos())

    def dibujar(self, t):
        v = self.orientacion
        for k in range(self.longitud):
            x, y = self.columna + v[0]*k, self.fila + v[1]*k
            t[x][y] = '@'



