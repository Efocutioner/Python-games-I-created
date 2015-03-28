import random

game = ["Rock", "Paper", "Scissors"]

print "\nWelcome to can you beat the computer\n"
rule = "The rules are simple, just pick either: \nRock, Paper, or Scissors \nand see if you can beat the computer."
print rule 
print
print "Well lets begin....\n"
print "Now pick:"
print
print " ".join(game)
print
#This is where I take the person input
user_input = raw_input("What is your guess: ")
user_input = user_input.lower()
while user_input != "rock" and user_input != "paper" and user_input != "scissors":
	print user_input
	user_input = raw_input("Seriously! What is your choice: ")

# this is where the computer choose a number at random
luck = random.randint(0,2)
if luck == 0:
	luck = "rock"
elif luck == 1:
	luck = "paper"
elif luck == 2:
	luck = "scissors"
else:
	luck = "whoa.... that's not right"
	
# This is where that random choice is compared to user input
if user_input == luck:
	print "You got lucky it's a draw"
elif user_input == "rock":
	if luck == "paper":
		print "The computer wins..."
	else:
		print "Not bad... you win"
elif user_input == "paper":
	if luck == "scissors":
		print "The computer wins..."
	else:
		print "Not bad... you win"
elif user_input == "scissors":
	if luck == "rock":
		print "The computer wins..."
	else:
		print "Not bad... you win"

print		
print "You choose: " + user_input + "\nand the computer choose: " + luck + "\nCongrads on playing my first game."
	