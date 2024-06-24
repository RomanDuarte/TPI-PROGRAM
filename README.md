Integrantes:

Duarte Sergio - 53356

Fux Mateo     - 53351

Gil Felipe    - 53336


TUP6

Año: 2024

Programacion 2

Realizamos un juego clasico como lo es el 3 en raya, o ta te ti. Con un ranking o sistema de puntuacion donde se registran las partidas ganadas por los usuarios. 

--------------------------------
|          TresEnRaya          |
--------------------------------
| - tablero: Tablero           |
| - jugador1: Jugador          |
| - jugador2: Jugador          |
| - jugador_actual: Jugador    |
--------------------------------
| + __init__(jugador1, jugador2)|
| + empezar_juego(): void      |
| + obtener_posicion(): tuple  |
| + cambiar_jugador(): void    |
| + verificar_ganador(ficha): bool |
| + mostrar_ranking(): void    |
| + volver_a_jugar(): bool     |
--------------------------------

--------------------------------
|           Jugador            |
--------------------------------
| - nombre: str                |
| - ficha: str                 |
| - victorias: int             |
--------------------------------
| + __init__(nombre, ficha)    |
| + incrementar_victoria(): void |
--------------------------------

--------------------------------
|           Tablero            |
--------------------------------
| - tablero: list              |
--------------------------------
| + __init__()                 |
| + mostrar(): void            |
| + agregar_ficha(ficha, fila, columna): bool |
| + esta_lleno(): bool         |
--------------------------------

Link: https://github.com/RomanDuarte/TPI-PROGRAM
