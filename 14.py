def controllo(numero):
    lista = [int(i) for i in str(numero)]
    lung = len(str(numero))
    appoggio = []
    for item in lista:
        appoggio.append(item**lung)
    if sum(appoggio) == numero:
        return True
    else:
        return False