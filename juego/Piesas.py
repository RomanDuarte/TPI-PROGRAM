class Piece:
    def __init__(self, color):
        """
        Inicializa una pieza con un color ('X' o 'O').

        Parámetros:
        color (str): El color de la pieza, debe ser 'X' o 'O'.
        """
        self.color = color

    def __str__(self):
        """Devuelve la representación en cadena de la pieza."""
        return self.color

def elegir_ficha_jugador(nombre_jugador):
    """
    Permite al jugador elegir su ficha ('X' o 'O') y devuelve la ficha elegida.

    Parámetros:
    nombre_jugador (str): El nombre del jugador para el que se elige la ficha.
    """
    while True:
        ficha = input(f"{nombre_jugador}, elige tu ficha (X o O): ").upper()
        if ficha in ['X', 'O']:
            return ficha
        else:
            print("Por favor, elige una ficha válida (X o O).")
