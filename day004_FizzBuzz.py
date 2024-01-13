## 1. Description
'''
Class name: ...
Functionality:

    FizzBuzz is a simple but engaging game that tests your understanding of divisibility. Here are the rules:

    Playing:
    - Players take turns counting up from 1.
    - Instead of saying the number:
        If the number is divisible by 3, say "Fizz".
        If the number is divisible by 5, say "Buzz".
        If the number is divisible by both 3 and 5 (a multiple of 15), say "FizzBuzz".
        Otherwise, say the number itself.

    Example:
        1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16...
'''
# -------------------------------------------- #

## 2. Libraries
# -------------------------------------------- #

## 3. Functions
# -------------------------------------------- #

## 4. Static Variables
array_of_numbers = ["1"]
# -------------------------------------------- #

## 5. User Entries
# -------------------------------------------- #

## 6. Main Class Action
for number in range(2,101):
    if number % 15 == 0 :
        array_of_numbers.append("FizzBuzz")
    elif number % 5 == 0 :
        array_of_numbers.append("Buzz")
    elif number % 3 == 0 :
        array_of_numbers.append("Fizz")
    else:
        array_of_numbers.append(str(number))

print (array_of_numbers)
# -------------------------------------------- #

## 7. Draft, Tests, TODO List, References
# -------------------------------------------- #