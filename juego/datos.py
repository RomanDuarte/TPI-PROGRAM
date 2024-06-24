from jugador import Jugador

# Datos precargados para los jugadores

# jugador1 = Jugador( "", "X")
# jugador2 = Jugador( "", "O")


diccionario = {"Juan" : 20, "Lucas" : 12, "Sofia" : 2, "Roberto" : 7, "Pedro" : 5, "Fede" : 7, "Delfina" : 6, "Paula" : 4}

diccionario_ordenado = sorted(diccionario.items(), key=lambda item: item[1], reverse=True)

print("----------------------------------")
print("      RANKING MAS VICTORIAS       ")
print("----------------------------------")
for clave, valor in diccionario_ordenado:
    print(f"{clave} = {valor}")
print("----------------------------------")
print()
