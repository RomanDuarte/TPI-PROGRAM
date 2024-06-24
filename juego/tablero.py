from Piezas import Piezas

class Tablero:
    def __init__(self): #funcion del tamaño y casillas
        self.filas = 3
        self.columnas = 3
        self.tablero = [[Piezas("") for _ in range(self.columnas)] for _ in range(self.filas)]

    def mostrar(self): # es el cuerpo el tablero y lo muestra en pantalla
        for fila in self.tablero:
            print("|" + "|".join(str(Piezas).center(3) for Piezas in fila) + "|")
            print("-" * (4 * self.columnas + 1))

    def agregar_ficha(self, ficha, fila, columna): #pone la ficha al tablero
        if self.tablero[fila][columna].color == '':
            self.tablero[fila][columna] = Piezas(ficha)
            return True
        else:
            return False

    def esta_lleno(self): #evalua si la casilla esta ocupada
        for fila in self.tablero:
            for casilla in fila:
                if casilla.color == '':
                    return False
        return True
