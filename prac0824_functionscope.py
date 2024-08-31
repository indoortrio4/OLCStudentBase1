'''
Exercise 1: Understanding Function Parameters and Arguments
Objective: Demonstrate that the values of a and b are passed 
            to x and y respectively. Understand that 
            the original values of a and b are passed as arguments to the 
            function parameters x and y.

'''
def multiply(num1,num2):
    return num1*num2
a = 20
b = 40
ans = multiply(a,b)
print(ans)

'''
Exercise 2: Local vs. Global Scope
Objective: Show the difference between a local variable x inside the 
            function and the global variable x outside. 
            Understand the concept of scope.
'''
x =10
def multiply():
    x = 5
    print("outside the function", x)



'''
Exercise 3: Using the global Keyword
Objective: Illustrate how the global keyword allows a function to modify a 
            global variable. Students should see that the change inside the 
            function affects the global variable.
'''
y = 10
def change_global():
    global y



'''
Exercise 4: Shadowing Global Variables
            Learn how local variables can shadow global variables within 
            the function's scope, without affecting the global variable.
'''
z = 20  # Global variable

def shadow_variable():
    z = 10  # Local variable shadows the global one
    print("Inside function:", z)

# shadow_variable()
#print("Outside function:", z)

'''
Exercise 5: Function with Default Parameters
            Objective: This exercise demonstrates how default parameters work 
            when no argument is passed. It will help students understand the 
            flexibility of function calls in Python.
'''
def greet(name="Student"):
    print("Hello, " + name + "!")

# greet("Alice")
# greet()

'''
Exercise 6: Accessing Global Variables within a Function
            Demonstrate how a function can access a global variable when 
            it's not defined within the function itself. 
            In this example, the global variable x is used inside the 
            function add. The function adds the value of x (which is 10) 
            to the argument a (which is 5), resulting in an output of 15.
'''
x = 10

def add(a):
    print(x + a)

# add(5)


'''
Challenge 6:
A programmer is writing a program to calculate the 
check digit for a 12-digit integer.

The check digit is calculated by multiplying the digits 
in odd positions by 3 and the digits in even positions by 1. 
These values are added together to produce a total. 
The total is subtracted from the next multiple of 10 to 
give a final value. If the final value is 10, the check digit is X.

Example: 
12-digit integer = 1  0  3  4  5  6  2  7  1  0  1  3
Result           = 3  0  9  4  15 6  6  7  3  0  3  3
Total = 3 + 0 + 9 + 4 + 15 + 6 + 6 +7 + 3 + 0 + 3 + 3 = 59
The next multiple of 10 is 60 (*hint: nextnum = math.ceil(num/10) * 10)
So, check digit = 60 - 59 = 1

(a) The The program code function calculate() takes a 
    12-digit number as a parameter. It calculates the 
    check digit and returns the check digit.

    Write the code for the function calculate [6]

(b) The main program:
•	Takes as input a 12-digit number until a valid 
    12-digit integer is entered
•	Calls the function calculate() with the valid input 
    as a parameter
•	Outputs the number with the check digit as its 13th digit

Write the code for the main program. [5]

Test that:
103456271013 = 1
123456789012 = 0
135792468013 = 5
'''
x = "103456271013"
def validate(numstring):
    totalodd = 0
    totaleven = 0
    for i in range(len(numstring)):
        print("index #: {}, value={}".format(i,num[i]))
        if i % 2 ==0:
            tempcal = int(numstring[i]) * 3
            totalodd = totalodd + tempcal
        else:
            totaleven = totaleven + int(numstring[i])
            total = totalodd + totaleven
    print(total)
# for i in range(len(num)):
#     print("index #: {}, value={}".format(i, num[i]))
#     #print(num[i])
    
    



'''

Challenge 7:
A developer needs to extract specific characters from a 
given string to generate a user ID.

(a) Write a function generate_user_id(name, birthdate) 
    that takes a user's full name as a single string in the 
    format "First Last" and a birthdate in the format "YYYYMMDD". 
    The function should return a user ID consisting of:

    - The first three letters of the last name (in uppercase),
    - The last two digits of the year of birth,
    - The first letter of the first name (in lowercase).
For example:
generate_user_id("John Doe", "19901225") should return DOE90j.
[6 marks]

(b) Write a main program that:

    - Takes as input a full name and birthdate,
    - Calls the generate_user_id() function,
    - Outputs the generated user ID.
Test cases:

generate_user_id("Alice Tan", "20030515") should return TAN03a.
generate_user_id("Michael Johnson", "19850911") should return JOH85m.
[4 marks]
'''

'''
Challenge: Credit Card Validation
A financial institution needs to verify the validity of credit card numbers 
using the Luhn algorithm.

Task 1: Implementing the Luhn Algorithm
(a) Write a function is_valid_credit_card(card_number) that takes 
    a credit card number as a string and checks if it is valid according 
    to the Luhn algorithm. The function should:

    - Start from the rightmost digit (check digit) and move left.
    - Double every second digit. If the doubling results in a number greater 
      than 9, subtract 9 from it.
    - Sum all the digits (including those not doubled).

If the total sum is divisible by 10, return True 
(indicating the card number is valid); otherwise, return False.

Example:

is_valid_credit_card("4539148803436467") should return True.
is_valid_credit_card("1234567812345670") should return False.
[6 marks]

Task 2: Testing the Function
(b) Test your function with the following credit card numbers 
and determine if they are valid:

4539148803436467
1234567812345670
4485275742308327
6011514433546201
1234567812345678
Write the expected output for each test case.
'''
