class Tablero:
    def __init__(self):
        """Inicializa el tablero con 3 filas y 3 columnas, lleno de espacios en blanco."""
        self.filas = 3
        self.columnas = 3
        self.tablero = [[' ' for _ in range(self.columnas)] for _ in range(self.filas)]

    def mostrar(self):
        """Muestra el tablero en la consola."""
        for fila in self.tablero:
            print("|" + "|".join(fila) + "|")
            print("-" * (2 * self.columnas + 1))

    def agregar_ficha(self, ficha, fila, columna):
        """
        Agrega una ficha en la posición especificada del tablero.
        Retorna True si se pudo agregar la ficha, False si la casilla está ocupada.
        """
        if self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = ficha
            return True
        else:
            return False

    def esta_lleno(self):
        """Verifica si el tablero está lleno, es decir, si no hay espacios en blanco."""
        for fila in self.tablero:
            if ' ' in fila:
                return False
        return True

    def verificar_ganador(self, ficha):
        """Verifica si hay un ganador en el tablero."""
        # Implementa la lógica para verificar si hay un ganador
        # Esto podría implicar revisar todas las filas, columnas y diagonales para ver si hay una línea completa del mismo símbolo (ficha)
        # Si hay un ganador, retorna True, de lo contrario, retorna False
        pass  # Aquí va tu implementación
