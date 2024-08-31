'''
Algorithm Question:
Given a list of random numbers, Write a program to determine which 
numbers in the list are even or odd. 
'''
# [3, 9, 10, 11, 17, 23, 25, 28, 29, 37, 39, 44, 45, 47, 56, 57, 85, 93, 99]
x = [3, 9, 10, 11, 17, 23, 25, 28, 29, 37, 39, 44, 45, 47, 56, 57, 85, 93, 99]
for i in x:
    if i % 2 == 0:
        print(i,"it is an even number")
    else:
        print(i,"it is an odd number")
    # if % i == 0:
    #     print("the number is even")
    # else:
    #     print("the number is odd")

122
# practice 2: 
# ask for a number, then check if the number is a multiple by 6
x = int(input("enter a number"))
if x % 6 == 0:
    print("the number is a muliple by 6")
else:
    print("the number is not a muliple by 6")


# # Exercise 1: Points Game
# """
# In this game, players collect points that are added to their total score. 
# The player can only see the last digit of their score on a display. 
# Your task is to write a Python program that takes the player’s total score 
# as input and returns the last digit of the score.

# Example input: 12345
# Expected output: 5

# HINT: Use the modulus operator (%) to find the last digit of the score.
# """
# score = 12345
x = int(input("enter your score: "))
print(f"The last digit of {x} is {x%1000}")


