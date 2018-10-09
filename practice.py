
#find the biggest #
def bigger(a, b):

	if a > b:
		return a
	else:
		return b

#find the biggest # in a list
def biglist(listx):
	biggest = listx[0]
	for i in listx:
		if i > biggest:
			biggest = i
		return biggest

#count the occurances in a list
def count_occ(listy):
	dicta={}
	for i in listy:
		if i in dicta:
			dicta[i] = dicta[i] + 1
		else: 
			dicta[i] = 1

	return dicta
	

