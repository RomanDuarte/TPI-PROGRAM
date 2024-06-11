class Jugador:
    def __init__(self, nombre, ficha):
        if nombre.strip() == "":
            raise ValueError("El nombre del jugador no puede estar vacío.")
        self.nombre = nombre
        if ficha not in ["X", "O"]:
            raise ValueError("La ficha del jugador debe ser 'X' o 'O'.")
        self.ficha = ficha
