def czy_potega(x):
    while x % 3 == 0:
        x /= 3
    return True if x == 1 else False


print(czy_potega(729))
