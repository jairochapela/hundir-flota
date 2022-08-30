
import random
from barco import Barco
from jugador import Jugador


class JugadorMaquina(Jugador):
    def __init__(self, nombre, partida):
        super().__init__(nombre, partida)

    def colocarBarcos(self, tablero):
        for s in [5, 4, 3, 3, 2]:
            while True:
                try:
                    fila = random.randrange(10)
                    columna = random.randrange(10)
                    orientacion = random.choice(['H', 'V'])
                    if orientacion=='H':
                        barco = Barco(fila, columna, s, Barco.HORIZONTAL)
                    elif orientacion=='V':
                        barco = Barco(fila, columna, s, Barco.VERTICAL)
                    else:
                        raise ValueError("Orientación no válida")
                    tablero.posicionarBarco(barco)
                    break
                except Exception:
                    pass

    def jugar(self):
        fila = random.randrange(10)
        columna = random.randrange(10)
        return fila, columna
        