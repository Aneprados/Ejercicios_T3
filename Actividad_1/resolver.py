

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(2000)  # Increase recursion limit
    num_piedras = 20  # Reduce the number of stones to a manageable level
    juego = TorreDeHanoi(num_piedras)
    print("Estado inicial:")
    juego.mostrar_estado()
    print("\nResolviendo...\n")
    juego.resolver()
    print("\nEstado final:")
    juego.mostrar_estado()