
from NaveEspacial import NaveEspacial
from GestorNaves import GestorNaves

def main():
    # Lista de naves espaciales
    naves = [
        NaveEspacial("Cometa Veloz", 120, 10, 50),
        NaveEspacial("Titán del Cosmos", 200, 15, 100),
        NaveEspacial("GX-1", 90, 5, 6),
        NaveEspacial("GX-2", 110, 8, 8),
        NaveEspacial("Estrella Fugaz", 150, 12, 80),
        NaveEspacial("Nebulosa", 180, 20, 120),
        NaveEspacial("Aurora", 100, 6, 10),
    ]

    gestor = GestorNaves(naves)

    # Ordenar por nombre ascendente y longitud descendente
    print("Naves ordenadas por nombre y longitud:")
    for nave in gestor.ordenar_por_nombre_y_longitud():
        print(nave)

    # Información de "Cometa Veloz" y "Titán del Cosmos"
    print("\nInformación de 'Cometa Veloz' y 'Titán del Cosmos':")
    for nave in gestor.obtener_informacion_naves(["Cometa Veloz", "Titán del Cosmos"]):
        print(nave)

    # Cinco naves con mayor cantidad de pasajeros
    print("\nCinco naves con mayor cantidad de pasajeros:")
    for nave in gestor.obtener_cinco_mas_pasajeros():
        print(nave)

    # Nave que requiere mayor cantidad de tripulación
    print("\nNave que requiere mayor cantidad de tripulación:")
    print(gestor.obtener_nave_mas_tripulacion())

    # Naves cuyo nombre comienza con "GX"
    print("\nNaves cuyo nombre comienza con 'GX':")
    for nave in gestor.obtener_naves_por_prefijo("GX"):
        print(nave)

    # Naves que pueden llevar seis o más pasajeros
    print("\nNaves que pueden llevar seis o más pasajeros:")
    for nave in gestor.obtener_naves_con_pasajeros(6):
        print(nave)

    # Nave más pequeña y más grande
    print("\nNave más pequeña:")
    print(gestor.obtener_nave_mas_pequena())
    print("\nNave más grande:")
    print(gestor.obtener_nave_mas_grande())


if __name__ == "__main__":
    main()