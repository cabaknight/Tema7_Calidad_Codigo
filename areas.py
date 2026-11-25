import math


def calcular_cuadrado(lado):
    return lado * lado


def calcular_rectangulo(base, altura):
    return base * altura


def calcular_circulo(radio):
    return math.pi * radio ** 2


def main():
    print("===== CALCULADORA DE AREAS =====")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Circulo")

    opcion = input("Seleccione una figura: ")

    if opcion == "1":
        lado = float(input("Ingrese el lado: "))
        area = calcular_cuadrado(lado)
        print("Area del cuadrado:", area)

    elif opcion == "2":
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = calcular_rectangulo(base, altura)
        print("Area del rectangulo:", area)

    elif opcion == "3":
        radio = float(input("Ingrese el radio: "))
        area = calcular_circulo(radio)
        print("Area del circulo:", round(area, 2))

    else:
        print("Opcion no valida.")


if __name__ == "__main__":
    main()