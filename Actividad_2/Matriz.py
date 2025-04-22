class Matriz3x3:
    def __init__(self, matriz):
        if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            raise ValueError("La matriz debe ser de 3x3.")
        self.matriz = matriz

    def calcular_determinante_recursivo(self):
        """
        Calcula el determinante de la matriz utilizando un método recursivo.
        """
        def determinante(matriz):
            if len(matriz) == 2:
                # Determinante de una matriz 2x2
                return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
            else:
                # Expansión por cofactores
                det = 0
                for i in range(len(matriz)):
                    submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
                    det += ((-1) ** i) * matriz[0][i] * determinante(submatriz)
                return det

        return determinante(self.matriz)

    def calcular_determinante_iterativo(self):
        """
        Calcula el determinante de la matriz utilizando un método iterativo.
        """
        a, b, c = self.matriz[0]
        d, e, f = self.matriz[1]
        g, h, i = self.matriz[2]

        # Fórmula del determinante para una matriz 3x3
        det = (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)
        return det