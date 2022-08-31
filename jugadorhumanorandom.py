from jugadorhumano import JugadorHumano
from jugadormaquina import JugadorMaquina

class JugadorHumanoRandom(JugadorMaquina,JugadorHumano):

    def colocarBarcos(self, tablero):
        return JugadorMaquina.colocarBarcos(self, tablero)

    def jugar(self):
        return JugadorHumano.jugar(self)
