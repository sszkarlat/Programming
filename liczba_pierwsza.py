def czy_pierwsza(n):
    pierwsze = []
    if n % 2 == 0:
        return False

    pierw = int(n ** 0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False


print(czy_pierwsza(2))
