#
# while loop

def w_loop(a):
	while a < 20:
		print(a)
		print("the number is less than 20 and is an even number")
		a = a + 2
	else:
		print("the number is not in the loop")
	
# range

def pets(pet_list):
	pet_list=['cat', 'dog', 'fish', 'turtle']
	for i in range(len(pet_list)):
		print("My favorite pet is", pet_list[i])

# list
def new_l(position):
	a=['Jane', 'Mary', 'Mark', 'Louie', 'Harry']
	b=['Dick', 'Jones', 'Carey', 'Linder', 'Hines']
	position = 5
	print(a[:])
	print(b[:])
	newlist = a + b
	print(newlist)

	
# For this assignment ensure you code using the best
# practices we have talked about. Do this cycle for each
# function you develop. Write the code in this module and
# create the appropriate test file.
# order:
# - write the stub
# - write the tests
# - run the tests (they must fail)
# - make them work
#

#
# All code must be in a function. Write all the code in this
# file and in the test code file. Create one function and several
# tests (in one method) to test the function.
#

#
# Write the code to prove to me you understand a function. Create
# your own function that has at least 5 lines in it. Create the tests
# to prove the function is doing what you expect.
#

#
# Write the code to prove you understand if statements and else
# statements. Make sure there are several statements in the if 
# and else. Write the code that proves to me you understand it.
#

#
# while
#



#
# until
#

#
# range
#

#
# array / list 
#

#
# dictionary
#

#
# string and string functions
#

#
# pick another concept to write a test about.
#

def check_temp(low_temp, high_temp):
	for i in range(low_temp, high_temp):
		if low_temp => 20:
			if high_temp <= 30:
				return 'nice weather'