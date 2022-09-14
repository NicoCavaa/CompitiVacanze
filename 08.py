
def controllo(s1, s2):
 if(sorted(s1)== sorted(s2)):
  print("anagramma")
 else:
  print("non è un anagramma")  
  
s1 ="casa"
s2 ="polo"
controllo(s1, s2)