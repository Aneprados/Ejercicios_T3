import sys  # Importar el módulo sys
from TorreDeHanoi import TorreDeHanoi

class Lanzador:
    def ejecutar(self):
        sys.setrecursionlimit(2000)  # Aumentar el límite de recursión
        num_piedras = 20  # Reducir el número de piedras a un nivel manejable
        juego = TorreDeHanoi(num_piedras)
        print("Estado inicial:")
        juego.mostrar_estado()
        print("\nResolviendo...\n")
        juego.resolver()
        print("\nEstado final:")
        juego.mostrar_estado()