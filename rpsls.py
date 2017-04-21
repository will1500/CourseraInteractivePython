# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "pick rock,spock,paper,lizard, or scissors!"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
  

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    comp_number = random.randrange(0, 5)
    #print comp_number
    # print a blank line to separate consecutive games
    
    # print out the message for the player's choice
    #print player_choice
    #print player_choice 
    player_number =  name_to_number(player_choice)
    #player_number = number_to_name(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_choice = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
  
    #print 'player chose %s'%(player_choice)
    # convert comp_number to comp_choice using the function number_to_name()
    #comp_number = comp_choice = number_to_name(comp_number)
    comp_choice = number_to_name(comp_number)
    
    print 'Computer chose %s'%(comp_choice)
    # print out the message for computer's choice
    #print 'comp chose %s'%(comp_number) 
    # compute difference of comp_number and player_number modulo five
    
    difference = (comp_number - player_choice)
    #print difference
    player_choice = number_to_name(player_choice)
    print 'Player chose %s'%(player_choice)
    # use if/elif/else to determine winner, print winner message
    if (comp_number + 1) % 5 == player_number:
        print "Player wins!"
    elif (comp_number + 2) % 5 == player_number:
        print "Player wins!"
    elif comp_number == player_number:
        print "Player and computer tie!"
    else:
        print "Computer wins!"
    print ""   
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("scissors")


# always remember to check your completed program against the grading rubric

