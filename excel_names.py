import openpyxl

wb = openpyxl.load_workbook('cSpace_Bookingv1.xlsx')
sheet = wb["Clients"]

nameslist = []

for cell in sheet['A']:
	nameslist.append(cell.value)
print(nameslist)

#received error when trying to use if statement.
	
for i in nameslist:
		first = [i.split(' ')[0] for i in nameslist]
print(first)

for i in nameslist:
	last = [i.split(' ')[-1] for i in nameslist]
print(last)


issues = []
for cell in sheet['F']:
	issues.append(cell.value)
print(issues)


