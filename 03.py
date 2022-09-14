def inLista(l, s):
	num = False
	if s == []:
		num = True
	elif s == l:
		num = True
	elif len(s) > len(l):
		num = False

	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					num = True

	return num

a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(inLista(a, b))
print(inLista(a, c))
