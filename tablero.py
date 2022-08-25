from barco import Barco


class Tablero:

    def __init__(self) -> None:
        self.posicionesBarcos = []
        self.disparos = []

    def posicionarBarco(self, barco):
        self.posicionesBarcos.append(barco)
        #TODO: comprobar solapamiento

    def recibirDisparo(self, fila, columna):
        if (fila, columna) in self.disparos:
            raise ValueError("Disparo repetido")
        self.disparos.append((fila, columna))

    def hundidos(self):
        pass

    def dibujar(self, ocultarBarcos):
        t = [[' ' for x in range(10)] for y in range(10)]
        if not ocultarBarcos:
            for b in self.posicionesBarcos:
                b.dibujar(t)
        for d in self.disparos:
            fila, columna = d
            t[fila][columna] = 'x' if t[fila][columna]!=' ' else 'o'
        s = "+---" * 10 + "+\n"
        for y in range(10):
            for x in range(10):
                s += f"| {t[x][y]} "
            s += "|\n" + ("+---" * 10) + "+\n"
        print(s)

if __name__ == '__main__':
    t = Tablero()
    b1 = Barco(2, 3, 4, Barco.HORIZONTAL)
    b2 = Barco(5, 8, 2, Barco.VERTICAL)
    t.posicionarBarco(b1)
    t.posicionarBarco(b2)
    t.recibirDisparo(2, 5)
    t.recibirDisparo(5, 2)
    t.dibujar(ocultarBarcos=False)