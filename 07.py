import re

def acro(name):
	acronimo = ''
	split_nouns = re.sub(r"(?<![A-Z ])(?<!^)([A-Z])",r" \1",name)
	cleaned_name = split_nouns.translate(str.maketrans('-','_','|')).split()
	
	for word in cleaned_name:
		acronimo += word[0].upper()
	return acronimo

name="CIAO"