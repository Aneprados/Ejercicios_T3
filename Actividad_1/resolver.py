def resolver(self):
    """
    Inicia el proceso de resolver el problema de la pirámide de piedras.
    """
    print("Iniciando el traslado de piedras...")
    self.mover_piedras(self.numero_de_piedras, origen="Columna A", destino="Columna C", auxiliar="Columna B")
    print("¡Traslado completado! ¿Dónde está el tesoro?")
