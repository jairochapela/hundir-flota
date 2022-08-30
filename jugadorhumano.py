from jugador import Jugador
from barco import Barco

class JugadorHumano(Jugador):
    def __init__(self, nombre, partida):
        super().__init__(nombre, partida)

    def colocarBarcos(self, tablero):
        for s in [5, 4, 3, 3, 2]:
            while True:
                try:
                    print("Coloque barco de tamaño", s)
                    fila = int(input("Fila>"))
                    columna = int(input("Columna>"))
                    orientacion = input("Orientación(H|V)>").upper()
                    if orientacion=='H':
                        barco = Barco(fila, columna, s, Barco.HORIZONTAL)
                    elif orientacion=='V':
                        barco = Barco(fila, columna, s, Barco.VERTICAL)
                    else:
                        raise ValueError("Orientación no válida")
                    tablero.posicionarBarco(barco)
                    break
                except Exception as error:
                    print(error)
    
    def jugar(self):
        fila = int(input("Fila> "))
        columna = int(input("Columna> "))
        return fila, columna
