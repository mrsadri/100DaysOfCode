## 0. Module Description
"""
Module name: ...
Functionality: This is a quiz game
Game rule: 
- You will be asked some questions about python programming language. 
- This questioning will be continued until you made your 3rd mistake.
- In future, I will connect this game to a global database and then you can know your rank among others

"""
# -------------------------------------------- #


## 1. External Data models and Libraries
import question_model
import random
# -------------------------------------------- #



## 2. Class Description
"""
Class name: ...
Functionality: ...
"""
class ClassName:
    """
    Class Description is here"""
## -------------------------------------------- #

### 2.1 Functions
    def __init__(self) -> None:
        self.seat = 5
        self.fuel = 60
        self.location = {"x": 0,"y": 0}
        self.speed = 0
        self.question__bank = question_model.python_quiz

    def question_provider(self, question_bank=None):
        if question_bank is None:
            question_bank = self.question__bank

        random_index = random.randrange(1,len(question_bank)) - 1
        needed_question = question_bank.pop(random_index)
        question__bank = question_bank

        return needed_question
    
    def ask_a_question(self):
        allow_to_ask = True
        
        asked_questions = 0
        user_score = 0
        user_mistakes = 0
        while allow_to_ask :
            a_question = self.question_provider()
            asked_questions += 1
            x = input(f"is the following phrase ture or false? (T=True, F=False) \n{a_question['question']}\nEnter your answer: ").lower()
            
            if ((x == "f" and a_question["answer"] == False) or (x == "t" and a_question["answer"] == True)) :
                user_score += 1
                print ("Your answer was CORRECT")
                print ("Let's go for next round")
            else:
                user_mistakes +=1
                print ("Your answer was WRONG")

            if user_mistakes >= 3 :
                allow_to_ask = False
                print(f'Total Questions: {asked_questions}\nScore: {int(user_score/asked_questions*100)/100}%')
        
        
    def start(self):
        self.ask_a_question()
        
# -------------------------------------------- #

### 2.2 Static Variables of the Module
    """
    (Static variables are defined only in the main class, while in other classes, static variables will be defined in the __init__ function.)
    """
    false_counter = 0 

# -------------------------------------------- #

### 2.3 User Entries
# -------------------------------------------- #

### 2.4 Module Actions
game_instance = ClassName()
game_instance.start()
# -------------------------------------------- #
# -------------------------------------------- #


## 3. Draft, Tests, TODO List, References
# -------------------------------------------- #

## 4. Document Tracking: Recording Imports by others
# -------------------------------------------- #