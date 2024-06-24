class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha
        self.victorias = 0  # Inicializar el contador de victorias en 0

    def incrementar_victoria(self):
        self.victorias += 1
