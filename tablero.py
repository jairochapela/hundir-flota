from barco import Barco


class Tablero:

    def __init__(self):
        self.posicionesBarcos = []
        self.disparos = []

    def posicionarBarco(self, barco):
        self.posicionesBarcos.append(barco)
        #TODO: comprobar solapamiento

    def recibirDisparo(self, fila, columna):
        if fila < 0 or fila >=10\
        or columna < 0 or columna >= 10:
            raise ValueError("Disparo fuera de rango")
  
        if (columna, fila) in self.disparos:
            raise ValueError("Disparo repetido")
        self.disparos.append((columna, fila))


    def hundidos(self):
        return filter(
            lambda b: b.hundido(self.disparos),
            self.posicionesBarcos)


    def dibujar(self, ocultarBarcos):
        # 1. Crear matriz de 10x10
        t = [[' ' for x in range(10)] for y in range(10)]
        # 2. Dibujar los disparos
        for disparo in self.disparos:
            x, y = disparo
            t[x][y] = '*'
        # 3. Colocar los barcos
        for barco in self.posicionesBarcos:
            barco.dibujar(t, self.disparos, ocultarBarcos)
        # 4. Imprimir tablero
        s = "+---" * 10 + "+\n"
        for y in range(10):
            for x in range(10):
                s += "| " + t[x][y] + " "
            s += "|\n"
            s += "+---" * 10 + "+\n"
        print(s)



if __name__ == '__main__':
    tab = Tablero()
    b1 = Barco(fila=2, columna=3, longitud=4, orientacion=Barco.HORIZONTAL)
    b2 = Barco(fila=5, columna=8, longitud=2, orientacion=Barco.VERTICAL)
    tab.posicionarBarco(b1)
    tab.posicionarBarco(b2)
    tab.recibirDisparo(2, 5)
    tab.recibirDisparo(5, 2)
    tab.dibujar(ocultarBarcos=True)