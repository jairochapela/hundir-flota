
class Jugador:
    '''
    Clase abstracta de jugador.
    Simplemente representa un jugador que no tiene
    definido comportamiento alguno.
    '''
    def __init__(self, nombre, partida):
        self.nombre = nombre
        self.partida = partida
    
    def colocarBarcos(self, tablero):
        pass

    def jugar(self, columna, fila):
        pass

    def __str__(self):
        return self.nombre