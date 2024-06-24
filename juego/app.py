from jugador import Jugador
from Piezas import elegir_ficha_jugador
from tres_en_raya import TresEnRaya
from datos import diccionario

def mostrar_menu():
    

    while True:
        print("\n-------- MENÚ --------")
        print("1. Empezar partida")
        print("2. Mostrar ranking")
        print("3. Salir")
        print("----------------------")
        
        opcion = input("Elige una opción (1-3): ")
        if opcion == "1":
            empezar_partida()
        elif opcion == "2":
            mostrar_ranking()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 3.")

def empezar_partida():
    print("\n-------- INICIA LA PARTIDA --------")
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
    
def mostrar_ranking():
    # Ordenar el diccionario de jugadores por número de victorias de mayor a menor
    diccionario_ordenado = sorted(diccionario.items(), key=lambda item: item[1], reverse=True)

    print("\n-------- RANKING DE JUGADORES --------")
    for nombre, victorias in diccionario_ordenado:
        print(f"{nombre}: {victorias} victorias")
    print("--------------------------------------")

def main():
    mostrar_menu()

if __name__ == "__main__":
    main()
