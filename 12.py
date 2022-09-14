def inverti(s):
 str = ""
 for i in s:
  str = i + str
 return str

s = "Geeksforgeeks"

print("Originale : ", end="")
print(s)

print("Invertita : ", end="")
print(inverti(s))
