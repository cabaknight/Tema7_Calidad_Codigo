
from abc import ABC, abstractmethod
import math


# Clase base para todas las figuras geométricas.
class Figura(ABC):

    @abstractmethod
    def calcular_area(self):
        pass


# Clase para calcular el área de un cuadrado.
class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


# Clase para calcular el área de un rectángulo.
class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


# Clase para calcular el área de un círculo.
class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2


# Nueva clase para calcular el área de un triángulo.
class Triangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


# Función encargada de mostrar los resultados.
def mostrar_areas(figuras):
    for figura in figuras:
        nombre = figura.__class__.__name__
        area = figura.calcular_area()
        print(f"Área del {nombre}: {area:.2f}")


# Función principal del programa.
def main():
    figuras = [
        Cuadrado(5),
        Rectangulo(6, 4),
        Circulo(3),
        Triangulo(8, 5)
    ]

    print("===== AREAS DE FIGURAS GEOMETRICAS =====")
    mostrar_areas(figuras)


if __name__ == "__main__":
    main()
