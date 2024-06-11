from jugador import Jugador
from tres_en_raya import TresEnRaya
import datos

def main():
    # Crear un objeto TresEnRaya con los jugadores precargados
    juego = TresEnRaya(datos.jugador1, datos.jugador2)
    
    # Empezar el juego
    juego.empezar_juego()

main()
