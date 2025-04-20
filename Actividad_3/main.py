if __name__ == "__main__":
    carrera = CarreraIntergalactica()

    # Agregar naves
    carrera.agregar_nave(NaveEspacial("Cometa Veloz", 120, 10, 50))
    carrera.agregar_nave(NaveEspacial("Titán del Cosmos", 200, 15, 100))
    carrera.agregar_nave(NaveEspacial("GX-1 Explorer", 150, 8, 6))
    carrera.agregar_nave(NaveEspacial("GX-2 Voyager", 180, 12, 8))
    carrera.agregar_nave(NaveEspacial("Estrella Fugaz", 90, 5, 4))

    # Ordenar por nombre y longitud
    carrera.ordenar_por_nombre_y_longitud()

    # Mostrar información de naves específicas
    print("Información de 'Cometa Veloz' y 'Titán del Cosmos':")
    carrera.mostrar_info_naves(["Cometa Veloz", "Titán del Cosmos"])

    # Cinco naves con mayor cantidad de pasajeros
    print("\nCinco naves con mayor cantidad de pasajeros:")
    carrera.cinco_mayor_pasajeros()

    # Nave que requiere mayor cantidad de tripulación
    print("\nNave con mayor cantidad de tripulación:")
    carrera.nave_mayor_tripulacion()

    # Naves cuyo nombre comienza con "GX"
    print("\nNaves cuyo nombre comienza con 'GX':")
    carrera.naves_comienzan_con("GX")

    # Naves que pueden llevar seis o más pasajeros
    print("\nNaves que pueden llevar seis o más pasajeros:")
    carrera.naves_con_seis_o_mas_pasajeros()

    # Nave más pequeña y más grande
    print("\nNave más pequeña y más grande:")
    carrera.nave_mas_pequena_y_grande()