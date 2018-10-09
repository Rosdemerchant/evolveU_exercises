#Verify all the names for a month.
#Input = month, year
#output = list of unverified clients
#generate a list of clients from Client tab v_client
#generate a list or dictionary of that month's clients from the calendar
#(loop through all rows and columns that aren't date or room named) m_client
#compare the two: if mclient not in v client, append mclient to unver_client list
#if unver_client is empty, return 'all good' message
#if not empty, return list of all unverified clients.

import openpyxl
wb = openpyxl.load_workbook('cSpace_Bookingv1.xlsx')
sheet = wb["Clients"]



v_client = []

for cell in sheet['A']:
	v_client.append(cell.value)
print(v_client)
  
