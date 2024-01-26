## 1. Description
"""
Class name: ...
Functionality: ...
"""
# -------------------------------------------- #

## 2. Libraries
import random
# -------------------------------------------- #

## 3. Functions
def card_assigner(whose_cards, how_many) :
    random.shuffle(total_cards)
    for _ in range(0,how_many):
        whose_cards.append(list(total_cards.pop(-1)))
    return whose_cards

def pc_logical_card_assigner(computer_cards) :
    while sumCalculator(computer_cards) < 17 :
        computer_cards = card_assigner(computer_cards,1)
    return computer_cards

def pick_one_card (whose_cards):
    return card_assigner(whose_cards, 1)

def sumCalculator(cards):
    sum = 0
    for i in cards :
        sum += badge_to_int(i[1]) 

    p = the_A_counter(cards)
    while ( p > 0 and sum > 21 ) :
        p -= 1
        sum -= 10
        if sum < 11 :
            p = 0
            sum += 10

    return sum

def the_A_counter(cards):
    counter = 0
    for i in cards:
        if i[1] == "A" :
            counter += 1
    return counter

def badge_to_int(string) :
    if string == "J" or string == "Q" or string == "K" :
        return int (10)
    elif string == "A":
        return int (11)
    else:
        return int(string)



def can_continue(cards):

    can_player = {"state" : False , "message" : ""}

    sum = sumCalculator(cards)
    if sum < 21 :
        can_player = {"state" : True , "message" : ""}

    elif sum == 21 :
        can_player = {"state" : False , "message" : ""}

    elif sum > 21 :
        can_player = {"state" : False , "message" : ""}

    else: 
        can_player = {"state" : False , "message" : ""}
    
    return can_player

def winner_check(card_side_one, card_side_two):

    state = "Lose"
    sumA = sumCalculator(card_side_one)
    sumB = sumCalculator(card_side_two)
    
    if sumA == 21 :
        if sumB != 21 :
            state = "Win"
        else:
            state = "Draw"
        return state

    if can_continue(card_side_one)["state"]:
            if sumA > sumB:
                state = "Win"
            elif sumA == sumB :
                state = "Draw"
            elif sumB > 21:
                state = "Win"
            else:
                state = "Lose"
    else:
        if sumB > 21 :
            state = "Draw"
        else: 
            state = "Lose"
    
    return state


# -------------------------------------------- #

## 4. Static Variables
suits = ["♥️", "♦️", "♣️", "♠️"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Create a list of all cards
total_cards = [(suit, rank) for suit in suits for rank in ranks]

# -------------------------------------------- #

## 5. User Entries
# -------------------------------------------- #

## 6. Main Class Action
your_cards = card_assigner([],2)

computer_cards = card_assigner([],2)
computer_cards = pc_logical_card_assigner (computer_cards)
print("First PC card: " , computer_cards[0])
print("Your cards: ", your_cards, "\nSum: ", sumCalculator(your_cards))

if sumCalculator(your_cards) == 21 :
    print("My cards: ",computer_cards, sumCalculator(computer_cards))
    print("You ", winner_check(your_cards,computer_cards))
else: 
    i = can_continue(your_cards)["state"]
    while i:
        if input( 'do you want to pick another? "Y" or "N"? ' ).lower() == "y":
            pick_one_card (your_cards)
            print("Your cards: ", your_cards, "\nSum: ", sumCalculator(your_cards))
            i = can_continue(your_cards)["state"]
            if sumCalculator(your_cards) == 21 :
                print("My cards: ",computer_cards, sumCalculator(computer_cards))
                print("You ", winner_check(your_cards,computer_cards))
                break
        else:
            i = False    
    else:
        print("My cards: ",computer_cards, sumCalculator(computer_cards))
        print("You ", winner_check(your_cards,computer_cards))

# -------------------------------------------- #

## 7. Draft, Tests, TODO List, References
    # TODO: PC gets new cards while its value is lower than 17 : Done
    # TODO: if sum is greater than 21, it goes to check if there is an A, it will changed to 1 : Done
    # TODO: If my card is equal to 21 , there is no need to ask that do you want to continue : Done
    # TODO: Printer to show K,Q,J and A correctly : Done
    # BUG: Why when I reach to 21 it says that I am a looser! : Done
    # Nice to have: Suggesting presseing Y or N based on probability of choosing from remained cards
# -------------------------------------------- #