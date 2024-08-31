# for loop 
# know exactly how many times to loop
# loop through a string, list, dictionary
# 4 ways of using, 
#1. range(start, stop, step)
#2. loop through a string
#3. loop through a list
#4. loop through a dictionary

# repeat x number of times
# for i in range(3):
#   print('hello')

# count numbers
# for i in range(10):
#   print(i)

# option 1: range(stop) 
# option 2: range(start, stop)
# option 3: range(start, stop, step)

### option 2 : range(start, stop)
# print the numbers 1 - 10
# for i in range(1, 11):
#   print(i)

# print the numbers from 6 - 15
  
# for i in range(6 , 16):
#   print(i)

### option 3 : range(start, stop, step)

# print out the multiples of 3 up till 36
# for i in range(3, 37, 3):
#   print(i)

# print out the numbers 10 to 1, in descending order
# for i in range(10, 0, -1):
#   print(i)

# print out the multiples of 6
# for i in range(6, 73 , 6):
#   print(i)
 
  
# print out a countdown from 15 to 1
# for i in range(15 , 0, -1):
#   print(i)
# while loop

#################################################################
#2. loop through a string
#################################################################

# word = 'antilope'
# for i in word:
#   print(i)

# ask for a name, and then write a cheer for this name
# name = input("enter your name: ")
# for i in name:
#   print("give me a", i)


###################################################
##3. for loop through a list
#################################################
# create a list of 5 countries
# loop through the list, and say 'someday i would like to visit [country name]'

# country = ['malaysia','france', 'italy']
# for i in country:
#   print('someday i would like to visit', i )




##############################################
##### while loop
##############################################

# count numbers using the while loop
# count numbers from 1 - 14
# count = 1
# while count < 15:
#   print(count)
#   count = count + 1

# while validation
# write a program to ask for a number
# keep repeating until the user type all numbers
# if user don't type numbers, print 'pls type numbers only'

# while True:
#   user = input("enter a number: ")
#   if user.isdigit():
#     break
#   else:
#     print("pls type numbers only")

#################################################
#### ALGORITHM Find Min/ Max in a list
###################################################
# Pre ####
# Q1 Generate a list of 100 random numbers
# each number is a range from 1 to 1000
# every number in this list must be unique
# import random

# # declare a list variable
# list_numbers = []

# while len(list_numbers) <100:
#   # generate a random number #random.randint(1, 1000)
#   random_number = random.randint(1,1000)
#   if random_number not in list_numbers:
#     list_numbers.append(random_number)
 
#list_numbers contains 100 random unique numbers
# Q2 Find the smallest number in this list
# loop through every number in the list
# tempmin = 1000
# for number in tempin:
#   number < tempin
#   number 



# print('the smallest number is', tempmin)


# Q3Find the maximum number in this list

# Q4 Find the average of this list





