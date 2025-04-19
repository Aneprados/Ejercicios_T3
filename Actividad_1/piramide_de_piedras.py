class PiramideDePiedras:
    def __init__(self, numero_de_piedras):
        """
        Inicializa la pirámide con el número de piedras.
        
        :param numero_de_piedras: Número total de piedras en la pirámide.
        """
        self.numero_de_piedras = numero_de_piedras

    def mover_piedras(self, n, origen, destino, auxiliar):
        """
        Resuelve el problema de mover n piedras de una columna a otra siguiendo las reglas.
        
        :param n: Número de piedras a mover.
        :param origen: Nombre de la columna origen.
        :param destino: Nombre de la columna destino.
        :param auxiliar: Nombre de la columna auxiliar.
        """
        if n == 1:
            print(f"Mueve la piedra de {origen} a {destino}")
            return
        # Mueve n-1 piedras de la columna origen a la columna auxiliar
        self.mover_piedras(n - 1, origen, auxiliar, destino)
        # Mueve la piedra más grande de la columna origen a la columna destino
        print(f"Mueve la piedra de {origen} a {destino}")
        # Mueve las n-1 piedras de la columna auxiliar a la columna destino
        self.mover_piedras(n - 1, auxiliar, destino, origen)

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