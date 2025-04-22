from Matriz import Matriz3x3
class Lanzador:
    def __init__(self):
        self.matriz = [
            [2, 4, 3],
            [1, 5, 7],
            [6, 8, 9]
        ]

    def ejecutar(self):
        matriz_obj = Matriz3x3(self.matriz)
        print("Determinante (recursivo):", matriz_obj.calcular_determinante_recursivo())
        print("Determinante (iterativo):", matriz_obj.calcular_determinante_iterativo())


