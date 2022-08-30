from jugadorhumano import JugadorHumano
from jugadorhumanorandom import JugadorHumanoRandom
from jugadormaquina import JugadorMaquina
from tablero import Tablero

class Juego:

    def __init__(self):
        self.jugadores = [
            JugadorHumanoRandom("Alice", self),
            JugadorMaquina("Bob", self)
        ]
        self.tableros = [
            Tablero() for _ in range(2)
        ]
        self.turno = 0

    def iniciarPartida(self):
        # 1. Colocación de barcos
        for i in range(2):
            self.jugadores[i].colocarBarcos(
                self.tableros[i])
        # 2. Bucle del juego
        while self.quedanBarcos():
            print("Tu tablero:")
            self.tableros[0].dibujar(False)
            print("Tablero contrincante:")
            self.tableros[1].dibujar(True)
            while True:
                try:
                    x,y = self.jugadores[self.turno].jugar()
                    self.disparar(fila=y,columna=x)
                    break
                except Exception as error:
                    print(error)
            self.turno = 1 - self.turno
        # 3. Proclamar vencedor
        print("Vencedor: ", self.vencedor())


    def quedanBarcos(self):
        return len(list(self.tableros[0].hundidos())) < 5 \
            and len(list(self.tableros[1].hundidos())) < 5


    def disparar(self, fila, columna):
        self.tableros[1-self.turno].recibirDisparo(fila, columna)

    def vencedor(self):
        for j in range(2):
            if len(list(self.tableros[j].hundidos()))<5:
                return self.jugadores[j]

if __name__ == '__main__':
    g = Juego()
    g.iniciarPartida()