class Jugador:
    def __init__(self, nombre, ficha):
        """
        Inicializa un jugador con un nombre y una ficha ('X' o 'O').

        Parámetros:
        nombre (str): El nombre del jugador.
        ficha (str): La ficha del jugador, debe ser 'X' o 'O'.
        
        Excepciones:
        ValueError: Si el nombre está vacío o la ficha no es 'X' o 'O'.
        """
        while True:
            if not nombre.strip():
                nombre = input("El nombre del jugador no puede estar vacío. Introduce un nombre: ").strip()
            else:
                break
        self.nombre = nombre

        if ficha not in ["X", "O"]:
            raise ValueError("La ficha del jugador debe ser 'X' o 'O'.")
        self.ficha = ficha
