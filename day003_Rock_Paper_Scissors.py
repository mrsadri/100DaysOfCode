## 1 out of 7: Description
""" 
Class name: ...
Its functionality: ...
"""
# ----------------------- #


## 2 out of 7: Libraries
import random
# ----------------------- #

## 3 out of 7: Functions
def set_random():
    # Select a random choice
    a = random.choice(options)
    print(f"the random ammount that is assigned is '{a}' which means {translator(a)}")
    return a

def translator(a):
    if a in options:
        if a == "r":
            return "rock"
        elif a == "p":
            return "paper"
        elif a == "s":
            return "scissors"
        else:
            print("The wrong choice")

def show_case(a):
    if a in options:
        if a == "r":
            print(rock)
        elif a == "p":
            print(paper)
        elif a == "s":
            print(scissors)
        else:
            print("The wrong choice")

def entry_check(a):
    if a not in options:
        print("Your entry is wrong we will assign a random one to you")
        return set_random()
    else:
        return a

def num_assigner(a):
    if a == "r":
        return int(1)
    elif a == "p":
        return int(2)
    elif a == "s":
        return int(3)
    else:
        a = entry_check(a)
        num_assigner ( a )


def winner_detector(a,b):
    a_num = num_assigner(a)
    b_num = num_assigner (b)
    if ( (a_num > b_num and not (a_num == 3 and b_num == 1)) or (a_num == 1 and b_num == 3) ) :
        print ("You win")
    elif a == b :
        print ("No winners")
    else:
        print ("You lose")
    print(f"a = {a_num}, b = {b_num}")
# ----------------------- #

## 4 out of 7: static variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ["r", "p", "s"]
# ----------------------- #

## 5 out of 7: User entries 
user_choice = input ("let try your chance: R, P or S? ").lower()
# ----------------------- #

## 6 out of 7: The main class action
user_choice = entry_check(user_choice)

pc_choice = set_random()

print(f"\nThis is your choice: {translator(user_choice)}")
show_case(user_choice)

print(f"\nThis is the pc's choice: {translator(pc_choice)}")
show_case(pc_choice)

winner_detector(user_choice,pc_choice)
print(f"user = {user_choice}, PC = {pc_choice}")
# ----------------------- #

## 7 out of 7: Draft, Test, TODO List, Refrences, etc
# ------------------------------------------ #
