from Polinomio import Polinomio


class Lanzador:
    def ejecutar(self):
        p1 = Polinomio()
        p1.agregar_termino(3, 2)
        p1.agregar_termino(5, 1)

        p2 = Polinomio()
        p2.agregar_termino(1, 1)
        p2.agregar_termino(2, 0)

        print("Polinomio 1:", p1)
        print("Polinomio 2:", p2)

        resta = p1.restar(p2)
        print("Resta:", resta)

        cociente, residuo = p1.dividir(p2)
        print("Cociente:", cociente)
        print("Residuo:", residuo)

        p1.eliminar_termino(1)
        print("Polinomio 1 después de eliminar término con exponente 1:", p1)

        existe = p1.existe_termino(2)
        print("¿Existe término con exponente 2 en Polinomio 1?", existe)