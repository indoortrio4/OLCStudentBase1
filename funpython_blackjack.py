'''
Create the game of Black Jack
'''
import random
import time

suits = ["♣ CLUB", "♦ DIAMOND","❤ HEART","♠ SPADE"]
ranks = ['2','3','4','5','6','7','8','9','JACK','QUEEN','KING','ACE']

# Step 1: Create the deck of cards
# Create a dictionary to store the value of each card rank
# Cards 2–10 are worth their face value, J, Q, K are worth 10, 
# and Ace can be 1 or 11
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
'JACK':10, 'QUEEN':10,'KING':10, 'ACE':11}
deck = []
# Combine ranks and suits to build a deck of cards
for s in suits:
    for r in ranks:
        deck.append([r,s])

# Shuffle the deck
for i in range(10):
    random.shuffle(deck)

# Initialize hands for the player and the banker
# Player and banker both start with two cards
player_hand = [deck.pop(),deck.pop()]
banker_hand=[deck.pop(),deck.pop()]
# Function to calculate the value of a hand
print(player_hand)
print(banker_hand)
# Function to display the hand cards (with rank and suit)
def calculate_hand(hand):
    points = 0
    ace_count = 0
    for c in hand:
        if c[0] == "ACE":
            ace_count += 1
        card_point = values[c[0]]
        points = points + card_point
    while points > 21 and ace_count >0:
            point = points - 10
            ace_count = ace_count -1
            return (points)

print(calculate_hand(player_hand))
print(calculate_hand(banker_hand))

# Game Loop, Player and Banker Turn
   
def display_hand(hand, turn):
     if turn.lower() == "player":
        print("\n\n\n")
        print("+"*30)
        print("{:^30}".format("players hand"))
        for c in hand:
            card_value="{} {}".format(c[0],c[1])
            print("{:^30}.formate(card_value)")
            score_msg = (" you have {} points.").format(calculate_hand(hand))
            print("{:^30}.formate(score_msg)")

            print("+"*30)
            print("\n")
        elif turn.lower() == "banker_hide":
                print("\n\n\n")
                print("$"*30)
                print("{:^30}".format("Banker Hand"))

                b_card = hand[0]
                b_card_value = "{} {}".format(b_card[0],b_card[1])
                print("{:^30}.format(b_card_value)")
                print("{:^30}").format("????")
                print("$"*30).fromat
                print("{:^30}.format(banker_hand)")
                               
display_hand(player_hand, "player")
display_hand(banker_hand,"banker_hid")

    # Show player's hand and banker's visible card

    # Check for Blackjack (21 points) in the player's hand

    # Ask player if they want to hit or stand

    #  Add a new card to the player's hand if they choose to hit

        # Check if the player busts (goes over 21)

    # End player's turn

    # Banker's turn (if player hasn't busted)
    # Banker hits until their total is 17 or more
    # Compare player and banker totals to determine the winner