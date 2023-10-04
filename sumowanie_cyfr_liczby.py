def suma(x):
    s = 0
    while x:  # dopóki zostały jakieś cyfry
        s = s + x % 10  # dodaj ostatnią cyfrę (jedności)
        x = x // 10  # podziel liczbę przez 10
    return s


print(suma(222053475982357983))
