class DeterminanteRecursivo:
    @staticmethod
    def calcular(matriz):
        if len(matriz) == 2:  # Caso base: matriz 2x2
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        
        determinante = 0
        for i in range(len(matriz)):
            submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
            signo = (-1) ** i
            determinante += signo * matriz[0][i] * DeterminanteRecursivo.calcular(submatriz)
        return determinante


class DeterminanteIterativo:
    @staticmethod
    def calcular(matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3:
            raise ValueError("Este método solo funciona para matrices 3x3.")
        
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]
        
        determinante = (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)
        return determinante


# Ejemplo de uso
if __name__ == "__main__":
    matriz = [
        [2, 4, 3],
        [1, 5, 7],
        [6, 8, 9]
    ]
    
    print("Determinante (recursivo):", DeterminanteRecursivo.calcular(matriz))
    print("Determinante (iterativo):", DeterminanteIterativo.calcular(matriz))