from Piesas import Piece

class Tablero:
    def __init__(self):
        self.filas = 3
        self.columnas = 3
        self.tablero = [[Piece("") for _ in range(self.columnas)] for _ in range(self.filas)]

    def mostrar(self):
        for fila in self.tablero:
            print("|" + "|".join(str(piece).center(3) for piece in fila) + "|")
            print("-" * (4 * self.columnas + 1))

    def agregar_ficha(self, ficha, fila, columna):
        if self.tablero[fila][columna].color == '':
            self.tablero[fila][columna] = Piece(ficha)
            return True
        else:
            return False

    def esta_lleno(self):
        for fila in self.tablero:
            for casilla in fila:
                if casilla.color == '':
                    return False
        return True
