import string, sys

def verifica(str1, lettere=string.ascii_lowercase):
    controllo = set(lettere)
    return controllo <= set(str1.lower())
 
print ( verifica('La veloce volpe marrone salta sopra il cane pigro')) 
