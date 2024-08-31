'''
A 2-player game is being programmed.
The following program allows each player, in turn, to enter the names of 5 animals. 
It converts the name of each animal to lower case. 
Each animal entered by player 2 is their guess for the animal entered by player1.
num_of_animals = 5
for x in range(num_of_animals):
  p1_animal = input(“Player 1, please enter an animal: “)
  p1_animal = p1_animal.lower()


  p2_guess = input(“Player 2, please enter your guess: “)
  p2_guess = p2_guess.lower()
Open the fie ANIMALGAME.py
Save the file as ANIMAL_2023_<your name>_<centre number>_<index number>.py


Question 1: 
6.	Edit the program to allow player 1 to keep entering animals until that player 
does not want to enter any more. All animals entered by player 1 must be stored in a list. 


Once all animals have been entered by player 1, player 2 will enter a single guess. 

All inputs and outputs must have suitable messages. 

Save your program. 

#######################
Question 2:
7.	Save your program as ANIMAL2_2023_<your name>_<centre number>_<index number>.py [3 marks]

Edit your program to search the list of animals to find the guess entered by player 2. 
Player 2 has a score that starts at 0. 
If the guess entered by player 2 is found in the list:

> the animal is removed from the list
> the score for player 2 is incremented by 1

Save your program.
########################

Question 3:
8.	Save your program as ANIMAL3_2023_<your name>_<centre number>_<index number>.py

Edit your program to allow player 2 to keep entering guesses until they 
enter an animal that is not found in the list, or until the list is empty. 
When player 2 enters an animal that is not found in the list:

> the game ends and informs player 2 the game is over
> a message is displayed showing:
>>> player 2 their score
>>> the animals that are still in the list.

All inputs and outputs must have suitable messages.
Save your program.

[3 marks]

'''
##### List Practice
zoo = ['cat', 'dog', 'tiger']

checkanimal = 'cat'
if checkanimal in zoo:
  print(checkanimal, 'is in the zoo')
else:
  print(checkanimal, 'is not in the zoo')

# # add a new animal to zoo .append()
# zoo.append('lion')

# # to retrieve an item from the list based on index
# print(zoo[2], 'is my favourite animal')

# print(zoo)
# # remove item from the list by the value
# zoo.remove('tiger')

# # use for loop to loop through a list
# for animal in zoo:
#   print('I want to see', animal)

########## Question 1 ###############
# p1_list = []
# while True:
#   p1_animal = input("enter a animal:")
#   p1_animal.lower()
#   if p1_animal == "stop":
#     break
#   p1_list.append(p1_animal)
# print(p1_list)
# p2_guess = input("enter your guess:")
# # something exists in something .>>>>> 'in' keyword
# if p2_guess in p1_list:
#   print("correct")
# else:
#   print("incorrect")
# # ask player 2 to guessanimals_list = []

########## Question 2 ###############
  p1_list = []
  while True:
    p1_animal = input("enter a animal:")
    p1_animal.lower()
    if p1_animal == "stop":
      break
    p1_list.append(p1_animal)
  print(p1_list)
  p2_guess = input("enter your guess:")
  # something exists in something .>>>>> 'in' keyword
  score = 0
  if p2_guess in p1_list:
    print("correct")
    score += 1
  else:
    print("incorrect")
    
  # ask player 2 to guessanimals_list = []






########## Question 3 ###############