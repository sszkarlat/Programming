def NWD(x, y):
    while y:
        x, y = y, x % y
    return x


print(NWD(27, 9))  # Jeżeli liczymy dla dwóch wartości
print(NWD(NWD(69, 27), 9))  # Jeżeli liczymy dla trzech wartości, zgodnie z zasadą


# NWD(a, b, c) = NWD(NWD(a, b), c)

def NWD2(x, y):
    while y:
        tmp = x
        x = y
        y = tmp % y
    return x


print(NWD(27, 9))
print(NWD2(27, 9))
