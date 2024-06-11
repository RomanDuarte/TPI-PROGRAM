from tablero import Tablero  # Importa la clase Tablero desde el archivo tablero.py

class TresEnRaya:
    def __init__(self, jugador1, jugador2):
        """
        Inicializa el juego con dos jugadores y un tablero.
        """
        if jugador1.ficha == jugador2.ficha:
            raise ValueError("Las fichas de los jugadores deben ser diferentes.")
        self.tablero = Tablero()  # Crea una instancia de la clase Tablero
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.jugador_actual = jugador1

    def empezar_juego(self):
        """
        Inicia el juego y maneja el flujo del mismo.
        """
        while True:
            self.tablero.mostrar()
            fila, columna = self.obtener_posicion()
            if self.tablero.agregar_ficha(self.jugador_actual.ficha, fila, columna):
                if self.verificar_ganador(self.jugador_actual.ficha):
                    self.tablero.mostrar()
                    print(f'{self.jugador_actual.nombre} gana!')
                    break
                if self.tablero.esta_lleno():
                    self.tablero.mostrar()
                    print('¡Empate!')
                    break
                self.cambiar_jugador()
            else:
                print('Casilla ocupada. Inténtalo de nuevo.')

    def obtener_posicion(self):
        """
        Pide al jugador actual que elija una posición en el tablero.
        """
        while True:
            try:
                fila = int(input(f'{self.jugador_actual.nombre}, elige una fila (0-2): '))
                columna = int(input(f'{self.jugador_actual.nombre}, elige una columna (0-2): '))
                if 0 <= fila <= 2 and 0 <= columna <= 2:
                    return fila, columna
                else:
                    print('Por favor, introduce valores válidos (0-2).')
            except ValueError:
                print('Por favor, introduce valores numéricos.')

    def cambiar_jugador(self):
        """Cambia al otro jugador."""
        self.jugador_actual = self.jugador2 if self.jugador_actual == self.jugador1 else self.jugador1

    def cambiar_jugador(self):
        """Cambia al otro jugador."""
        if self.jugador_actual == self.jugador1:
            self.jugador_actual = self.jugador2
        else:
            self.jugador_actual = self.jugador1

    def verificar_ganador(self, ficha):
        """
        Verifica si hay un ganador en el tablero.
        """
        tab = self.tablero.tablero

        # Verifica filas y columnas
        for i in range(3):
            if tab[i][0] == tab[i][1] == tab[i][2] == ficha or tab[0][i] == tab[1][i] == tab[2][i] == ficha:
                return True

        # Verifica diagonales
        if tab[0][0] == tab[1][1] == tab[2][2] == ficha or tab[0][2] == tab[1][1] == tab[2][0] == ficha:
            return True

        return False
