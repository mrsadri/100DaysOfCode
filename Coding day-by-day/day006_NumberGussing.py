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

# -------------------------------------------- #

## 4. Static Variables
the_upper_limit_of_the_interval = 1024
theـlowerـlimitـofـtheـinterval = 1
the_random_number = random.randrange(theـlowerـlimitـofـtheـinterval,the_upper_limit_of_the_interval+1)
level_of_difficulty = "easy"
"""
On easy mode you can guess 10 times and you will have an assitant to help you choose the right value
"""
# -------------------------------------------- #

## 5. User Entries
# -------------------------------------------- #

## 6. Main Class Action
print("the random number is:", the_random_number)

attempts = 0
the_guessedـnumber = theـlowerـlimitـofـtheـinterval
while the_guessedـnumber != the_random_number :
    the_suggested_number = int(   (the_upper_limit_of_the_interval + theـlowerـlimitـofـtheـinterval)/2   )
    print("The suggested number is:", str(the_suggested_number))
    the_guessedـnumber = int(input("Pleae try youer cahnce: ")) 
    # the_guessedـnumber = the_suggested_number #Automated
    attempts += 1
    print("ok, let me check")
    if the_guessedـnumber > the_random_number :
        the_upper_limit_of_the_interval = min (the_guessedـnumber, the_upper_limit_of_the_interval)
        print ("It is too high")
    elif the_guessedـnumber < the_random_number: 
        theـlowerـlimitـofـtheـinterval = max (the_guessedـnumber, theـlowerـlimitـofـtheـinterval)
        print("It is too low")
    else:
        print(f"You finally won after {attempts} attempts, congratulations.")

# -------------------------------------------- #

## 7. Draft, Tests, TODO List, References
# -------------------------------------------- #
