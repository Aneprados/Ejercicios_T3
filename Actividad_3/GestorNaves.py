class GestorNaves:
    def __init__(self, naves):
        self.naves = naves

    def ordenar_por_nombre_y_longitud(self):
        return sorted(self.naves, key=lambda x: (x.nombre, -x.longitud))

    def obtener_informacion_naves(self, nombres):
        return [nave for nave in self.naves if nave.nombre in nombres]

    def obtener_cinco_mas_pasajeros(self):
        return sorted(self.naves, key=lambda x: x.pasajeros, reverse=True)[:5]

    def obtener_nave_mas_tripulacion(self):
        return max(self.naves, key=lambda x: x.tripulantes)

    def obtener_naves_por_prefijo(self, prefijo):
        return [nave for nave in self.naves if nave.nombre.startswith(prefijo)]

    def obtener_naves_con_pasajeros(self, min_pasajeros):
        return [nave for nave in self.naves if nave.pasajeros >= min_pasajeros]

    def obtener_nave_mas_pequena(self):
        return min(self.naves, key=lambda x: x.longitud)

    def obtener_nave_mas_grande(self):
        return max(self.naves, key=lambda x: x.longitud)