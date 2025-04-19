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