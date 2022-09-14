def classify(numero):
    somma = 0
    if numero <= 0:
        print("numero troppo basso")
    else:
        for x in range(1, numero):
            if numero % x == 0:
                somma += x
        if somma == numero:
            print("numero perfetto")
        elif somma > numero:
            print("numero non perfetto")

numero=19