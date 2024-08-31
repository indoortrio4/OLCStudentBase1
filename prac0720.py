########## string formatting  #############
#### string concatenation --- - joining strings together
name = "John"
age = 18
### My name is John, I am 18 years old

##### option 1: print() and comma, simple, type conversion for you
#strmsg =  # tuple
#str1=  # tuple, list
print("my name is", (name), "i am", str(age),"years old")

###### options 2: use + operator to join, need to handle type conversion
str2= "my name is" + (name) + "i am" + str(age) + "years old"
print(str2)

###### option 3: use f string -- what most programmers use, 
strmsg2 = f"My name is {name}. I am {age} years old."
print(strmsg2)

##### option 4: use "".format() #backward compatible
strmsg3 = "My name is {}, I am {} years old.".format(name, age)
print(strmsg3)


type1 = 'cannot'
type2 = 'binary'

#0b10 is a binary literal for 2
x = 'There are {} types of people in this world.'.format(0b10) 
y = 'Those who can read {1} and those who {0}'.format(type1, type2)

print(x)
print(y)

###################################################
# #### string.format()
# # option 1: define the variable and value inside.
txt1 = "My name is {fname}, I'm {age}".format(fname = "Alex", age = 18)

# # option 2: use indexes, the numbering must match
txt2 = "My name is {0}, I'm {1}".format("Alex",18)

# # option 3: just use the position
txt3 = "My name is {}, I'm {}".format("Alex",18)

# # Example 1: show a binary conversion number
# #Use "b" to convert the number into binary format:
# txtbinary = "The binary version of {0} is {0:b}"
# print(txtbinary.format(5))

# # Example 2: show a decimal number
# #Use "d" to convert a number, in this case a binary number, 
# # into decimal number format:
# txtdec = "We have {:d} chickens."
# print(txtdec.format(0b101))

# # Example 3: show a fixed point number
# #Use "f" to convert a number into a fixed point number, 
# # default with 6 decimals, but use a period followed by a number 
# # to specify the number of decimals:
# txt = "The price is {:.2f} dollars."
# print(txt.format(45))

# #without the ".2" inside the placeholder, 
# # this number will be displayed like this:
# txt = "The price is {:f} dollars."
# print(txt.format(45))

# # reference for the different formats
# # https://www.w3schools.com/python/ref_string_format.asp


# #######################################################
# #                    Practice                         #
# #######################################################
# '''
# # Exercise 1: Personalized Greeting
# # Write a Python program that takes a user's first name and age as input 
# # and prints a personalized greeting using the format() function.
# # Example input: first_name = "Alex", age = 18
# # Expected output: "Hello, Alex! You are 18 years old."
# '''

# first_name = input("Enter your first name: ")
# age = int(input("Enter your age: "))
# greeting = "Hello, {fname}! You are {age} years old.".format(fname=first_name, age=age)
# print(greeting)

# '''
# # Exercise 2: Itemized Receipt
# # Create a Python program that generates a receipt for three items 
# # purchased at a store. Use the format() function to display the item 
# # names and their prices.
# # Example input: item1 = "Apple", price1 = 0.5, item2 = "Banana", 
# # price2 = 0.3, item3 = "Cherry", price3 = 0.2
# # Expected output:
# # Receipt:
# # 1. Apple: $0.50
# # 2. Banana: $0.30
# # 3. Cherry: $0.20
# '''

# item1 = "Apple"
# price1 = 0.5
# item2 = "Banana"
# price2 = 0.3
# item3 = "Cherry"
# price3 = 0.2

# receipt = """
# Receipt:
# 1. {0}: ${1:.2f}
# 2. {2}: ${3:.2f}
# 3. {4}: ${5:.2f}
# """.format(item1, price1, item2, price2, item3, price3)
# print(receipt)

# '''
# # Exercise 3: Binary and Decimal Conversion
# # Write a Python program that converts a number to both its binary 
# # and decimal format using the format() function.
# # Example input: number = 5
# # Expected output:
# # The binary version of 5 is 101
# # The decimal version of 101 is 5
# '''

# number = int(input("Enter a number: "))
# binary_conversion = "The binary version of {0} is {0:b}".format(number)
# decimal_conversion = "The decimal version of {0:b} is {0:d}".format(number)
# print(binary_conversion)
# print(decimal_conversion)
