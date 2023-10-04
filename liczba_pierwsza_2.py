def is_prime(number):
    if number < 2:
        return False
    else:
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True


primeNumbers = [number for number in range(0, 101) if is_prime(number)]
print(primeNumbers)
