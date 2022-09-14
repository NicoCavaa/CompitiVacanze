def square(n):
    if n < 1 or n > 64:
        raise ValueError("Numero non compreso tra 1 e 64")
    return 2 ** (n - 1)
def total():
    return 2 ** 64 - 1