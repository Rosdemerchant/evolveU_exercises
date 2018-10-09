import openpyxl

wb = openpyxl.load_workbook('cSpace_Bookingv1.xlsx')
sheet = wb["Clients"]

def cell_has_value(ws, row, col):
    if row > sheet.max_row:
        return False
    if col > sheet.max_column:
        return False
    if not sheet.cell(row=row, column=col).value:
        return False
    if not sheet.cell(row=row, column=col).value.strip():
        return False

    return True


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


