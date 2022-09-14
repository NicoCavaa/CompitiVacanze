def sommaMultipli(n, fattore = [3, 5]):
    x = 0
    for m in range(1, n):
        for f in fattore:
            if f != 0 and m % f == 0:
                x += m
                break
    return x

sommaMultipli(1)
sommaMultipli(1000)
sommaMultipli(20, [7, 13, 17])