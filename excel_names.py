import openpyxl

wb = openpyxl.load_workbook('cSpace_Bookingv1.xlsx')
sheet = wb["Clients"]


for cell in sheet['A']:
	fullname = cell.value
	x=fullname.split()
	if fullname != "Name":
		y=(x[0])
		print(y)
		
for cell in sheet['A']:
	fullname = cell.value
	x=fullname.split()
	if fullname != "Name":
		z=(x[1])
		print(z)
		
for cell in sheet['F']:
	issues=cell.value
	print(issues)

# nameslist.append(cell.value)

# print("print nameslist", nameslist)

# for i in nameslist:
# 	print("-->",i)
# 	print("ros")
# 	print("larry")
# 	print(i)


#received error when trying to use if statement.
	
# for i in nameslist:
# 	first = i.split(' ')[0]
# print("first names", first)

# for i in nameslist:
# 	last = i.split(' ')[-1]
# print("last names", last)


# 

