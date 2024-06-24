from jugador import Jugador
from Piesas import elegir_ficha_jugador
from tres_en_raya import TresEnRaya
from datos import diccionario

def main():
    print("        INICIA LA PARTIDA         ")
    print("----------------------------------")


    # Jugador 1 elige su ficha
    ficha_jugador1 = elegir_ficha_jugador("Jugador 1")
    jugador1 = Jugador(input("Introduce el nombre del jugador 1: "), ficha_jugador1)

    # Jugador 2 elige su ficha
    ficha_jugador2 = 'X' if ficha_jugador1 == 'O' else 'O'
    jugador2 = Jugador(input("Introduce el nombre del jugador 2: "), ficha_jugador2)

    # Crear un objeto TresEnRaya con los jugadores creados
    juego = TresEnRaya(jugador1, jugador2)
    
    # Empezar el juego
    juego.empezar_juego()

if __name__ == "__main__":
    main()
