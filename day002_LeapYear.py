"""
Leap Year Logic
on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
        unless the year is also evenly divisible by 400
"""
import random

# how_many_tries = int(input("let me know how many tries you need: "))

# for how_many_tries in range(1,201,10):

#     accuracy = 0
#     accuracySum = 0

#     for i in range (1,1001):

#         counter = 0
                
#         for x in range(1, how_many_tries):

#             year = random.randrange(1,300000)

#             isLeap = False

#             if year % 400 == 0:
#                 isLeap = True
#             elif year % 100 == 0:
#                 isLeap = False
#             elif year %4 == 0:
#                 isLeap = True

#             if isLeap:
#                 # print(str(year))
#                 counter += 1
            
#         # print(str(  int(counter*400/97/how_many_tries*1000)/1000  ))
#         accuracySum += abs(int(counter*400/97/how_many_tries*1000)/1000 - 1)
#         # print("this is a Leap Year") if isLeap else print("this is NOT a Leap Year")

#     accuracy = round( 100 - accuracySum/10 )

#     print(f"{how_many_tries},{accuracy}%")

try:
    year = int(input ("Please ebnter the year (in #number format): "))

    isLeap = False

    if year % 400 == 0:
        isLeap = True
    elif year % 100 == 0:
        isLeap = False
    elif year %4 == 0:
        isLeap = True

    print("this is a Leap Year") if isLeap else print("this is NOT a Leap Year")
except:
    print("There is an Error")
