from Piesas import Piece

class Tablero:
    def __init__(self):
        """Inicializa el tablero con 3 filas y 3 columnas, lleno de piezas vacías."""
        self.filas = 3
        self.columnas = 3
        self.tablero = [[Piece("") for _ in range(self.columnas)] for _ in range(self.filas)]

    def mostrar(self):
        """Muestra el tablero en la consola."""
        for fila in self.tablero:
            print("|" + "|".join(str(piece).center(3) for piece in fila) + "|")
            print("-" * (4 * self.columnas + 1))

    def agregar_ficha(self, ficha, fila, columna):
        """
        Agrega una ficha en la posición especificada del tablero.
        Retorna True si se pudo agregar la ficha, False si la casilla está ocupada.
        """
        if self.tablero[fila][columna].color == '':
            self.tablero[fila][columna] = Piece(ficha)
            return True
        else:
            return False

    def esta_lleno(self):
        """Verifica si el tablero está lleno, es decir, si no hay espacios en blanco."""
        for fila in self.tablero:
            for casilla in fila:
                if casilla.color == '':
                    return False
        return True
