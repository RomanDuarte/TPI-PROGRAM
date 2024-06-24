class Piezas:
    def __init__(self, color):
        self.color = color #piezas que rellenan el tablero

    def __str__(self):
        return self.color

def elegir_ficha_jugador(nombre_jugador): #funcion para fichas
    while True:
        ficha = input(f"{nombre_jugador}, elige tu ficha (X o O): ").upper()
        if ficha in ['X', 'O']:
            return ficha
        else:
            print("Por favor, elige una ficha válida (X o O).")
