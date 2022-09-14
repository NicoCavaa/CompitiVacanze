def append(x, y):
    lungX = lunghezza(x)
    lungY = lunghezza(y)
    fine = [None] * (lungX + lungY)
    fine[:lungX] = x
    fine[lungX:] = y
    return fine

def concat(lists):
    fine = []
    for one_list in lists:
        fine = append(fine, one_list)
    return fine

def filter(function, x):
    return [x for x in x if function(x)]

def lunghezza(x):
    fine = 0
    for _ in x:
        fine += 1
    return fine

def map(function, x):
    return [function(x) for x in x]

def riempiS(function, x, acc):
    fine = acc
    for x in x:
        fine = function(fine, x)
    return fine

def riempiD(function, x, acc):
    fine = acc
    for x in contrario(x):
        fine = function(x, fine)
    return fine

def contrario(x):
    lungX = lunghezza(x)
    fine = [None] * lungX
    i = 0
    while i != lungX:
        fine[i] = x[lungX - 1 - i]
        i += 1
    return fine