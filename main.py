def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def pomnoz(a, b):
    return a * b


def podziel(a, b):
    if b == 0:
        return "Nie dzielimy przez zero"
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", dodaj(2, 3))
    print("7 - 4 =", odejmij(7, 4))
    print("6 * 7 =", pomnoz(6, 7))
    print("8 / 0 =", podziel(8, 0))

# potęga w przygotowaniu