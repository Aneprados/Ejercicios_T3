# Ejemplo de uso
if __name__ == "__main__":
    matriz = [
        [2, 4, 3],
        [1, 5, 7],
        [6, 8, 9]
    ]

    matriz_obj = Matriz3x3(matriz)

    print("Determinante (recursivo):", matriz_obj.calcular_determinante_recursivo())
    print("Determinante (iterativo):", matriz_obj.calcular_determinante_iterativo())