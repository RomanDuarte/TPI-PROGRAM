from jugador import Jugador
from tablero import Tablero
from datos import ranking

class TresEnRaya:
    def __init__(self, jugador1, jugador2):
        if jugador1.ficha == jugador2.ficha: #verifica que las fichas no sean las mismas
            raise ValueError("Las fichas de los jugadores deben ser diferentes.")
        self.tablero = Tablero()
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.jugador_actual = jugador1

    def empezar_juego(self):
        #agrega jugadores al diccionario con sus partidas ganadas
        ranking[self.jugador1.nombre] = self.jugador1.victorias 
        ranking[self.jugador2.nombre] = self.jugador2.victorias
        
        while True:
            self.tablero.mostrar()
            fila, columna = self.obtener_posicion()
            
            if self.tablero.agregar_ficha(self.jugador_actual.ficha, fila, columna):
                if self.verificar_ganador(self.jugador_actual.ficha):
                    self.tablero.mostrar()
                    print(f'{self.jugador_actual.nombre} gana!')
                    self.jugador_actual.incrementar_victoria()  # Incrementa el contador de victorias del jugador actual
                    ranking[self.jugador_actual.nombre] = self.jugador_actual.victorias
                    self.mostrar_ranking()  # Muestra el ranking actualizado
                    if self.volver_a_jugar():
                        self.tablero = Tablero()  # Reinicia el tablero
                        self.jugador_actual = self.jugador1  # Reinicia con jugador1
                        continue  # Vuelve al inicio del bucle para comenzar una nueva partida
                    else:
                        break  # Termina el juego si no se desea jugar otra partida
                if self.tablero.esta_lleno():
                    self.tablero.mostrar()
                    print('¡Empate!')
                    if self.volver_a_jugar():
                        self.tablero = Tablero()  # Reinicia el tablero
                        self.jugador_actual = self.jugador1  # Reinicia con jugador1
                        continue  # Vuelve al inicio del bucle para comenzar una nueva partida
                    else:
                        break  # Termina el juego si no se desea jugar otra partida
                
                self.cambiar_jugador()  # Cambia al siguiente jugador
            else:
                print('Casilla ocupada. Inténtalo de nuevo.')

    def obtener_posicion(self): #pide las coordenadas por teclado
        while True:
            fila_str = input(f'{self.jugador_actual.nombre}, elige una fila (1-3): ')
            columna_str = input(f'{self.jugador_actual.nombre}, elige una columna (1-3): ')
            
            if fila_str.isdigit() and columna_str.isdigit():
                fila = int(fila_str) - 1
                columna = int(columna_str) - 1
                if 0 <= fila <= 2 and 0 <= columna <= 2: #verifica que sean correctas
                    return fila, columna
                else:
                    print('Por favor, introduce valores válidos (1-3).')
            else:
                print('Por favor, introduce valores numéricos.')

    def cambiar_jugador(self): #despues que termina el turno cambia el jugador 
        if self.jugador_actual == self.jugador1:
            self.jugador_actual = self.jugador2
        else:
            self.jugador_actual = self.jugador1

    def verificar_ganador(self, ficha): #verifica si hay ganador tanto vertical, horizontal y diagonal 
        tab = self.tablero.tablero

        for i in range(3):
            if tab[i][0].color == tab[i][1].color == tab[i][2].color == ficha or tab[0][i].color == tab[1][i].color == tab[2][i].color == ficha:
                return True

        if tab[0][0].color == tab[1][1].color == tab[2][2].color == ficha or tab[0][2].color == tab[1][1].color == tab[2][0].color == ficha:
            return True

        return False
    
    def mostrar_ranking(self):
        # Ordenar el ranking de jugadores por número de victorias de mayor a menor
        ranking_ordenado = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
        print("\n-------- RANKING DE JUGADORES --------")
        for nombre, victorias in ranking_ordenado:
            print(f"{nombre}: {victorias} victorias")
        print("--------------------------------------")
    
    def volver_a_jugar(self):#pregunta al usuario en pantalla si quiere volver a jugar 
        while True:
            respuesta = input("¿Deseas jugar otra partida? (s/n): ").lower()
            if respuesta == 's':
                return True
            elif respuesta == 'n':
                return False
            else:
                print("Respuesta no válida. Por favor, responde 's' o 'n'.")

def main(): # al principio de la partida se da a elejir las fichas
    ficha_jugador1 = input("Jugador 1, elige tu ficha (X o O): ").upper()
    jugador1 = Jugador(input("Introduce el nombre del jugador 1: "), ficha_jugador1)

    ficha_jugador2 = 'X' if ficha_jugador1 == 'O' else 'O'
    jugador2 = Jugador(input("Introduce el nombre del jugador 2: "), ficha_jugador2)

    juego = TresEnRaya(jugador1, jugador2)
    juego.empezar_juego()

if __name__ == "__main__":
    main()
