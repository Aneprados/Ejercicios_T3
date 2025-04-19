class PiramideDePiedras:

    def resolver(self):
        """
        Inicia el proceso de resolver el problema de la pirámide de piedras.
        """
        print("Iniciando el traslado de piedras...")
        self.mover_piedras(self.numero_de_piedras, "Columna A", "Columna C", "Columna B")
        print("¡Traslado completado! ¿Dónde está el tesoro?")


# Número de piedras en la pirámide
numero_de_piedras = 74

# Crear una instancia de la clase y resolver el problema
piramide = PiramideDePiedras(numero_de_piedras)
piramide.resolver()