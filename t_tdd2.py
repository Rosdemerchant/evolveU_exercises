

import datetime as dt
from datetime import datetime

#add5 to a number
def plus_five(x):
	return x+5

#find highest number without using max function
def highestNumber(l):
    list = [1,2,3,4]
    list.sort()
    return list[-1]

#find lowest number without using min function
def lowestNumber(list):
	list = [1,2,3,4]
	list.sort()
	return list[0] 

#Yields all the positions of the pattern 'Mary had' in the string s.
def has_string(maryhad, s):
    i = s.find("Mary had")
    while i != -1:
        yield i
        i = s.find("Mary had", i+1)


#convert a string to a date 2018-09-03 always in this format
def to_date(dt):
	return datetime.strptime(dt, "%Y-%m-%d").date()
	print(datetime_obj.date())

#find the number of days between two dates
def date_diff(date1, date2):
	# date1 = date(2008, 9, 1)
	# date2 = date(2018, 9, 2)
	delta = date1 - date2
	print(date1, date2)

#find the number of days between Sept 1st this year and the mayan end of the world 	
def datemayan(date1, date2):
	date1 = date(2012-12-21)
	date2 = date(2018-9-01)
	return (delta.days)
	print(date_diff(date('2012-12-21'), date('2018-09-01')))

#check if a value is contained in a list
def contains(listhave):
	listhave = ['a', 'b' 'c' 'd']
	if 'a' in listhave:
    		print("The letter a is in the list.")
	else:
    		print("The number a is NOT in the list.")

#add the contents of a list
def add_contents(contentlist):
	listhas = [1,2,3]
	listhas.append = (4,5,6)
	return listhas

#return the value for the key and add mine to the end of the string
def lookup(add_mine):
	dict_l = {1:'one', 2:'two', 3:'three'}
	str(get(1)) + 'mine'
