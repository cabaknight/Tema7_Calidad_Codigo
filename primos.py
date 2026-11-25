def es_primo(numero):
    """
    Determina si un número es primo.
    """

    if numero < 2:
        return False

    limite = int(numero ** 0.5)

    for divisor in range(2, limite + 1):
        if numero % divisor == 0:
            return False

    return True