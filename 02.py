def isogramma(string):
    string = string.lower()
    a = [x for x in list(set(list(string))) if x != ' ']
    b = [x for x in list(string) if x != ' ']
    if len(a) == len(b):
        return string + " è un isogramma"
    else:
        return string + " Non è un isogramma"
print(isogramma("dottore"))