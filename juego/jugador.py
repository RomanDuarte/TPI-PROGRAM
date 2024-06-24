class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre #nombre ingresado por el usuario
        self.ficha = ficha #ficha elejida por el usuario
        self.victorias = 0  # Inicializar el contador de victorias en 0

    def incrementar_victoria(self):
        self.victorias += 1 #funcion que suma una victoria en caso de ganarla
