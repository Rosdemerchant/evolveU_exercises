 #resource folder

#4  A function is a block of code that only runs when it is called. 
#   There are two things you can do with a function, define it or call it.
#   Python knows how many lines are in a function because 
#   the block of code for that specific function are indented.

#5  How to execute a function:
#   you execute the function by calling it for example number('hello', 'goodbye') print('whatever')

#6  Describe what a test is. How a test can 'Test' or just 'Execute' a function. 
#   Document this as comments in your test Python file. 
#   Keep your comments aesthetically pleasing. 
#   Separate your comments in a way that will be easy for you to reference later.

#   A test is used to ensure your program is executing as expected.
#   A test can execute a function by running code in the test
#   with the outcome you expect from the program file.() 
#   NO ASSERT STATEMENT ex.- t_logic.comp_operators(24, 2)
#   You can execute a function by calling it from the test file.

#7  Pytest is specific to testing python programs (unit tests).  
#   It is used to test each line of code. Pytest looks for the 
#   file(s) you imported at the top of the pytest file.?????
#   It looks for the methods you have defined in your program 
#   code, these method names must also be defined in your pytest.

#8  create a file for your program code.
#   create a function.
#   create a file for your test code.
#   create a stub (return 0) in the program code, and create
#   a test for the function in your test file.
#   indent the block of statements after defining the function so 
#   so that the computer knows they are part of the function.
#   call the function.
#   create a test in your test file and run it.

#9  List the steps in creating functions / tests as a comment in the py file.
#   List the steps in creating functions / tests as a comment in the py file.
#   create a stub
#   create a test file
#   test the stub
#   in the program file, write the statements under the function.
#   test the function.


#9  The seven math operators in Python are:
#   +, -, *, /, %, //, **

#10. Write 3 functions & tests to test 3 math operators that you have not yet used. 
#    Do it in the correct order and show Larry as often as you can.

def math_operators(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    e = x % y
    f = x // y 
    g = x ** y


#   modulus example:
#   The % (modulo) operator yields the remainder 
#   from the division of the first argument by the second.
#   >>> 5 % 2
#   1
def mod(a, b):
    c = a % b
    return c

def floor_division(a, b):
    f = a // b
    return f

def exponent(a, b):
    g = a ** b
    return g

#11.    Write a function to return the largest of 3 numbers with tests. 

def large_n(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

#12     The range() function generates a list of numbers,
#       which is generally used to iterate over with for
#       loops.  Often you will want to use this when you want 
#       to perform an action X number of times, where you may
#       or may not care about the index.  Other times you may 
#       want to iterate over a list (or another iterable object) 
#       while being able to have the index available.

#13     Write 2 function to return a list of numbers between 2 numbers with tests. 
# For example: if I pass 5 and 9; a list with 6,7,8 will be returned. 
# One function will use a for loop and the other will use a while loop.

def num_range(a, b):
    return []
    # for i in range
    #     print(i)


def while_range(a, b):
    return []

    # a = 1
    # while (a <5):
    #     print(a)
    #     a = a + 1


#14   Write a function to return the odd numbers between 2 numbers with tests. 
#       Same as above with odd numbers.

def odd_num(a):
    for i in range(1, 20, 2):
        print(i)
#15
#   list the 6 comparison operators Python has 
#   >Greater than, <Less than, == Equal to, 
#   !=Not equal to, >+Greater than or Equal to
#   <+Less than or equal to.

#16 Write a single function that shows how to use the 6 comparison operators. 
#   Use print() as proof it works but returns nothing. Write a test to run the function 
#   (but not test anything).

def comp_operators(x, y):
    a = x > y
    b = x < y
    c = x == y
    d = x != y
    e = x >= y
    f = x <= y 
    print(a,b,c,d,e,f)  

#17 Write a function to print the contents of a list without using the 'for' statement. 
#   It will return nothing. 
def p_list(list_p):
    list_P = [1,2,3,4,5]
    print(list_p)

#18 Write a function to return the largest number of a list with tests.

def l_list(listx):
    largest = listx[0]
    for i in listx:
        if i >= largest:
            largest = i
    return largest

#19 Write a function to return the longest string (most characters) from a list.

def long_str(alist):     
    a = 0     
    answer = '' 
    for i in alist:         
        x = i     
    if x > a:         
        a = x         
        answer = x     
    elif i == a:         
        if i not in alist:             
            answer = answer + ' ' + i     
    return answer

#20 Write a function to read and print each line of a file. 
#   Use a test to run the code but not to test the code.
