class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __str__(self):
        return f"Nombre: {self.nombre}, Longitud: {self.longitud}, Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}"


class CarreraIntergalactica:
    def __init__(self):
        self.naves = []

    def agregar_nave(self, nave):
        self.naves.append(nave)

    def ordenar_por_nombre_y_longitud(self):
        self.naves.sort(key=lambda x: (x.nombre, -x.longitud))

    def mostrar_info_naves(self, nombres):
        for nave in self.naves:
            if nave.nombre in nombres:
                print(nave)

    def cinco_mayor_pasajeros(self):
        top_cinco = sorted(self.naves, key=lambda x: x.pasajeros, reverse=True)[:5]
        for nave in top_cinco:
            print(nave)

    def nave_mayor_tripulacion(self):
        mayor_tripulacion = max(self.naves, key=lambda x: x.tripulantes)
        print(mayor_tripulacion)

    def naves_comienzan_con(self, prefijo):
        for nave in self.naves:
            if nave.nombre.startswith(prefijo):
                print(nave)

    def naves_con_seis_o_mas_pasajeros(self):
        for nave in self.naves:
            if nave.pasajeros >= 6:
                print(nave)

    def nave_mas_pequena_y_grande(self):
        nave_mas_pequena = min(self.naves, key=lambda x: x.longitud)
        nave_mas_grande = max(self.naves, key=lambda x: x.longitud)
        print("Nave más pequeña:")
        print(nave_mas_pequena)
        print("Nave más grande:")
        print(nave_mas_grande)


