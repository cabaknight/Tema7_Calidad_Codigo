import math


def calcular_cuadrado(lado):
    return lado ** 2


def calcular_rectangulo(base, altura):
    return base * altura


def calcular_circulo(radio):
    return math.pi * radio ** 2


def solicitar_medida(mensaje):
    while True:
        try:
            valor = float(input(mensaje))

            if valor > 0:
                return valor

            print("El valor debe ser mayor que cero.")

        except ValueError:
            print("Ingrese un número válido.")


def main():
    print("===== CALCULADORA DE AREAS =====")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Circulo")

    opcion = input("Seleccione una figura: ")

    if opcion == "1":
        lado = solicitar_medida("Ingrese el lado: ")
        area = calcular_cuadrado(lado)
        print("Area del cuadrado:", area)

    elif opcion == "2":
        base = solicitar_medida("Ingrese la base: ")
        altura = solicitar_medida("Ingrese la altura: ")
        area = calcular_rectangulo(base, altura)
        print("Area del rectangulo:", area)

    elif opcion == "3":
        radio = solicitar_medida("Ingrese el radio: ")
        area = calcular_circulo(radio)
        print("Area del circulo:", round(area, 2))

    else:
        print("Opcion no valida.")


if __name__ == "__main__":
    main()