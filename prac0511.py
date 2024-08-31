# Practice 1
'''Create a Password Validator program that checks if a password is strong.
1. Ask the user to input a password.
2. Check if the password is at least 8 characters long.
3. Check if it contains at least one uppercase letter and one lowercase letter
4. Check if it contains one digit.
5. Check if it contains a special character "!@#$%^&*()"
6. Provide feedback on which criteria the password pass/ or fail.
7. Indicate if the password is strong if all criteria are met.'''


# y = input("enter your password:")
# lower =  False
# upper = False
# length = False
# digit = False
# special = False
# if len(y) >= 8:
#   length = True
# for char in y:
#   if char.islower():
#     lower = True
#   if char.isupper():
#     upper = True
#   if char.isdigit():
#     digit = True
#   if char in "!@#%^&*()":
#     special = True
# if lower and upper and length and digit and special:
#   print("strong password")
# else:
#   print("weak password")
  
# Practice 2 
'''
Code a Word Guessing Game between 2 persons.
1. Ask Player 1 to input a word for player 2 to guess.
2. Ask Player 2 to input a guess.
  2a. The program will keep asking Player 2 to enter the guess until the correct word is given
3. If Player 2's word guess is too long, inform the player with a suitable message
4. If Player 2's word guess is too short, inform the player with a suitable message
5. If Player 2's word guess is the correct length, inform the player with a suitable message
6. If the word length is correct, give player 2 a hint as to the word
For example: if the Player 1's word is "five", and Player 2 guesses "four",
the program will print "f _ _ _"
7. End the game with suitable messages when Player 2 guesses correctly.
'''
player1 = input("player 1 enter a word:")
while True:
  player2guess = input("guess player1 word:")
  if len(player2guess) < len(player1):
    print("word is too short")
  if len(player2guess) > len(player1):
    print("word is too long")
  if len(player2guess) == len(player1):
    print("word is the same length")
    output = ''  
    for i in range(len(player1)):
      if player1[i] == player2guess[i]:
        output = output + player1[i]
      else:
        output = output + "_"
    print(output)
    if (player2guess) == (player1):
      print("correct!")
      break
  # if (player2guess) == (player1):
  #   print("correct")  

    

