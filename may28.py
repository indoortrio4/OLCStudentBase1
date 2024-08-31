####################### string/list slicing ###############
# sometimes you will be asked to retrieve part of a string, part of a list
# word = "MALAYSIA"

# # extract the first letter, extract the last letter
# # print(word[0])

# planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter','saturn', 'uranus', 'neptune']
# print(planets[2])

# extract the last character
# print(word[-1])
# print(planets[-1])

# extract the 4th planet from planets
# print(planets[3])
# extract the last second letter from word
# print(word[-2])

# slicing [start: stop: step]
# syllable1 = word[:2]
# print(syllable1)

#extract the first 2 planets from planet
# planet1 = planets[0:2]
# print(planet1)

# # extract LAY from MALAYSIA
# syllable2 = word[2:5]
# print(syllable2)

# # extract planet 3 to 5
# idk = planets[2:5]
# print(idk)

# syllable3 = word[5:]
# print(syllable3)
# idkk = planets[5:]
# print(idkk)

# temp1 = word[::2]
# print(temp1)

# idkkk = planets[::2]
# print(idkkk)


######## HOW TO REVERSE A STRING #######
### MALAYSIA will change to AISYALAM
# reverse = word[::-1]
# print(reverse)
# idkkkk = planets[::-1]
# print(idkkkk)

# write a program to generate a user name
# ask user for first name e.g. Jovan
# ask user for last name e.g. Lee
# Form the user name with first 4 characters of first name + first 4 characters of last name
# assume in this case, first name and last name has minimum of length 4
# output the username in lowercase
# first = input("enter your first name: ")
# second = input("enter your second name: ")
# form = first[0:4]
# form1 = second[0:4]
# add = (form+form1).lower()
# print(add)




############################################### Practice Conditions
# 3. Work with Conditional Statements
# Write multiple if-elif-else constructs.
# Understand logical operators (and, or, not).

# Question 1: Check if a number is positive, negative, or zero
# Test case 1: example input: 5, example output: "Positive"
# Test case 2: example input: -3, example output: "Negative"
# number = int(input("enter a number: "))
# if number < 0:
#   print("number is negative")
# elif number == 0:
#     print("number is zero")
# else:
#   print("number is postive")



# Question 2: Check if a number is even or odd
# Test case 1: example input: 4, example output: "Even"
# Test case 2: example input: 7, example output: "Odd"

# use the modulus --- remainder after a division, 
# # for even numbers if there is no remainder after a division by 2, means its even number
# number = int(input("enter a number: "))
# if number % 2 == 0:
#   print("number is even")
# else:
#   print("number is odd")

  


# Question 3: Check if a person is eligible to vote (age 21 or above)
# Test case 1: example input: 22, example output: "Eligible to vote"
# # Test case 2: example input: 16, example output: "Not eligible to vote"
# age = int(input("enter your age: "))
# if age >= 21:
#   print("you can vote")
# else:
#   print("you cant vote")


# Question 4: Check if a number is within a specific range (10 to 20 inclusive)
# Test case 1: example input: 15, example output: "Within range"
# Test case 2: example input: 25, example output: "Out of range"
# number = int(input("enter a number: "))
# if number >20:
#   print("number is out of range")
# elif number<10:
#   print("number is out of range")
# else:
#   print("number is within range")

# if number >= 10 and number <= 20:
#   print("number is within range")
# else:
#   print('out of range')

# Question 5: Check if a character is a vowel or consonant
# Test case 1: example input: "a", example output: "Vowel"
# Test case 2: example input: "b", example output: "Consonant"
# in membership
# letter = 'z'
# word = 'abcde'
# if letter in word:
#   print(letter, 'exists in ', word)
# else:
#   print(letter, 'does not exists in ', word)
# vowel = 'aeiou'
# letter = input("enter a letter: ").lower()
# if letter in vowel:
#   print(letter,"is a vowel")
# else:
#   print(letter,"is not a vowel")


# Question 6: Determine the largest of three numbers
# Test case 1: example input: 3 7 5, example output: "Largest: 7"
# Test case 2: example input: 10 4 6, example output: "Largest: 10"
one = int(input("enter number1: "))
two = int(input("enter number2: "))
three = int(input("enter number3: "))
if one > two and one > three:
  print("number 1 is the biggest")
elif two > one and two >three:
  print("number2 is the biggest")
elif three > two and three >one:
  print("number3 is the biggest")

# Question 7: Grade categorization based on marks
# Test case 1: example input: 85, example output: "Grade: A"
# Test case 2: example input: 65, example output: "Grade: C"


