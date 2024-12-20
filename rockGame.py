''' The Game of Rock paper and scissors'''
# Rock Paper Scissors ASCII Art
import random


games = ("""
__ _  __ _ _ __ ___   ___  ___ 
 / _` |/ _` | '_ ` _ \ / _ \/ __|
| (_| | (_| | | | | | |  __/\__\
\__, |\__,_|_| |_| |_|\___||___/
  __/ |                          
 |___/""")
# Rock
ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK
"""

# Paper
PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
PAPER
"""

# Scissors
SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS
"""


signChoice = [ROCK, PAPER, SCISSORS]
print(" Lets Play \n", games)
userChoice = int (input  ("""Enter your Choice Number \n Enter 1 for Rock \n Enter 2 for Paper \n Enter 3 for Scissors""" ))

if userChoice < 1 or userChoice > 3:
    print(" Computer Won You entered invalid number!!", emoji.emojize(":slightly_frowning_face:"))

userChoice = userChoice -1

print("Your Choice was " , signChoice[userChoice])

buddyCompChoice = random.randint(0,2)
print(buddyCompChoice)
print ("Your Buddy Computer Choice was " , signChoice[buddyCompChoice])

if userChoice == buddyCompChoice:
    print( " Its Draw")
elif userChoice == 0 and buddyCompChoice == 2:
    print("You Won, Yeah You Rock Rockstar!!,")


elif userChoice == 2 and buddyCompChoice == 1:
    print("You Won!! Congratulations Champion ")
elif userChoice == 1 and buddyCompChoice == 0:
    print("You Won Awesome Well Played!!")
else:
    print(" Oh Computer Won Better Luck Next Time!!")
