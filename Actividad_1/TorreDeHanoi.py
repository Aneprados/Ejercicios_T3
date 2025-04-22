from Columna import Columna
from Piedra import Piedra

class TorreDeHanoi:
    def __init__(self, num_piedras):
        self.num_piedras = num_piedras
        self.columna_origen = Columna("Origen")
        self.columna_auxiliar = Columna("Auxiliar")
        self.columna_destino = Columna("Destino")
        self._inicializar_piedras()

    def _inicializar_piedras(self):
        for tamaño in range(self.num_piedras, 0, -1):
            self.columna_origen.apilar(Piedra(tamaño))

    def resolver(self):
        self._mover_piedras(self.num_piedras, self.columna_origen, self.columna_destino, self.columna_auxiliar)

    def _mover_piedras(self, n, origen, destino, auxiliar):
        if n == 1:
            piedra = origen.desapilar()
            destino.apilar(piedra)
            print(f"Mover {piedra} de {origen.nombre} a {destino.nombre}")
        else:
            self._mover_piedras(n - 1, origen, auxiliar, destino)
            self._mover_piedras(1, origen, destino, auxiliar)
            self._mover_piedras(n - 1, auxiliar, destino, origen)

    def mostrar_estado(self):
        print(self.columna_origen)
        print(self.columna_auxiliar)
        print(self.columna_destino)
